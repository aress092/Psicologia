import os
import re
import random

dir_path = '/home/ares/Psicologia/CME/.preguntas/'
files = [
    'q_t1.js', 'q_t1_v2.js', 'q_t1_v3.js',
    'q_t2.js', 'q_t2_v2.js', 'q_t2_v3.js',
    'q_t3.js', 'q_t3_v2.js', 'q_t3_v3.js',
    'q_t4.js', 'q_t4_v2.js', 'q_t4_v3.js'
]

all_qs = []

# Basic regex to parse the javascript objects
# We are looking for { theme: "...", question: "...", options: ["...","...","...","..."], correct: ..., justification: "..." }
pattern = re.compile(r'\{\s*theme:\s*"(.*?)",\s*question:\s*"(.*?)",\s*options:\s*\[(.*?)\],\s*correct:\s*(\d+),\s*justification:\s*"(.*?)"\s*\}', re.DOTALL)

for f in files:
    path = os.path.join(dir_path, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            matches = pattern.findall(content)
            for m in matches:
                theme, question, options_str, correct, justification = m
                
                # options are separated by commas and quotes
                opts = re.findall(r'"(.*?)"', options_str)
                all_qs.append({
                    'theme': theme,
                    'question': question,
                    'options': opts
                })

print(f"Total questions loaded: {len(all_qs)}")

# Simulacro de 30 preguntas
random.shuffle(all_qs)
test_qs = all_qs[:30]

with open('/home/ares/Psicologia/CME/Simulacro_CME_Imprimible.md', 'w', encoding='utf-8') as out:
    out.write("# Simulacro Examen CME (Sin Respuestas)\n\n")
    out.write("> Un test aleatorio de 30 preguntas mezcladas de todos los temas. ¡Anota tus opciones en un papel!\n\n---\n\n")
    for i, q in enumerate(test_qs):
        clean_q = re.sub(r'^\d+\.\s*', '', q['question'])
        out.write(f"### {i+1}. {clean_q}\n\n")
        letters = ['A', 'B', 'C', 'D']
        for j, opt in enumerate(q['options']):
            out.write(f"- [ ] **{letters[j]})** {opt}\n")
        out.write("\n")

print("Generado Simulacro_CME_Imprimible.md")

# Todo el Banco
all_qs.sort(key=lambda x: x['theme'])
with open('/home/ares/Psicologia/CME/Banco_CME_Completo_Imprimible.md', 'w', encoding='utf-8') as out:
    out.write(f"# Todo el Banco de Preguntas CME (Sin Respuestas)\n\n")
    out.write(f"> Total de preguntas: {len(all_qs)}\n\n---\n\n")
    for i, q in enumerate(all_qs):
        clean_q = re.sub(r'^\d+\.\s*', '', q['question'])
        out.write(f"### {i+1}. [{q['theme']}] {clean_q}\n\n")
        letters = ['A', 'B', 'C', 'D']
        for j, opt in enumerate(q['options']):
            out.write(f"- [ ] **{letters[j]})** {opt}\n")
        out.write("\n")

print("Generado Banco_CME_Completo_Imprimible.md")
