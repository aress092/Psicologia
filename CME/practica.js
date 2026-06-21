document.addEventListener('DOMContentLoaded', () => {
  const apiKeyPanel = document.getElementById('apiKeyPanel');
  const apiKeyInput = document.getElementById('apiKey');
  const saveKeyBtn = document.getElementById('saveKeyBtn');
  const clearKeyBtn = document.getElementById('clearKeyBtn');
  
  const captchaAnswer = document.getElementById('captchaAnswer');
  const revealKeyBtn = document.getElementById('revealKeyBtn');
  const revealedKey = document.getElementById('revealedKey');
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
  
  // 0. Captcha Logic to reveal the API key safely
  revealKeyBtn.addEventListener('click', () => {
    if (parseInt(captchaAnswer.value) === 12) {
      // Obfuscate the key slightly in code so simple bots don't grab it easily
      const part1 = "AQ.Ab8RN6";
      const part2 = "JvzineGfBNs-ygj";
      const part3 = "otpP-EVHPS_lNAg3EytDebyS2ARbg";
      revealedKey.textContent = part1 + part2 + part3;
      revealedKey.classList.remove('hidden');
    } else {
      alert('Respuesta incorrecta. Pista: suma los dos números.');
    }
  });

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
  

  clearKeyBtn.addEventListener('click', () => {
    localStorage.removeItem('gemini_api_key');
    apiKeyInput.value = '';
    apiKeyPanel.classList.remove('hidden');
    alert('La clave ha sido borrada de tu navegador de forma segura.');
  });
  

  // 2. Initialize with Predefined Questions
  questions = typeof preguntas_desarrollo !== 'undefined' ? preguntas_desarrollo : [];
  if (questions.length > 0) {
    currentIndex = 0;
    showQuestion();
    practicePanel.classList.remove('hidden');
    resultPanel.classList.add('hidden');
  } else {
    questionText.textContent = "No se han encontrado preguntas.";
  }

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
NO pidas que la respuesta sea exacta palabra por palabra. El alumno puede estar redactando la teoría formal O bien puede estar proponiendo ejemplos prácticos suyos para demostrar que entiende el concepto.
Evalúa si el alumno ha entendido el concepto principal y si sus ejemplos (si los ha puesto) son válidos y van acordes a la teoría.

PREGUNTA: ${q.pregunta || q.question}
RESPUESTA IDEAL/REFERENCIA: ${idealAnswer}

RESPUESTA DEL ALUMNO: ${answer}

Instrucciones:
1. Dile si va por buen camino o si ha fallado.
2. Si el alumno aporta un ejemplo, evalúa rigurosamente si es correcto y explícale por qué ilustra (o no) la teoría.
3. Señala qué conceptos clave ha acertado y qué información teórica importante le ha faltado mencionar para tener la respuesta perfecta.
4. Dale una nota orientativa sobre 10 al final.
Mantén un tono animado, constructivo y pedagógico. Usa formato Markdown.
`;

    checkBtn.disabled = true;
    loader.classList.remove('hidden');
    resultPanel.classList.add('hidden');

    try {
      const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=${key}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          contents: [{ parts: [{ text: prompt }] }]
        })
      });

      if (!response.ok) {
        const errData = await response.json().catch(() => ({}));
        const errMsg = errData.error && errData.error.message ? errData.error.message : response.statusText;
        throw new Error(`Error en la API (${response.status}): ` + errMsg);
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
