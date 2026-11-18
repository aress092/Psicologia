const fs = require('fs');
const path = require('path');

function loadFile(filepath) {
    let content = fs.readFileSync(filepath, 'utf8');
    // Eliminar 'const varName = '
    content = content.replace(/const \w+ = /, 'return ');
    // Eliminar posibles export o console.log al final
    try {
        return new Function(content)();
    } catch(e) {
        console.error("Error parsing", filepath, e);
        return [];
    }
}

const dir = '/home/ares/Psicologia/CME/.preguntas/';
const files = [
    'q_t1.js', 'q_t1_v2.js', 'q_t1_v3.js',
    'q_t2.js', 'q_t2_v2.js', 'q_t2_v3.js',
    'q_t3.js', 'q_t3_v2.js', 'q_t3_v3.js',
    'q_t4.js', 'q_t4_v2.js', 'q_t4_v3.js'
];

let allQs = [];
files.forEach(f => {
    let p = path.join(dir, f);
    if(fs.existsSync(p)) {
        allQs = allQs.concat(loadFile(p));
    }
});

function shuffle(array) {
    let curId = array.length;
    while (0 !== curId) {
        let randId = Math.floor(Math.random() * curId);
        curId -= 1;
        let tmp = array[curId];
        array[curId] = array[randId];
        array[randId] = tmp;
    }
    return array;
}

let testQs = shuffle(allQs).slice(0, 30);

let md = "# Simulacro Examen CME (Sin Respuestas)\n\n";
md += "> Un test aleatorio de 30 preguntas mezcladas de todos los temas. ¡Anota tus opciones en un papel!\n\n---\n\n";

testQs.forEach((q, i) => {
    let cleanQ = q.question.replace(/^\d+\.\s*/, '');
    md += `### ${i+1}. ${cleanQ}\n\n`;
    q.options.forEach((opt, idx) => {
        let letter = String.fromCharCode(65 + idx); // A, B, C, D
        md += `- [ ] **${letter})** ${opt}\n`;
    });
    md += `\n`;
});

// Guardarlo como un archivo markdown local
fs.writeFileSync('/home/ares/Psicologia/CME/Simulacro_CME_Imprimible.md', md);
console.log("Generado Simulacro_CME_Imprimible.md");

// Opcional: Generar TODO el banco de preguntas sin respuestas
let mdAll = "# Todo el Banco de Preguntas CME (Sin Respuestas)\n\n";
mdAll += `> Total de preguntas: ${allQs.length}\n\n---\n\n`;
allQs.forEach((q, i) => {
    let cleanQ = q.question.replace(/^\d+\.\s*/, '');
    mdAll += `### ${i+1}. [${q.theme}] ${cleanQ}\n\n`;
    q.options.forEach((opt, idx) => {
        let letter = String.fromCharCode(65 + idx); // A, B, C, D
        mdAll += `- [ ] **${letter})** ${opt}\n`;
    });
    mdAll += `\n`;
});
fs.writeFileSync('/home/ares/Psicologia/CME/Banco_CME_Completo_Imprimible.md', mdAll);
console.log("Generado Banco_CME_Completo_Imprimible.md");
