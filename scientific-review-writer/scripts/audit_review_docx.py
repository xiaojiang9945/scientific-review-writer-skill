import argparse
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def para_text(par):
    return "".join(t.text or "" for t in par.findall(".//w:t", NS)).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--docx", required=True)
    ap.add_argument("--expect-figures", type=int, default=None)
    ap.add_argument("--expect-tables", type=int, default=None)
    ap.add_argument("--min-references", type=int, default=None)
    args = ap.parse_args()

    docx = Path(args.docx)
    with zipfile.ZipFile(docx) as z:
        xml = z.read("word/document.xml")
        media = [n for n in z.namelist() if n.startswith("word/media/") and not n.endswith("/")]

    root = ET.fromstring(xml)
    paras = []
    image_paras = 0
    for par in root.findall(".//w:p", NS):
        text = para_text(par)
        if text:
            paras.append(text)
        elif par.findall(".//w:drawing", NS):
            image_paras += 1

    text = "\n\n".join(paras)
    try:
        ref_start = paras.index("References")
        ref_paras = paras[ref_start + 1 :]
    except ValueError:
        ref_paras = []
    refs = [p for p in ref_paras if re.match(r"^\d+\. ", p)]
    fig_caps = [p for p in paras if re.match(r"^Figure \d+\. ", p)]
    table_count = len(root.findall(".//w:tbl", NS))
    figures_ok = args.expect_figures is None or len(media) == args.expect_figures == len(fig_caps)
    tables_ok = args.expect_tables is None or table_count == args.expect_tables
    refs_ok = args.min_references is None or len(refs) >= args.min_references

    citations = []
    body = text.split("References", 1)[0]
    for m in re.finditer(r"\[(\d+(?:-\d+)?(?:,\s*\d+(?:-\d+)?)*)\]", body):
        for part in re.split(r",\s*", m.group(1)):
            if "-" in part:
                a, b = map(int, part.split("-"))
                citations.extend(range(a, b + 1))
            else:
                citations.append(int(part))
    ref_nums = [int(re.match(r"^(\d+)\. ", r).group(1)) for r in refs]
    seen = []
    for n in citations:
        if n not in seen:
            seen.append(n)

    out = {
        "docx": str(docx.resolve()),
        "size_bytes": docx.stat().st_size,
        "paragraphs": len(paras),
        "image_paragraphs": image_paras,
        "embedded_media": len(media),
        "figure_captions": len(fig_caps),
        "tables": table_count,
        "references": len(refs),
        "citation_markers": len(re.findall(r"\[\d", body)),
        "first_citation_order_ok": seen == sorted(seen),
        "citation_reference_parity": set(citations) == set(ref_nums),
        "figures_ok": figures_ok,
        "tables_ok": tables_ok,
        "references_ok": refs_ok,
        "has_outstanding_questions": "Outstanding Questions" in text,
        "has_keywords": "Keywords:" in text,
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    if not (figures_ok and tables_ok and refs_ok and out["first_citation_order_ok"] and out["citation_reference_parity"]):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
