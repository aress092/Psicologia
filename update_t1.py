import re
import json

def process_file(filename, valid_indices, new_questions, var_name):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'const\s+' + var_name + r'\s*=\s*(\[[\s\S]*?\]);', content)
    if not match:
        print("Could not find array in", filename)
        return
    
    array_str = match.group(1)
    objects = re.findall(r'(\{[^\}]+\})', array_str)
    kept_objects = [objects[i] for i in valid_indices]
    
    for q in new_questions:
        obj_str = f'{{ theme: "CC", question: "{q["question"]}", options: {json.dumps(q["options"], ensure_ascii=False)}, correct: {q["correct"]}, justification: "{q["justification"]}" }}'
        kept_objects.append(obj_str)
        
    final_objects = []
    for i, obj in enumerate(kept_objects):
        obj = re.sub(r'question:\s*"\d+\.\s*', f'question: "{i+1}. ', obj)
        final_objects.append("  " + obj)
        
    final_js = f"const {var_name} = [\n" + ",\n".join(final_objects) + "\n];\n"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_js)
    print("Updated", filename)

new_v2 = [
    {"question": "Según el modelo de CC, el aprendizaje es un proceso...", "options": ["innato", "de adquisición de nueva información a través de la experiencia", "que solo ocurre en humanos", "pasivo y sin memoria"], "correct": 1, "justification": "El aprendizaje se define como el proceso de adquisición de nueva información o comportamientos a través de la experiencia."},
    {"question": "En el CC, asociamos estímulos que...", "options": ["controlamos totalmente", "no controlamos y respondemos de forma automática", "dependen de nuestras consecuencias", "operan en el ambiente"], "correct": 1, "justification": "En el CC asociamos estímulos que no controlamos (EI) y respondemos automáticamente (RI/RC)."},
    {"question": "Para producir CC, el EC debe ser emparejado con...", "options": ["otro EC", "un Estímulo Incondicionado (EI)", "una Respuesta Condicionada", "un castigo positivo"], "correct": 1, "justification": "El procedimiento básico implica emparejar un estímulo neutro (EC) con un estímulo incondicionado (EI)."},
    {"question": "En el experimento de Pavlov, las 'secreciones psíquicas' eran...", "options": ["una molestia inicial que llevó al descubrimiento del CC", "una enfermedad gástrica", "el Estímulo Incondicionado", "una conducta operante"], "correct": 0, "justification": "Pavlov inicialmente las vio como algo que molestaba, hasta que comprendió su importancia y descubrió el CC."},
    {"question": "El término 'irrelevancia aprendida' se refiere al retraso en el aprendizaje debido a...", "options": ["experiencia previa con el EC solo", "experiencia previa con contingencia nula P(EI|EC) = P(EI|noEC)", "experiencia previa con el EI solo", "falta de atención"], "correct": 1, "justification": "Ocurre cuando el organismo aprende que el EC no aporta información relevante sobre el EI."},
    {"question": "¿Qué ocurre si el intervalo entre el EC y el EI aumenta excesivamente?", "options": ["Aumenta la fuerza de la RC", "Pierde efectividad el condicionamiento", "Se produce inhibición latente", "Se condiciona más rápido"], "correct": 1, "justification": "La demora corta es lo más efectivo; a mayor intervalo, se pierde efectividad porque el EC deja de anticipar el EI."},
    {"question": "La hipótesis de la codificación temporal sugiere que el animal aprende que el EC y el EI van juntos, pero no presenta RC a menos que...", "options": ["el EC sea informativo y sirva para predecir el EI", "el EI sea muy doloroso", "se presenten de forma aleatoria", "el EC se devalúe"], "correct": 0, "justification": "En el condicionamiento simultáneo se aprende la relación, pero no hay ejecución (RC) porque el EC no anticipa ni predice."},
    {"question": "¿Cuál es un ejemplo claro de generalización?", "options": ["Dejar de salivar ante la campana", "Un niño que teme a un coche en marcha y también muestra miedo a camiones o motos", "Aprender que la luz verde significa comida y la roja no", "El olvido con el paso del tiempo"], "correct": 1, "justification": "Extender la respuesta aprendida a estímulos similares de la misma categoría."},
    {"question": "Para demostrar que hay condicionamiento clásico, el grupo experimental debe...", "options": ["dar menos RC que el grupo de control", "dar más RC en el ensayo de prueba que el grupo control", "no presentar RI", "extinguirse más rápido"], "correct": 1, "justification": "El grupo experimental se compara en la fase de prueba con el control (ej. desemparejado) y debe mostrar mayor magnitud de RC."},
    {"question": "Si una rata picotea una luz que predice comida de forma innecesaria, se llama...", "options": ["Bloqueo", "Sombreado", "Automoldeamiento o seguimiento del signo", "Supresión condicionada"], "correct": 2, "justification": "Es la aparición de respuestas de contacto con el EC (luz) aunque no sean necesarias para recibir el EI."},
    {"question": "En la aversión al sabor, el intervalo entre el EC y el EI puede ser...", "options": ["solo de segundos", "de varias horas", "simultáneo obligatoriamente", "hacia atrás"], "correct": 1, "justification": "Por su utilidad biológica, la aversión gustativa tolera intervalos muy largos entre el sabor y el malestar gástrico."},
    {"question": "En el experimento de devaluación del EI, si tras condicionar el EC al EI, devaluamos el EI...", "options": ["la respuesta al EC aumenta", "la respuesta al EC se reduce", "la asociación desaparece permanentemente", "el EC se vuelve inhibidor"], "correct": 1, "justification": "La RC se reduce, lo que apoya la hipótesis E-EI: el EC activa una representación del EI devaluado."}
]

