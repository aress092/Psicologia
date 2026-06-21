import os
import re

IGNORE_LIST = {'.git', '.github', 'src', 'node_modules', 'build.js', 'build.py', 'README.md', '.DS_Store', '.preguntas', '.notas'}
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_TITLE = "Estudios de Psicología"

def get_icon(filename, is_directory):
    if is_directory:
        return '<div class="card-icon folder-icon">📁</div>'
    ext = os.path.splitext(filename)[1].lower()
    if ext == '.pdf':
        return '<div class="card-icon file-pdf">📄</div>'
    if ext in ('.html', '.htm'):
        return '<div class="card-icon file-html">🌐</div>'
    if ext in ('.doc', '.docx'):
        return '<div class="card-icon file-doc">📝</div>'
    return '<div class="card-icon file-default">📎</div>'

def generate_html(title, is_root, items, relative_path_to_root):
    cards_html = []
    for item in items:
        icon = get_icon(item['name'], item['is_directory'])
        href = f"{item['name']}/index.html" if item['is_directory'] else item['name']
        target = '' if item['is_directory'] else ' target="_blank" rel="noopener noreferrer"'
        card_class = 'folder-card' if item['is_directory'] else 'file-card'
        
        cards_html.append(f"""
      <a href="{href}" class="card {card_class}"{target}>
        {icon}
        <div class="card-title">{item['name']}</div>
        <div class="card-meta">{'Carpeta' if item['is_directory'] else 'Archivo'}</div>
      </a>
        """)
    cards_str = '\n'.join(cards_html)
    
    back_link = "" if is_root else f"""
    <a href="{relative_path_to_root}index.html" class="back-link">
      <svg fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path></svg>
      Volver al inicio
    </a>
    """
    
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} | {SITE_TITLE}</title>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600&family=Lora:ital,wght@0,400;0,500;0,600;1,400&display=swap" rel="stylesheet">
  <meta name="theme-color" content="#fcfbfa">
  <link rel="stylesheet" href="{relative_path_to_root}src/style.css">
</head>
<body>
  <div class="container">
    {back_link}
    <header>
      <h1>{'Mis Estudios de Psicología' if title == SITE_TITLE else title}</h1>
      <p class="subtitle">{'Selecciona una asignatura o tema' if is_root else 'Documentos y recursos'}</p>
    </header>
    <main class="grid">
      {cards_str if cards_str else '<p style="text-align: center; grid-column: 1/-1; color: var(--text-muted)">No hay elementos en esta carpeta.</p>'}
    </main>
  </div>
</body>
</html>"""
    return html

def process_directory(current_path, relative_path_to_root):
    dir_name = os.path.basename(current_path)
    title = SITE_TITLE if current_path == ROOT_DIR else dir_name
    is_root = current_path == ROOT_DIR

    entries = os.listdir(current_path)
    items = []
    
    for name in entries:
        if name in IGNORE_LIST or name.startswith('.'):
            continue
        if name == 'index.html' or name.endswith('.js') or name.endswith('.json') or name.endswith('.py'):
            continue
        
        full_path = os.path.join(current_path, name)
        is_directory = os.path.isdir(full_path)
        
        if is_directory:
            process_directory(full_path, relative_path_to_root + '../')
            
        items.append({'name': name, 'is_directory': is_directory})
        
    items.sort(key=lambda x: (not x['is_directory'], x['name']))
    
    html = generate_html(title, is_root, items, relative_path_to_root)
    with open(os.path.join(current_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Generated index.html in {current_path}")

print('Starting static site build (Python version)...')
process_directory(ROOT_DIR, '')
print('Build completed successfully!')
