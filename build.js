const fs = require('fs');
const path = require('path');

const IGNORE_LIST = ['.git', '.github', 'src', 'node_modules', 'build.js', 'README.md', '.DS_Store'];
const ROOT_DIR = __dirname;
const SITE_TITLE = "Estudios de Psicología";

function getIcon(filename, isDirectory) {
  if (isDirectory) return '<div class="card-icon folder-icon">📁</div>';
  const ext = path.extname(filename).toLowerCase();
  if (ext === '.pdf') return '<div class="card-icon file-pdf">📄</div>';
  if (ext === '.html' || ext === '.htm') return '<div class="card-icon file-html">🌐</div>';
  if (ext === '.doc' || ext === '.docx') return '<div class="card-icon file-doc">📝</div>';
  return '<div class="card-icon file-default">📎</div>';
}

function generateHTML(title, isRoot, items, relativePathToRoot) {
  const cardsHTML = items.map(item => {
    const icon = getIcon(item.name, item.isDirectory);
    // Links logic: 
    // If it's a directory, link points to that directory's index.html
    // If it's a file, link points to the file itself, opening in new tab
    const href = item.isDirectory ? `${item.name}/index.html` : item.name;
    const target = item.isDirectory ? '' : ' target="_blank" rel="noopener noreferrer"';
    
    return `
      <a href="${href}" class="card"${target}>
        ${icon}
        <div class="card-title">${item.name}</div>
        <div class="card-meta">${item.isDirectory ? 'Carpeta' : 'Archivo'}</div>
      </a>
    `;
  }).join('\n');

  const backLink = isRoot ? '' : `
    <a href="${relativePathToRoot}index.html" class="back-link">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
      Volver al inicio
    </a>
  `;

  return `<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>${title} | ${SITE_TITLE}</title>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;800&family=Poppins:wght@500;700;800&display=swap" rel="stylesheet">
  <meta name="theme-color" content="#f4f7f6">
  <link rel="stylesheet" href="${relativePathToRoot}src/style.css">
</head>
<body>
  <div class="container">
    ${backLink}
    <header>
      <h1>${title === SITE_TITLE ? 'Mis Estudios de Psicología' : title}</h1>
      <p class="subtitle">${isRoot ? 'Selecciona una asignatura o tema' : 'Documentos y recursos'}</p>
    </header>
    <main class="grid">
      ${cardsHTML.length > 0 ? cardsHTML : '<p style="text-align: center; grid-column: 1/-1; color: var(--text-muted)">No hay elementos en esta carpeta.</p>'}
    </main>
  </div>
</body>
</html>`;
}

function processDirectory(currentPath, relativePathToRoot) {
  const dirName = path.basename(currentPath);
  const title = currentPath === ROOT_DIR ? SITE_TITLE : dirName;
  const isRoot = currentPath === ROOT_DIR;

  const entries = fs.readdirSync(currentPath, { withFileTypes: true });
  
  const items = entries
    .filter(entry => !IGNORE_LIST.includes(entry.name) && !entry.name.startsWith('.'))
    .filter(entry => entry.name !== 'index.html' && !entry.name.endsWith('.js') && !entry.name.endsWith('.json')) // Hide index.html, JS and JSON config files
    .map(entry => {
      const isDirectory = entry.isDirectory();
      if (isDirectory) {
        // Recursively process this sub-directory
        processDirectory(path.join(currentPath, entry.name), relativePathToRoot + '../');
      }
      return { name: entry.name, isDirectory };
    });

  // Sort: Directories first, then files, alphabetically
  items.sort((a, b) => {
    if (a.isDirectory && !b.isDirectory) return -1;
    if (!a.isDirectory && b.isDirectory) return 1;
    return a.name.localeCompare(b.name);
  });

  const html = generateHTML(title, isRoot, items, relativePathToRoot);
  fs.writeFileSync(path.join(currentPath, 'index.html'), html);
  console.log(`Generated index.html in ${currentPath}`);
}

// Start processing from root
console.log('Starting static site build...');
processDirectory(ROOT_DIR, '');
console.log('Build completed successfully!');
