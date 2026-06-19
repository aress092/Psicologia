const fs = require('fs');
const path = require('path');
const pdf = require('pdf-parse');

const ROOT_DIR = __dirname;
const IGNORE_LIST = ['.git', '.github', 'src', 'node_modules'];
const NOTAS_DIR = path.join(ROOT_DIR, '.notas');

// Ensure .notas directory exists
if (!fs.existsSync(NOTAS_DIR)) {
  fs.mkdirSync(NOTAS_DIR);
  console.log('Created .notas directory.');
}

function findPDFs(dir, pdfList) {
  const entries = fs.readdirSync(dir, { withFileTypes: true });

  for (const entry of entries) {
    if (IGNORE_LIST.includes(entry.name) || (entry.name.startsWith('.') && entry.name !== '.notas')) {
      continue;
    }

    const fullPath = path.join(dir, entry.name);

    if (entry.isDirectory()) {
      findPDFs(fullPath, pdfList);
    } else if (entry.name.toLowerCase().endsWith('.pdf')) {
      pdfList.push(fullPath);
    }
  }
}

async function generateMDs() {
  const allPDFs = [];
  findPDFs(ROOT_DIR, allPDFs);

  let generatedCount = 0;

  for (const pdfPath of allPDFs) {
    const baseName = path.basename(pdfPath, path.extname(pdfPath));
    const mdFilename = `${baseName}.md`;
    const mdPath = path.join(NOTAS_DIR, mdFilename);

    if (!fs.existsSync(mdPath)) {
      try {
        console.log(`Extracting text from ${pdfPath}...`);
        const dataBuffer = fs.readFileSync(pdfPath);
        const data = await pdf(dataBuffer);
        
        const template = `# ${baseName}\n\n${data.text}\n`;
        fs.writeFileSync(mdPath, template);
        console.log(`Generated ${mdFilename} with extracted text.`);
        generatedCount++;
      } catch (error) {
        console.error(`Failed to extract text from ${pdfPath}:`, error);
      }
    }
  }

  if (generatedCount === 0) {
    console.log('No new PDFs found or all PDFs already have their .md files.');
  } else {
    console.log(`Successfully generated ${generatedCount} new .md files with extracted text.`);
  }
}

generateMDs();
