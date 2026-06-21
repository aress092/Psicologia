import re
import json

def process_file(filename, valid_indices, new_questions, var_name):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    match = re.search(r'const\s+' + var_name + r'\s*=\s*(\[[\s\S]*?\]);', content)
    if not match: return
    array_str = match.group(1)
    objects = re.findall(r'(\{[^\}]+\})', array_str)
    kept_objects = [objects[i] for i in valid_indices]
    
    for q in new_questions:
        obj_str = f'{{ theme: "CI", question: "{q["question"]}", options: {json.dumps(q["options"], ensure_ascii=False)}, correct: {q["correct"]}, justification: "{q["justification"]}" }}'
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
    {"question": "Los críticos de la teoría evolutiva de Darwin señalaron que existe una discontinuidad crucial entre especies basada en...", "options": ["La capacidad de caminar sobre dos piernas", "La capacidad humana de pensar y razonar, que según ellos los animales no compartían", "La agresividad", "El instinto reproductivo"], "correct": 1, "justification": "Argumentaban que pensar y razonar era algo exclusivamente humano, oponiéndose a la continuidad evolutiva."},
    {"question": "Según la Ley del Efecto, los animales aprenden una asociación entre...", "options": ["El EC y el EI", "La respuesta y las consecuencias directamente", "La respuesta y los estímulos presentes (E-R)", "Dos conductas operantes"], "correct": 2, "justification": "Aprenden una asociación E-R, y las consecuencias satisfactorias sólo sirven para fortalecer dicha asociación E-R."},
    {"question": "Para Skinner, los procesos mentales (como emociones o pensamientos)...", "options": ["No existen y deben ser ignorados", "Son el origen del libre albedrío", "Son en realidad conductas encubiertas que ocurren como consecuencias de reforzamientos", "Causan las conductas abiertas"], "correct": 2, "justification": "Skinner consideró que los sucesos mentales son conductas encubiertas sujetas a las mismas leyes de aprendizaje que las conductas abiertas."},
    {"question": "La metáfora de la caja negra en el conductismo sugiere que...", "options": ["El cerebro es oscuro y misterioso", "Para entender las leyes que rigen la conducta no es preciso abrir la caja y ver qué ocurre dentro", "Los animales perciben el mundo en blanco y negro", "El aprendizaje requiere falta de luz"], "correct": 1, "justification": "La caja es opaca; las leyes de la conducta se deducen relacionando el ambiente (inputs) con el comportamiento (outputs)."},
    {"question": "En los procedimientos de ensayos discretos, como el laberinto, dos medidas importantes son...", "options": ["Tasa de respuesta y resistencia a extinción", "Latencia y Velocidad de carrera", "Razón de supresión y Condicionamiento de huella", "Número de respuestas por minuto"], "correct": 1, "justification": "El ensayo termina al llegar a la meta, por lo que se mide cuánto tarda en empezar (latencia) y en recorrerlo (velocidad)."},
    {"question": "Para mantener habilidades adquiridas en el tiempo de forma duradera, es más útil un programa de...", "options": ["Reforzamiento continuo", "Extinción", "Castigo intermitente", "Reforzamiento intermitente o parcial"], "correct": 3, "justification": "El continuo es mejor para adquirir la conducta, y el intermitente para mantenerla."},
    {"question": "Un programa de Reforzamiento Diferencial de Tasas Bajas (RDB) exige que el sujeto...", "options": ["Responda lo más rápido posible", "Refrene su respuesta hasta que haya pasado un cierto período de tiempo desde la anterior", "No responda nunca", "Responda a cualquier estímulo"], "correct": 1, "justification": "Se refuerzan los Tiempos Entre Respuestas (TER) largos."},
    {"question": "En los programas concurrentes encadenados, a diferencia de los concurrentes simples...", "options": ["El organismo debe elegir de antemano con cuál de los operantes va a trabajar, y el no elegido queda inactivo", "El organismo puede alternar libremente todo el tiempo", "Se aplica solo castigo", "No hay fase de elección"], "correct": 0, "justification": "Se escoge primero la rama y luego se trabaja en ella, simulando elecciones con compromiso."},
    {"question": "El contraste conductual negativo ocurre cuando...", "options": ["Una recompensa favorable es seguida por una desfavorable, provocando una caída drástica en la respuesta", "Una descarga es eliminada", "Dos recompensas son iguales", "Aumenta la tasa de respuesta"], "correct": 0, "justification": "La experiencia previa con el buen refuerzo hace que el nuevo (peor) parezca aún menos valioso."},
    {"question": "El 'procedimiento de marcado' en condicionamiento instrumental sirve para...", "options": ["Castigar al sujeto físicamente", "Indicar inmediatamente la respuesta correcta a reforzar cuando la entrega del reforzador se demora", "Marcar el territorio de la rata", "Extinguir una conducta de evitación"], "correct": 1, "justification": "Ayuda a salvar el problema de la demora, conectando la respuesta específica con el reforzador que llegará más tarde."}
]

