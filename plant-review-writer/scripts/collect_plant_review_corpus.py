import csv
import json
import re
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


OUT = Path("outputs/plant_review_skill_work")
OUT.mkdir(parents=True, exist_ok=True)

SOURCES = {
    "Nature": "S137773608",
    "Science": "S3880285",
    "Cell": "S110447773",
    "Nature Biotechnology": "S106963461",
    "Nature Plants": "S2764671299",
    "The Plant Cell": "S48849333",
    "Annual Review of Plant Biology": "S176558078",
    "Trends in Plant Science": "S201780205",
}

PLANT_FOCUSED = {
    "Nature Plants",
    "The Plant Cell",
    "Annual Review of Plant Biology",
    "Trends in Plant Science",
}

PLANT_TERMS = [
    "plant", "plants", "crop", "crops", "agriculture", "agricultural",
    "arabidopsis", "wheat", "rice", "maize", "barley", "soybean", "sorghum",
    "tomato", "potato", "cassava", "cotton", "rapeseed", "brassica",
    "seed", "germination", "root", "shoot", "leaf", "flowering", "stomata",
    "chloroplast", "photosynthesis", "phytohormone", "auxin", "aba",
    "gibberellin", "ethylene", "cytokinin", "strigolactone", "jasmonate",
    "plant immunity", "pathogen", "microbiome", "rhizosphere", "mycorrhiza",
    "drought", "salinity", "heat stress", "cold stress", "nutrient",
    "nitrogen", "phosphorus", "genome editing", "crispr", "breeding",
    "phenotyping", "synthetic biology", "cell wall", "xylem", "phloem",
]

CORE_PLANT_TERMS = [
    "plant", "plants", "crop", "crops", "agriculture", "agricultural",
    "arabidopsis", "wheat", "rice", "maize", "barley", "soybean", "sorghum",
    "tomato", "potato", "cassava", "cotton", "rapeseed", "brassica",
    "seed", "root", "shoot", "leaf", "flowering", "stomata", "chloroplast",
    "photosynthesis", "phytohormone", "rhizosphere", "mycorrhiza", "soil", "cell wall",
    "xylem", "phloem", "forest", "grassland",
]

NEGATIVE_TERMS = [
    "cancer", "tumor", "oncology", "patient", "human", "mammal", "mouse",
    "mice", "neuron", "brain", "virus vaccine", "sars-cov-2", "covid",
    "clinical", "immune checkpoint", "exosome", "extracellular vesicle",
]


def openalex(path, params):
    url = f"https://api.openalex.org/{path}?{urlencode(params)}"
    req = Request(url, headers={"User-Agent": "codex-plant-review-skill/1.0"})
    with urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def inv_to_text(inv):
    if not inv:
        return ""
    pairs = []
    for word, positions in inv.items():
        for pos in positions:
            pairs.append((pos, word))
    return " ".join(w for _, w in sorted(pairs))


def source_name(work):
    loc = work.get("primary_location") or {}
    source = loc.get("source") or {}
    return source.get("display_name") or ""


def authors_short(work):
    authors = []
    for a in work.get("authorships") or []:
        au = a.get("author") or {}
        if au.get("display_name"):
            authors.append(au["display_name"])
        if len(authors) >= 3:
            break
    if not authors:
        return ""
    suffix = " et al." if len(work.get("authorships") or []) > 3 else ""
    return ", ".join(authors) + suffix


def text_blob(work):
    fields = [
        work.get("display_name") or "",
        inv_to_text(work.get("abstract_inverted_index")),
        source_name(work),
    ]
    for k in work.get("keywords") or []:
        fields.append(k.get("display_name") or "")
    topic = work.get("primary_topic") or {}
    fields.append(topic.get("display_name") or "")
    for t in work.get("topics") or []:
        fields.append(t.get("display_name") or "")
    return " ".join(fields).lower()


def plant_score(work):
    blob = text_blob(work)
    score = sum(1 for t in PLANT_TERMS if t in blob)
    score -= sum(1 for t in NEGATIVE_TERMS if t in blob)
    return score


def is_plant_related(work):
    src = source_name(work)
    if src in PLANT_FOCUSED:
        return True
    blob = text_blob(work)
    title = (work.get("display_name") or "").lower()
    core_hits = sum(1 for t in CORE_PLANT_TERMS if t in blob)
    title_core_hits = sum(1 for t in CORE_PLANT_TERMS if t in title)
    biomedical_hits = sum(1 for t in NEGATIVE_TERMS if t in blob)
    return title_core_hits >= 1 and core_hits >= 2 and plant_score(work) >= 2 and biomedical_hits <= 1


