const fs = require("fs");
const path = require("path");
const {
  AlignmentType,
  BorderStyle,
  Document,
  Footer,
  HeadingLevel,
  ImageRun,
  LevelFormat,
  Packer,
  PageNumber,
  Paragraph,
  ShadingType,
  Table,
  TableCell,
  TableRow,
  TextRun,
  VerticalAlign,
  WidthType,
} = require("docx");

function arg(name, fallback = null) {
  const flag = `--${name}`;
  const i = process.argv.indexOf(flag);
  return i >= 0 && i + 1 < process.argv.length ? process.argv[i + 1] : fallback;
}

const mdPath = path.resolve(arg("md") || "");
const outPath = path.resolve(arg("out") || "review_output.docx");
const imageWidth = Number(arg("image-width", "630"));
const maxImageHeight = Number(arg("image-height", "460"));

if (!mdPath || !fs.existsSync(mdPath)) {
  throw new Error("Usage: node scripts/build_review_docx.js --md manuscript.md --out manuscript.docx");
}

const mdDir = path.dirname(mdPath);
const md = fs.readFileSync(mdPath, "utf8").replace(/\r\n/g, "\n");

function cleanText(s) {
  return s.replace(/\\\*/g, "*").trim();
}

function runs(text, opts = {}) {
  const parts = [];
  const re = /(\*\*[^*]+\*\*|\*[^*]+\*)/g;
  let last = 0;
  for (const m of text.matchAll(re)) {
    if (m.index > last) parts.push({ text: text.slice(last, m.index) });
    const markupSegment = m[0];
    if (markupSegment.startsWith("**")) parts.push({ text: markupSegment.slice(2, -2), bold: true });
    else parts.push({ text: markupSegment.slice(1, -1), italics: true });
    last = m.index + markupSegment.length;
  }
  if (last < text.length) parts.push({ text: text.slice(last) });
  return parts.filter((p) => p.text.length).map((p) => new TextRun({
    text: p.text,
    bold: p.bold || opts.bold,
    italics: p.italics || opts.italics,
    size: opts.size || 22,
    font: "Arial",
    color: opts.color || "111111",
  }));
}

function para(text, options = {}) {
  return new Paragraph({
    alignment: options.alignment,
    heading: options.heading,
    numbering: options.numbering,
    spacing: options.spacing || { before: 80, after: 120, line: 300 },
    indent: options.indent,
    children: runs(cleanText(text), { size: options.size || 22, color: options.color }),
  });
}

function tableFromRows(rows) {
  const widths = Array(rows[0].length).fill(Math.floor(9360 / rows[0].length));
  const line = { style: BorderStyle.SINGLE, size: 1, color: "B7C0C7" };
  const borders = { top: line, bottom: line, left: line, right: line };
  return new Table({
    width: { size: 100, type: WidthType.PERCENTAGE },
    columnWidths: widths,
    margins: { top: 90, bottom: 90, left: 120, right: 120 },
    rows: rows.map((row, r) => new TableRow({
      tableHeader: r === 0,
      children: row.map((cell, c) => new TableCell({
        borders,
        width: { size: widths[c], type: WidthType.DXA },
        verticalAlign: VerticalAlign.CENTER,
        shading: r === 0 ? { fill: "DCECEF", type: ShadingType.CLEAR } : undefined,
        children: [new Paragraph({
          alignment: r === 0 ? AlignmentType.CENTER : AlignmentType.LEFT,
          spacing: { before: 40, after: 40 },
          children: runs(cell, { size: 18, color: "111111", bold: r === 0 }),
        })],
      })),
    })),
  });
}

function imageSize(buffer, ext) {
  if (ext === "png" && buffer.slice(1, 4).toString("ascii") === "PNG") {
    return { width: buffer.readUInt32BE(16), height: buffer.readUInt32BE(20) };
  }
  if ((ext === "jpg" || ext === "jpeg") && buffer[0] === 0xff && buffer[1] === 0xd8) {
    let i = 2;
    while (i < buffer.length) {
      if (buffer[i] !== 0xff) break;
      const marker = buffer[i + 1];
      const len = buffer.readUInt16BE(i + 2);
      if (marker >= 0xc0 && marker <= 0xc3) {
        return { height: buffer.readUInt16BE(i + 5), width: buffer.readUInt16BE(i + 7) };
      }
      i += 2 + len;
    }
  }
  return { width: 16, height: 9 };
}