new_v3 = [
    {"question": "La hipótesis de la inminencia depredadora asume que...", "options": ["Los depredadores aprenden por ensayo y error", "El animal elige la respuesta defensiva midiendo los diferentes niveles del daño percibido", "La huida siempre es la mejor opción", "No existen respuestas incondicionadas"], "correct": 1, "justification": "Las respuestas de defensa cambian dependiendo de qué tan inminente perciba el organismo la amenaza."},
    {"question": "Para que un castigo sea eficaz, respecto a su familiaridad...", "options": ["Debe ser novedoso, pues los familiares generan habituación", "Debe ser muy familiar para que el sujeto lo reconozca", "Debe incrementarse su intensidad de menos a más", "Da igual su nivel de familiaridad"], "correct": 0, "justification": "El castigo debe ser intenso desde el principio y estímulos aversivos novedosos funcionan mejor que los ya conocidos."},
    {"question": "Uno de los efectos secundarios emocionales del castigo, especialmente si es intenso, es...", "options": ["El aumento de la inteligencia", "Provocar llanto y miedo generalizado", "Generar alegría encubierta", "El aprendizaje por imitación positivo"], "correct": 1, "justification": "El castigo intenso causa efectos emocionales adversos que pueden interferir en el aprendizaje general."},
    {"question": "El famoso experimento de Albert Bandura con el muñeco Bobo demostró...", "options": ["El aprendizaje clásico del miedo", "Que los niños imitaban la agresividad física al observar a un adulto golpeando al muñeco", "Que el castigo es ineficaz", "El moldeamiento en palomas"], "correct": 1, "justification": "Fundamentó la teoría del aprendizaje por observación (o vicario) de conductas agresivas."},
    {"question": "¿Qué hallazgo biológico (Giacomo Rizzolatti) proporciona una base neural para el aprendizaje por imitación?", "options": ["El hipocampo", "La amígdala extendida", "Las neuronas espejo", "Los neurotransmisores de dopamina"], "correct": 2, "justification": "Las neuronas espejo se activan tanto al ejecutar la acción como al ver a otro ejecutarla."},
    {"question": "Para extinguir la conducta de evitación patológica en clínica, se suele usar la técnica de...", "options": ["Inundación o Prevención de la Respuesta (impedirle emitir la respuesta ante el EC)", "Moldeamiento", "Autocontrol", "Castigo positivo intenso"], "correct": 0, "justification": "Al forzar al sujeto a exponerse al EC sin dejarle escapar, descubre que el EI aversivo ya no ocurre, extinguiendo el miedo."},
    {"question": "La teoría de los dos procesos destaca la dependencia mutua entre...", "options": ["Castigo y Extinción", "Condicionamiento Clásico (miedo) y Condicionamiento Instrumental (escape)", "Razón Fija y Razón Variable", "Fobias y Ansiedad"], "correct": 1, "justification": "Sin el miedo condicionado previamente (CC), no existiría el refuerzo negativo de escapar de él (CI)."},
    {"question": "El paradigma de 'escape del miedo' (Brown y Jacobs) demostró empíricamente que...", "options": ["Los animales no sienten miedo condicionado", "Terminar un estímulo aversivo condicionado funciona como un reforzador eficaz de la conducta instrumental", "Solo el dolor físico puede reforzar la conducta", "La extinción es imposible"], "correct": 1, "justification": "Entrenaron primero el miedo a un tono, y luego probaron que las ratas aprendían a saltar la barrera solo para apagar el tono."},
    {"question": "Sobre la consistencia del castigo, es cierto que...", "options": ["El castigo parcial (aleatorio) funciona mejor", "El castigo continuo funciona mucho mejor que el castigo parcial", "Solo funciona si se aplica un día sí y otro no", "La consistencia no importa"], "correct": 1, "justification": "Para eliminar la conducta de forma eficaz, el castigo debe aplicarse cada vez que ocurra la respuesta, sin excepciones."},
    {"question": "El 'diseño triádico' de Seligman sirvió específicamente para...", "options": ["Curar fobias", "Aislar los efectos de la incontrolabilidad frente a los efectos producidos simplemente por el choque aversivo", "Ver si tres ratas cooperaban", "Demostrar que el castigo daña emocionalmente"], "correct": 1, "justification": "Comparó un grupo con escape, otro sin escape (acoplado) y otro sin choque, demostrando que lo dañino es la falta de control."}
]

valid_v2 = [0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 17, 18, 19, 21, 23, 24, 25, 26, 29]
valid_v3 = [0, 1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 15, 16, 17, 18, 19, 20, 22, 25, 27]

process_file('/home/ares/Psicologia/CME/.preguntas/q_t2_v2.js', valid_v2, new_v2, 'qT2_v2')
process_file('/home/ares/Psicologia/CME/.preguntas/q_t2_v3.js', valid_v3, new_v3, 'qT2_v3')
