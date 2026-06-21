document.addEventListener('DOMContentLoaded', () => {
  const apiKeyPanel = document.getElementById('apiKeyPanel');
  const apiKeyInput = document.getElementById('apiKey');
  const saveKeyBtn = document.getElementById('saveKeyBtn');
  
  const fileInput = document.getElementById('fileInput');
  
  const practicePanel = document.getElementById('practicePanel');
  const questionCounter = document.getElementById('questionCounter');
  const questionText = document.getElementById('questionText');
  const userAnswer = document.getElementById('userAnswer');
  
  const prevBtn = document.getElementById('prevBtn');
  const nextBtn = document.getElementById('nextBtn');
  const checkBtn = document.getElementById('checkBtn');
  const loader = document.getElementById('loader');
  
  const resultPanel = document.getElementById('resultPanel');
  const resultContent = document.getElementById('resultContent');

  let questions = [];
  let currentIndex = 0;
  
  // 1. Manage API Key
  const storedKey = localStorage.getItem('gemini_api_key');
  if (storedKey) {
    apiKeyInput.value = storedKey;
    apiKeyPanel.classList.add('hidden'); // Hide if already exists
  }

  saveKeyBtn.addEventListener('click', () => {
    const key = apiKeyInput.value.trim();
    if (key) {
      localStorage.setItem('gemini_api_key', key);
      alert('Clave guardada correctamente en tu navegador.');
      apiKeyPanel.classList.add('hidden');
    } else {
      alert('Por favor, introduce una clave válida.');
    }
  });

  // 2. Handle File Upload
  fileInput.addEventListener('change', (e) => {
    const file = e.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.onload = function(e) {
      try {
        let content = e.target.result;
        // Basic cleanup if it's a JS file instead of pure JSON
        if (file.name.endsWith('.js')) {
          // Attempt to extract the array if it starts with 'const name = ['
          const match = content.match(/\[\s*\{[\s\S]*\}\s*\]/);
          if (match) {
            content = match[0];
          }
        }
        
        // Convert JS object syntax to JSON if necessary (very basic regex)
        // Note: It is highly recommended that the user uploads pure JSON
        // but we try to parse it anyway.
        // A safer robust way is to just expect pure JSON.
        try {
            questions = JSON.parse(content);
        } catch(parseErr) {
            // Unsafe fallback for simple JS object arrays (eval is safe here ONLY because it's the user's own local file in their own browser)
            questions = eval('(' + content + ')');
        }

        if (!Array.isArray(questions) || questions.length === 0) {
          throw new Error('El archivo no contiene un array de preguntas válido.');
        }

        // Format check
        if (!questions[0].pregunta && !questions[0].question) {
           throw new Error('El formato debe ser [{"pregunta": "...", "respuesta_ideal": "..."}]');
        }

        currentIndex = 0;
        showQuestion();
        practicePanel.classList.remove('hidden');
        resultPanel.classList.add('hidden');
      } catch (error) {
        alert('Error al leer el archivo. Asegúrate de que el formato es correcto: ' + error.message);
        console.error(error);
      }
    };
    reader.readAsText(file);
  });

  // 3. UI Navigation
  function showQuestion() {
    if (questions.length === 0) return;
    
    const q = questions[currentIndex];
    questionText.textContent = q.pregunta || q.question;
    userAnswer.value = ''; // clear previous answer
    resultPanel.classList.add('hidden');
    
    questionCounter.textContent = `Pregunta ${currentIndex + 1} de ${questions.length}`;
    
    prevBtn.disabled = currentIndex === 0;
    nextBtn.disabled = currentIndex === questions.length - 1;
  }

  prevBtn.addEventListener('click', () => {
    if (currentIndex > 0) {
      currentIndex--;
      showQuestion();
    }
  });

  nextBtn.addEventListener('click', () => {
    if (currentIndex < questions.length - 1) {
      currentIndex++;
      showQuestion();
    }
  });

  // 4. API Call to Gemini
  checkBtn.addEventListener('click', async () => {
    const key = localStorage.getItem('gemini_api_key') || apiKeyInput.value.trim();
    if (!key) {
      alert('Necesitas configurar tu clave API de Gemini primero.');
      apiKeyPanel.classList.remove('hidden');
      return;
    }

    const answer = userAnswer.value.trim();
    if (!answer) {
      alert('Escribe una respuesta antes de corregir.');
      return;
    }

    const q = questions[currentIndex];
    const idealAnswer = q.respuesta_ideal || q.justification || q.options?.[q.correct] || "Respuesta no definida en el documento.";

    const prompt = `
Eres un profesor experto y amable de psicología. Tienes que corregir la respuesta de un alumno a una pregunta abierta de desarrollo.
NO pidas que la respuesta sea exacta palabra por palabra. Evalúa si el alumno ha entendido el concepto principal.

PREGUNTA: ${q.pregunta || q.question}
RESPUESTA IDEAL/REFERENCIA: ${idealAnswer}

RESPUESTA DEL ALUMNO: ${answer}

Instrucciones:
1. Dile si va por buen camino o si ha fallado.
2. Señala qué conceptos clave ha acertado.
3. Señala qué información importante le ha faltado mencionar (si falta alguna).
4. Dale una nota orientativa sobre 10 al final.
Mantén un tono animado y pedagógico. Usa formato Markdown.
`;

    checkBtn.disabled = true;
    loader.classList.remove('hidden');
    resultPanel.classList.add('hidden');

    try {
      const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${key}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }]
        })
      });

      if (!response.ok) {
        throw new Error('Error en la API: ' + response.statusText);
      }

      const data = await response.json();
      const aiText = data.candidates[0].content.parts[0].text;
      
      resultContent.innerHTML = formatMarkdown(aiText);
      resultPanel.classList.remove('hidden');
      
    } catch (error) {
      alert('Hubo un problema al contactar con la IA. Comprueba tu clave API y tu conexión. Detalle: ' + error.message);
    } finally {
      checkBtn.disabled = false;
      loader.classList.add('hidden');
    }
  });

  // Simple Markdown parser for basic formatting
  function formatMarkdown(text) {
    let formatted = text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n/g, '<br>');
    return formatted;
  }
});