function imagePara(src) {
  const imagePath = path.resolve(mdDir, src);
  const base = path.basename(src);
  if (!fs.existsSync(imagePath)) throw new Error(`Missing image: ${imagePath}`);
  const ext = path.extname(imagePath).toLowerCase().slice(1);
  const type = ext === "jpg" ? "jpeg" : ext;
  const data = fs.readFileSync(imagePath);
  const size = imageSize(data, ext);
  let width = imageWidth;
  let height = Math.round(width * size.height / size.width);
  if (height > maxImageHeight) {
    height = maxImageHeight;
    width = Math.round(height * size.width / size.height);
  }
  return new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { before: 180, after: 80 },
    children: [new ImageRun({
      type,
      data,
      transformation: { width, height },
      altText: {
        title: base.replace(/_/g, " "),
        description: base,
        name: base.replace(/\.[^.]+$/, ""),
      },
    })],
  });
}

const children = [];
const lines = md.split("\n");
let inRefs = false;
let i = 0;

while (i < lines.length) {
  const line = lines[i].trim();
  if (!line) {
    i += 1;
    continue;
  }

  if (line.startsWith("# ")) {
    children.push(new Paragraph({
      heading: HeadingLevel.TITLE,
      alignment: AlignmentType.CENTER,
      spacing: { before: 240, after: 220 },
      children: [new TextRun({ text: line.slice(2), bold: true, size: 40, font: "Arial", color: "123A40" })],
    }));
    i += 1;
    continue;
  }

  if (line.startsWith("## ")) {
    const title = line.slice(3);
    inRefs = title === "References";
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_1,
      spacing: { before: 260, after: 120 },
      children: [new TextRun({ text: title, bold: true, size: 28, font: "Arial", color: "123A40" })],
    }));
    i += 1;
    continue;
  }

  if (line.startsWith("![")) {
    const m = line.match(/\]\(([^)]+)\)/);
    if (m) children.push(imagePara(m[1]));
    i += 1;
    continue;
  }

  if (line.startsWith("|")) {
    const rows = [];
    while (i < lines.length && lines[i].trim().startsWith("|")) {
      const raw = lines[i].trim();
      if (!/^\|\s*[-:]+/.test(raw)) rows.push(raw.slice(1, -1).split("|").map((x) => x.trim()));
      i += 1;
    }
    if (rows.length) {
      children.push(tableFromRows(rows));
      children.push(new Paragraph({ spacing: { after: 120 }, children: [] }));
    }
    continue;
  }

  if (line.startsWith("- ")) {
    children.push(para(line.slice(2), {
      numbering: { reference: "bullet-list", level: 0 },
      spacing: { before: 30, after: 70, line: 280 },
    }));
    i += 1;
    continue;
  }

  if (inRefs && /^\d+\.\s/.test(line)) {
    children.push(para(line, {
      size: 18,
      spacing: { before: 20, after: 80, line: 250 },
      indent: { left: 360, hanging: 360 },
    }));
    i += 1;
    continue;
  }

  const isCaption = /^\*\*Figure \d+\./.test(line) || /^\*\*Table \d+\./.test(line);
  children.push(para(line, {
    size: isCaption ? 19 : 22,
    color: isCaption ? "333333" : "111111",
    spacing: isCaption ? { before: 40, after: 180, line: 260 } : undefined,
  }));
  i += 1;
}

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      {
        id: "Heading1",
        name: "Heading 1",
        basedOn: "Normal",
        next: "Normal",
        quickFormat: true,
        run: { size: 28, bold: true, color: "123A40", font: "Arial" },
        paragraph: { spacing: { before: 260, after: 120 }, outlineLevel: 0 },
      },
      {
        id: "Title",
        name: "Title",
        basedOn: "Normal",
        run: { size: 40, bold: true, color: "123A40", font: "Arial" },
        paragraph: { alignment: AlignmentType.CENTER, spacing: { before: 240, after: 220 } },
      },
    ],
  },
  numbering: {
    config: [{
      reference: "bullet-list",
      levels: [{
        level: 0,
        format: LevelFormat.BULLET,
        text: "\u2022",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 540, hanging: 260 } } },
      }],
    }],
  },
  sections: [{
    properties: { page: { margin: { top: 1080, right: 1080, bottom: 1080, left: 1080 } } },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ text: "Page ", size: 18 }),
            new TextRun({ children: [PageNumber.CURRENT], size: 18 }),
          ],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buffer) => {
  fs.mkdirSync(path.dirname(outPath), { recursive: true });
  fs.writeFileSync(outPath, buffer);
  console.log(outPath);
});