new_v3 = [
    {"question": "En el condicionamiento de orden superior, el condicionamiento de tercer orden es...", "options": ["Imposible", "Difícil de establecer", "Igual de fuerte que el de primer orden", "El más habitual"], "correct": 1, "justification": "El de tercer orden es muy difícil, y el de cuarto orden se considera imposible."},
    {"question": "Un niño desarrolla miedo a las alturas porque sus padres le gritan al subir a una escalera. Esto es ejemplo de...", "options": ["Precondicionamiento sensorial", "Condicionamiento de segundo orden", "Sombreado", "Extinción"], "correct": 1, "justification": "Los gritos (EI) se asocian al peligro, y luego las alturas (EC2) se asocian a los gritos (EC1)."},
    {"question": "En el precondicionamiento sensorial, la fase 1 consiste en...", "options": ["Asociar un EC con un EI", "Asociar dos estímulos neutros (EC1 y EC2) juntos", "Presentar el EI solo", "Devaluar el EI"], "correct": 1, "justification": "Se asocian dos neutros; luego uno se asocia al EI, y el otro adquiere capacidad de provocar la RC por la asociación previa."},
    {"question": "¿Cuál es la principal diferencia entre sombreado y bloqueo?", "options": ["El sombreado depende de la intensidad relativa y el bloqueo de una experiencia previa con un elemento", "Son exactamente lo mismo", "El sombreado usa inhibición y el bloqueo no", "El bloqueo es operante"], "correct": 0, "justification": "Sombreado = estímulo más saliente interfiere. Bloqueo = estímulo condicionado previamente interfiere con el nuevo."},
    {"question": "Para que ocurra el condicionamiento inhibitorio, la ausencia del EI debe ser...", "options": ["Totalmente aleatoria", "Significativa (debe haber un contexto excitatorio que genere expectativa del EI)", "Muy prolongada", "Precedida por un castigo"], "correct": 1, "justification": "La ausencia de un evento solo se puede aprender si el evento era esperado en ese contexto."},
    {"question": "Una contingencia negativa entre EC y EI se da cuando...", "options": ["P(EI|EC) > P(EI|noEC)", "P(EI|EC) < P(EI|noEC)", "Ambas son iguales", "P(EI|EC) = 1"], "correct": 1, "justification": "La fórmula Cont = p(EI|EC) - p(EI|noEC) da un resultado negativo, lo que vuelve al EC inhibitorio."},
    {"question": "En el procedimiento de inhibición diferencial se alternan...", "options": ["Ensayos EC+ con el EI, y ensayos EC- sin el EI", "Ensayos hacia atrás", "Ensayos simultáneos y de huella", "Extinciones y recuperaciones"], "correct": 0, "justification": "Se presentan ensayos excitatorios e inhibitorios separados; el sujeto aprende a discriminar."},
    {"question": "Para medir el condicionamiento inhibitorio se pueden usar sistemas de respuesta...", "options": ["Solo motores", "Bidireccionales (ej. acercarse vs alejarse, frecuencia cardiaca)", "Unidireccionales exclusivamente", "Aleatorios"], "correct": 1, "justification": "Las respuestas bidireccionales permiten ver caídas por debajo de la línea base fisiológica o conductual."},
    {"question": "En la prueba del retraso de adquisición para inhibidores...", "options": ["Se presenta el EC- junto con un excitador", "Se intenta condicionar excitatoriamente el presunto EC-", "Se extingue el EC-", "Se devalúa el EI"], "correct": 1, "justification": "Si era un buen inhibidor, aprenderá más lentamente a ser excitador que un estímulo completamente neutro."},
    {"question": "En el experimento de prueba de sumación de Cole et al., si X es un inhibidor, el compuesto AX generará...", "options": ["Más respuesta que A sola", "Menos respuesta que A sola", "Cero respuesta siempre", "Sobreexpectativa"], "correct": 1, "justification": "El inhibidor X tiene la capacidad de restar o reducir la respuesta excitatoria generada por A."},
    {"question": "¿Qué ocurre con la Razón de Supresión si su valor es de 1?", "options": ["Condicionamiento perfecto de miedo", "Condicionamiento inhibitorio (aumento de respuestas operantes)", "Falta de atención", "Extinción completa"], "correct": 1, "justification": "Un valor de 1 indica que hay más respuestas durante el EC; actúa como señal de seguridad (inhibición)."},
    {"question": "El condicionamiento hacia atrás se caracteriza por presentar...", "options": ["El EC antes del EI", "El EI seguido del EC", "Ambos a la vez", "Solo el EI"], "correct": 1, "justification": "Es muy poco eficaz excitatoriamente y el EC suele convertirse en una señal de seguridad de que el EI ya pasó."},
    {"question": "La extinción es el proceso por el cual...", "options": ["El sujeto olvida la asociación por el paso del tiempo", "El EC se presenta repetidamente sin el EI, perdiendo gradualmente su capacidad de evocar la RC", "Se castiga al sujeto", "Se suprime la conducta con fármacos"], "correct": 1, "justification": "Es un reaprendizaje activo mediante la exposición repetida al EC solo, no un simple olvido."},
    {"question": "El control aleatorio sirve para evitar confundir el condicionamiento con...", "options": ["Extinción", "Condicionamiento fortuito", "Sombreado", "Inhibición"], "correct": 1, "justification": "Controla la posibilidad de que se formen asociaciones accidentales o cambios por mera exposición a los estímulos."},
    {"question": "En la teoría E-R frente a E-EI, el experimento de la devaluación apoya que...", "options": ["Respondemos como un reflejo ciego", "Respondemos al EC porque activa una representación o memoria del EI", "El EC es idéntico al EI", "No hay asociación"], "correct": 1, "justification": "Al devaluar el EI y observar caída de la RC, se concluye que el animal evalúa el estado actual del EI evocado por el EC."}
]

valid_v2 = [0, 1, 2, 3, 4, 5, 6, 9, 10, 18, 21, 22, 23, 24, 25, 26, 27, 29]
valid_v3 = [0, 3, 6, 10, 11, 13, 14, 16, 20, 21, 23, 24, 25, 26, 27]

process_file('/home/ares/Psicologia/CME/.preguntas/q_t1_v2.js', valid_v2, new_v2, 'qT1_v2')
process_file('/home/ares/Psicologia/CME/.preguntas/q_t1_v3.js', valid_v3, new_v3, 'qT1_v3')