def best_fulltext(work):
    content = work.get("content_urls") or {}
    oa = work.get("open_access") or {}
    best = work.get("best_oa_location") or {}
    loc = work.get("primary_location") or {}
    candidates = [
        content.get("grobid_xml"),
        content.get("pdf"),
        best.get("pdf_url"),
        best.get("landing_page_url"),
        oa.get("oa_url"),
        loc.get("landing_page_url"),
    ]
    candidates = [c for c in candidates if c]
    status = "open-fulltext-link" if any(c for c in candidates[:5]) else "publisher-landing-only"
    if content.get("grobid_xml"):
        status = "openalex-grobid-fulltext"
    elif content.get("pdf") or best.get("pdf_url"):
        status = "open-pdf"
    elif oa.get("is_oa"):
        status = "oa-landing"
    return status, candidates[0] if candidates else ""


def collect():
    works = {}
    select = ",".join([
        "id", "doi", "display_name", "publication_year", "publication_date",
        "primary_location", "best_oa_location", "open_access", "cited_by_count",
        "type", "authorships", "abstract_inverted_index", "biblio",
        "content_urls", "has_content", "primary_topic", "topics", "keywords",
    ])
    for label, sid in SOURCES.items():
        page = 1
        while True:
            data = openalex("works", {
                "filter": f"primary_location.source.id:{sid},from_publication_date:2020-01-01,to_publication_date:2026-05-22,type:review",
                "per-page": 200,
                "page": page,
                "sort": "cited_by_count:desc",
                "select": select,
            })
            results = data.get("results") or []
            if not results:
                break
            for w in results:
                if is_plant_related(w):
                    works[w["id"]] = w
            if len(results) < 200:
                break
            page += 1
            time.sleep(0.2)
    return sorted(works.values(), key=lambda w: (w.get("cited_by_count") or 0), reverse=True)


def write_outputs(works):
    rows = []
    for i, w in enumerate(works, 1):
        status, fulltext_url = best_fulltext(w)
        abstract = inv_to_text(w.get("abstract_inverted_index"))
        title = re.sub(r"<[^>]+>", "", w.get("display_name") or "")
        rows.append({
            "rank": i,
            "title": title,
            "year": w.get("publication_year") or "",
            "date": w.get("publication_date") or "",
            "journal": source_name(w),
            "authors": authors_short(w),
            "cited_by_count": w.get("cited_by_count") or 0,
            "doi": w.get("doi") or "",
            "openalex_id": w.get("id") or "",
            "fulltext_status": status,
            "fulltext_url": fulltext_url,
            "topic": ((w.get("primary_topic") or {}).get("display_name") or ""),
            "abstract": abstract,
        })
    tsv = OUT / "plant_review_corpus_2020_2026_top250.tsv"
    with tsv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(rows[:250])
    quotas = {
        "Trends in Plant Science": 45,
        "Annual Review of Plant Biology": 40,
        "Nature Plants": 30,
        "The Plant Cell": 30,
        "Science": 20,
        "Cell": 10,
        "Nature": 10,
        "Nature Biotechnology": 10,
    }
    balanced = []
    used = set()
    for journal, quota in quotas.items():
        journal_rows = [r for r in rows if r["journal"] == journal]
        for r in journal_rows[:quota]:
            balanced.append(r)
            used.add(r["openalex_id"])
    for r in rows:
        if len(balanced) >= 250:
            break
        if r["openalex_id"] not in used:
            balanced.append(r)
            used.add(r["openalex_id"])
    balanced_tsv = OUT / "plant_review_corpus_2020_2026_source_balanced250.tsv"
    with balanced_tsv.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter="\t")
        writer.writeheader()
        writer.writerows(balanced[:250])
    counts = {}
    status_counts = {}
    for r in balanced[:250]:
        counts[r["journal"]] = counts.get(r["journal"], 0) + 1
        status_counts[r["fulltext_status"]] = status_counts.get(r["fulltext_status"], 0) + 1
    summary = OUT / "corpus_summary.md"
    with summary.open("w", encoding="utf-8") as f:
        f.write("# Plant Review Corpus Summary\n\n")
        f.write("Source: OpenAlex works API. Date filter: 2020-01-01 to 2026-05-22. Type filter: review.\n\n")
        f.write(f"Collected plant-related reviews: {len(works)}. Top records exported: {min(250, len(rows))}. Source-balanced records exported: {min(250, len(balanced))}.\n\n")
        f.write("## Journal Counts In Source-Balanced Export\n\n")
        for k, v in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
            f.write(f"- {k}: {v}\n")
        f.write("\n## Full-Text Link Status In Source-Balanced Export\n\n")
        for k, v in sorted(status_counts.items(), key=lambda x: (-x[1], x[0])):
            f.write(f"- {k}: {v}\n")
        f.write("\n## Top 30 By Citation Count\n\n")
        for r in rows[:30]:
            f.write(f"{r['rank']}. {r['title']} ({r['journal']}, {r['year']}; citations: {r['cited_by_count']}) {r['doi']}\n")
    return tsv, balanced_tsv, summary


if __name__ == "__main__":
    works = collect()
    if len(works) < 200:
        raise SystemExit(f"Only collected {len(works)} plant-related reviews; broaden filters before building the skill.")
    tsv, balanced_tsv, summary = write_outputs(works)
    print(f"collected={len(works)}")
    print(tsv)
    print(balanced_tsv)
    print(summary)
