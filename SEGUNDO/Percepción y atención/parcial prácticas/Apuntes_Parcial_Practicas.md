# Apuntes Resumidos de Examen: Parcial de Prácticas (Percepción y Atención)

---

## BLOQUE I: PSICOFÍSICA CLÁSICA Y NUEVA PSICOFÍSICA (Tudela + Práctica 1)

### 1. Sensación, Percepción y Psicofísica
* **Sensación**: experiencia básica inmediata provocada por estímulos aislados (tiene **modalidad**, pero **no significado**). Operacionalmente: respuesta (verbal/manual) ante la manipulación de una dimensión estimular.
* **Percepción**: integración, transformación y organización de las sensaciones para reconocer objetos/escenas y actuar adecuadamente. **No hay correspondencia directa** entre el estímulo físico y la sensación subjetiva.
* **Fechner (1860, *Elementos de Psicofísica*)**: funda la psicofísica para relacionar cuantitativamente la **dimensión física (estímulo, $E$)** y la **dimensión psíquica (sensación, $S$)** sin recurrir a la fisiología (distingue **nivel de tarea** vs. **nivel de proceso**: detección y discriminación). Defendía el **paralelismo psicofísico** (*panpsiquismo*: mente y materia son dos caras de una misma realidad).

### 2. Conceptos Fundamentales y Tareas
Fechner buscaba una **escala de razón** para la sensación, necesitando un **punto cero ($S_0$)** y una **unidad de medida ($DMP$)**:

| Concepto | Dimensión | Definición y función |
| :--- | :--- | :--- |
| **Umbral Absoluto ($UA$ / $E_0$)** | Física | Mínima estimulación detectada (por debajo no se detecta, por encima sí). Define un **punto** que mide indirectamente el **punto cero ($S_0$)** de la sensación. |
| **Umbral Diferencial ($UD$ / $\Delta E$)** | Física | Mínimo cambio físico capaz de producir un cambio en la sensación. Define un **intervalo** físico (crece al aumentar el estímulo). |
| **Diferencia Mínima Perceptible ($DMP$)** | Psíquica | Cambio mínimo discriminable en la sensación, medido indirectamente a través del $UD$. Define un **intervalo** subjetivo asumido constante. |

* **Tareas de Detección** (para **$UA$**): 1 único estímulo; respuesta dicotómica (**SÍ/NO**). Incluye **ensayos trampa (*catch trials*)** sin estímulo para evitar aciertos por rutina.
* **Tareas de Discriminación** (para **$UD$**): $\ge 2$ estímulos. Se compara un **Estímulo Estándar ($EE$, fijo)** con un **Estímulo de Prueba ($EP$, variable)** respondiendo **MAYOR (`+`), IGUAL (`=`) o MENOR (`-`)**. Si se presentan a la vez y se responde *IGUAL/DIFERENTE*, es una **tarea de igualación (*matching task*)**.
* **Parámetros**: en psicofísica clásica solo se mide la **precisión** (aciertos/errores), no la velocidad (**Tiempo de Reacción, TR**).

### 3. Métodos Psicofísicos Clásicos (Indirectos)
Se diferencian por cómo presentan los estímulos:

1. **Método de Ajustes**: el sujeto o experimentador ajusta la intensidad de forma **lenta y continua** hasta detectar ($UA$) o igualar/notar diferencia ($UD$). **El más rápido**, menos preciso.
2. **Método de los Límites**: series ordenadas **ascendentes ($A$)** y **descendentes ($D$)** alternadas (con distinto inicio para evitar rutinas). La serie **termina al cambiar la respuesta** (en $UD$, al aparecer la respuesta opuesta a la inicial).
   * **Cálculo de $UA$**: punto medio del cambio en cada serie $\to$ media de series $A$ ($UA$), media de series $D$ ($UD$) $\to$ media global ($UA_{\text{global}}$).
   * **Sesgos (diagnóstico con $UD - UA$)**:
     * **Habituación** (*repetir la respuesta previa más allá del cambio*): umbral más bajo en $D$ y más alto en $A \implies \mathbf{UD - UA < 0}$ (**negativa**).
     * **Anticipación** (*adelantar el cambio antes de tiempo*): umbral más alto en $D$ y más bajo en $A \implies \mathbf{UD - UA > 0}$ (**positiva**).
     * **Sin sesgo**: $\mathbf{UD - UA = 0}$.
   * **Cálculo de $UD$** (hay 2 transiciones por serie):
     * **$US$ (Umbral Superior)**: punto medio entre MAYOR (`+`) e IGUAL (`=`).
     * **$UI$ (Umbral Inferior)**: punto medio entre IGUAL (`=`) y MENOR (`-`).
     * **Intervalo de Incertidumbre**: $\mathbf{II = US - UI}$ (abarca 2 discriminaciones).
     * **Umbral Diferencial**: $\mathbf{UD = \frac{II}{2} = \frac{US - UI}{2}}$.
     * **Punto de Igualdad Subjetiva**: $\mathbf{PIS = \frac{US + UI}{2} = UI + UD = US - UD}$.
     * **Error Constante**: $\mathbf{EC = PIS - EE}$ ($EC > 0 \implies$ sobreestima el $EE$; $EC < 0 \implies$ subestima el $EE$).
3. **Método de los Estímulos Constantes**: estímulos en **ORDEN ALEATORIO** repetidos muchas veces. **El más preciso y robusto; elimina habituación y anticipación**, pero requiere **mucho tiempo**. En discriminación ($+$ / $-$): **$US = 75\%$** «Mayor», **$PIS = 50\%$**, **$UI = 25\%$** ($II = US - UI$; $UD = II/2$).

### 4. Leyes Psicofísicas y Nueva Psicofísica (Stevens)
* **Ley de Weber**: el $UD$ es una fracción constante del $EE$:
  $$\frac{UD}{EE} = c \quad \Longleftrightarrow \quad \frac{\Delta EE}{EE} = c \quad \Longleftrightarrow \quad UD = c \cdot EE$$
  *(Válida en intensidades **intermedias**; falla en valores **extremos**).*
* **Ley de Fechner**: deducida por inducción desde $E_0$ ($E_i = E_0(1+c)^r$, crecimiento exponencial del estímulo para incrementos constantes de $1\text{ DMP}$). Despejando $r$:
  $$r = k \cdot \log\left(\frac{E_i}{E_0}\right), \quad k = \frac{1}{\log(1+c)}$$
  Es una **función logarítmica** (los incrementos de sensación son cada vez menores).
* **Nueva Psicofísica (S. S. Stevens)**: usa **métodos directos** (juicios cuantitativos directos sobre la sensación):
  * **Estimación de Magnitud**: se da un estímulo con un valor numérico (**módulo**, ej. $50$) y el sujeto asigna números a otros manteniendo la razón (doble $= 100$, mitad $= 25$).
  * **Producción de Magnitud**: el experimentador da un número y el sujeto ajusta un estímulo continuo hasta igualar esa sensación.
  * **Ley Potencial de Stevens**:
    $$S = c \cdot E^k \quad \Longleftrightarrow \quad \log S = \log c + k \cdot \log E$$
    En coordenadas logarítmicas es una recta de pendiente $k$: **$k=1$** lineal; **$k>1$** positivamente acelerada; **$k<1$** negativamente acelerada.
* **¿Fechner o Stevens? Tipo de continuo**:
  * **Continuos Protéticos** (varía la **cantidad/intensidad**, ej. sonoridad, brillo): cada $DMP$ añade más sensación $\implies$ se cumple **Stevens** (falla Fechner).
  * **Continuos Metatéticos** (varía la **cualidad**, ej. tono auditivo/frecuencia): se cumple **Fechner**.

---

## BLOQUE II: TEORÍA DE DETECCIÓN DE SEÑALES — TDS (Tudela + Diapos + Excel)

### 1. Ruptura con la Psicofísica Clásica y Procesos Independientes
* **Origen (1953–1954, Tanner y Swets)**: investigación de radares en la II Guerra Mundial.
* **Modelo Pasivo (clásico)** ($\text{Estímulo} \to \text{Sensación} \to \text{Respuesta}$, umbral fijo) vs. **Modelo Activo (TDS)** ($\text{Estímulo} \to \text{Sensación} \to \textbf{Observador} \to \text{Respuesta}$): **prescinde del umbral** y trata la detección como una **toma de decisiones bajo incertidumbre**.
* **Dos procesos independientes**:
  1. **Procesos Sensoriales ($d'$)**: sensibilidad/discriminabilidad. Afectada por **intensidad de la señal**, relación señal/ruido, dificultad y **pericia** (ej. radiólogos expertos, músicos). *No afecta a $\beta$.*
  2. **Proceso de Decisión ($\beta$)**: criterio de respuesta. Afectado por **probabilidades *a priori***, **incentivos/consecuencias**, motivación, personalidad y **aquiescencia** (decir SÍ sin razonar). *No afecta a $d'$.*

### 2. Matriz de Confusión ($2 \times 2$, 2 grados de libertad)
Intensidad de la señal constante; respuesta binaria (**SÍ / NO**):

| Estado real | Respuesta **SÍ** | Respuesta **NO** | Suma |
| :--- | :---: | :---: | :---: |
| **SEÑAL ($SR$)** | **ACIERTO ($A$):** $TA = p = \frac{\text{Aciertos}}{\text{Ensayos } SR}$ | **FALLO ($F$):** $TF = 1 - TA$ | $1$ |
| **RUIDO ($R$)** | **FALSA ALARMA ($FA$):** $TFA = q = \frac{\text{Falsas Alarmas}}{\text{Ensayos } R}$ | **RECHAZO CORRECTO ($RC$):** $TRC = 1 - TFA$ | $1$ |

*(Paralelismo estadístico: $FA =$ Error Tipo I $\alpha$; $F =$ Error Tipo II $\beta$; $A =$ Potencia $1-\beta$).*

### 3. Supuestos, $d'$, $\beta$ y Fórmulas
* **Supuestos sensoriales**: los sentidos están **siempre activos**, generando dos curvas normales: **Ruido ($R$)** y **Señal ($SR$, desplazada a la derecha)**.
* **Razón de verosimilitud ($p/q = Y(S)/Y(R)$)**: cociente entre la ordenada de $SR$ y la de $R$ en un nivel de sensación ($=1$ en el punto de cruce; $<1$ a la izq.; $>1$ a la dcha.).
* **Discriminabilidad ($d'$)**: distancia en puntuaciones $z$ entre las medias de $R$ y $SR$:
  $$d' = z_{\text{cola dcha.}}(FA) - z_{\text{cola dcha.}}(A) = z_{\text{acum.}}(A) - z_{\text{acum.}}(FA)$$
  * $d' = 0$: solapamiento total (nula discriminación). $d' > 1\text{–}2$: buena discriminación (máx. $\approx 6$). Si $TA > TFA \implies d' > 0$.
* **Criterio ($\beta$)**: razón de verosimilitud en el punto de corte ($\beta = p[z(A)] / q[z(FA)] = Y(S)/Y(R)$):
  * **$\beta = 1$ (Neutral)**: en el punto de cruce, sin sesgo.
  * **$\beta > 1$ (Estricto)**: desplazado a la derecha; ante la duda dice **«NO»** $\implies$ **menos Aciertos y menos FA**.
  * **$\beta < 1$ (Laxo)**: desplazado a la izquierda; arriesga y dice **«SÍ»** $\implies$ **más Aciertos y más FA**.

### 4. Casos Prácticos Clave
* **Cuadro 3 (Tudela)**: $150\ SR$ ($90$ Aciertos $\to TA=0,60$), $150\ R$ ($30$ FA $\to TFA=0,20$). $z(FA)=0,842, q=0,280$; $z(A)=-0,253, p=0,386 \implies \mathbf{d'=1,095}$ y $\mathbf{\beta = 0,386/0,280 = 1,38}$ (criterio estricto).
* **Dos Radiólogos (Diapos 70–71)** ($126$ con cáncer, $123$ sin cáncer):
  * **Radiólogo 1**: $TA = 76/126 = 0,603$; $TFA = 48/123 = 0,390 \implies \mathbf{d' = 0,54}$ (baja discriminación, mucho solapamiento), $\mathbf{\beta = 1,00}$ (neutro).
  * **Radiólogo 2**: $TA = 101/126 = 0,802$; $TFA = 12/123 = 0,098 \implies \mathbf{d' = 2,14}$ (muy buena discriminación, poco solapamiento), $\mathbf{\beta = 1,62}$ (estricto).
  * *Mamografías (Slide 69)*: expertos discriminan mejor que residentes en orientación **habitual (*upright*)**, pero empeoran en orientación **invertida** (sin efecto en residentes).
* **Casos extremos**: $TA=0,50$ y $TFA=0,50 \implies d'=0$ (azar). $TA=1,0$ y $TFA=1,0 \implies d'=0, \beta \to 0$ (siempre dice SÍ). $TA=0$ y $TFA=0,90 \implies$ discrimina pero invierte las etiquetas.
* **Excel**: meter $TA$ y $TFA$ en celdas amarillas con **punto decimal** (`INV.NORM.ESTAND` y `DIST.NORM.ESTAND.N`).

---

## BLOQUE III: CONTROL EJECUTIVO (Práctica 6 + Cuestionario)

### 1. Las 5 Situaciones de Control Ejecutivo
1. **Situaciones nuevas** sin esquemas aprendidos (*Ej. B: hablar un idioma que estás aprendiendo*).
2. **Conflicto con respuestas habituales dominantes** (*Ej. C: inhibir dar dos besos en pandemia*).
3. **Corrección de errores** (*Ej. A: tejer y corregir un punto mal hecho*).
4. **Planificación o toma de decisiones** (*Ej. E: organizar el horario semanal académico*).
5. **Situaciones difíciles o peligrosas** (*Ej. D: conducir con lluvia intensa*).

### 2. Paradigmas de Interferencia ($\text{TR}_{\text{incongruente}} > \text{TR}_{\text{congruente}}$)
* **Tarea Stroop (1935)**: responder al **color de la tinta** ignorando la palabra. Explicación: *velocidad de procesamiento* (leer es más rápido) y *automaticidad* (leer es automático y compite con nombrar el color, exigiendo inhibición). Variantes: direccional, animal, numérico y **emocional** (palabras emocionales $\to$ mayor TR que neutras).
* **Tarea Simon (1969)**: responder a la palabra («LEFT» $\to$ `A`, «RIGHT» $\to$ `L`) ignorando el lado de la pantalla. En incongruentes la posición espacial activa la mano contraria y compite.
* **Tarea de Flancos (Eriksen y Eriksen, 1974)**: responder a la letra/flecha central ignorando los flancos (`CCCCC` vs `VVCVV`). En incongruentes hay que inhibir la respuesta activada por los flancos.

### 3. Efecto Gratton, Cambio de Tarea y Cuestionario
* **Efecto Gratton (1992, efecto secuencial)**: la interferencia en un ensayo incongruente es **menor tras otro ensayo incongruente (`i-I`) que tras uno congruente (`c-I`)**: $\text{TR}(\texttt{i-I}) < \text{TR}(\texttt{c-I})$. Refleja **adaptación al conflicto** (el ensayo incongruente previo pone en guardia al control ejecutivo).
* **Cambio de Tarea (Jersild, 1927)**: cambiar de tarea produce un **coste (mayor TR y errores)** por dos motivos:
  1. **Cambio de esquema mental** (se reduce con preparación: secuencias predecibles, más tiempo o señal previa *cue*).
  2. **Inercia mental**: parte del coste **persiste pese a la preparación** por la activación residual de la tarea anterior.
* **Cuestionario de Control Atencional (Derryberry y Reed, 2002)**: prueba subjetiva (focalizar, cambiar de tarea, controlar el pensamiento). **20 ítems** (rango **20–80**; **$> 52,5$** = alto control atencional).
  * **Directos ($1\text{ a }4$)**: **`4, 5, 9, 10, 13, 14, 17, 18, 19`**.
  * **Inversos ($4\text{ a }1$)**: **`1, 2, 3, 6, 7, 8, 11, 12, 15, 16, 20`**.

---

## BLOQUE IV: ALTERACIONES PERCEPTIVAS POR INATENCIÓN (Práctica 7)

| Fenómeno | Paradigma y Datos Clave | Causa / Mecanismo |
| :--- | :--- | :--- |
| **Ceguera por Inatención** | **Mack y Rock (1998)**: cruz $200\text{ ms}$ (sin sacádicos) + máscara $1500\text{ ms}$; no se ve el cuadrado inesperado. **Gorila invisible / TAC (Drew et al., 2013)**: el **83%** de radiólogos expertos no ve un gorila en el TAC aunque lo miran (*eye-tracking*). También al usar el móvil. | Un estímulo saliente e inesperado no se percibe porque la **atención está ocupada en otra tarea** (no se busca). |
| **Ceguera al Cambio** | **Simons y Levin (1997)**: cambio de interlocutor tras una puerta. Ocurre **incluso buscando activamente el cambio** (tras un parpadeo o corte). | Detectar cambios exige **búsqueda activa, tiempo y memoria de trabajo**. Codificamos solo la **esencia (*gist*)** de la escena; si no cambia la esencia, pasa desapercibido. |
| **Parpadeo Atencional** | **Paradigma RSVP** (flujo rápido de letras: $T_1$ y $T_2$). Si $T_2$ sale entre **$100\text{–}450\text{ ms}$** tras $T_1$, no se percibe conscientemente. Se recupera a los **$\approx 500\text{ ms}$**. | Procesar $T_1$ consume recursos atencionales; $T_2$ se procesa parcialmente pero sin llegar a la conciencia. **Se reduce o suprime si $T_2$ es amenazante** (valencia negativa) o con meditación. |

---

## BLOQUE V: REDES ATENCIONALES Y TAREA ANTI (Práctica 8)

### 1. Modelo de Posner, ANT y ANTI
* **3 Redes de Posner (1990, 2012)**: **Alerta** (activación general/vigilancia, estado), **Orientación** (red posterior, selección espacial) y **Control Ejecutivo** (red anterior, inhibición/resolución de conflicto).
* **ANT (Fan et al., 2002)** $\to$ **ANTI (Callejas et al., 2005)**: la ANT usaba asteriscos tanto para alerta como para orientación y **no medía interacciones**. La ANTI desacopla las 3 redes:
  * **Alerta (2 niveles)**: **Tono auditivo** ($50\%$) vs. **No tono** ($50\%$).
  * **Orientación (3 niveles)**: asterisco espacial **Cued** (válido), **No cue** (neutro) o **Uncued** (inválido).
  * **Control Ejecutivo (2 niveles)**: 5 flechas (responder a la central: `C` izq., `M` dcha.) **Congruente** vs. **Incongruente**.

### 2. Cronometría (SOA vs. ISI) y Diseño
* **SOA** = inicio $S_1 \to$ inicio $S_2$ ($\text{Duración } S_1 + \text{ISI}$). **ISI** = fin $S_1 \to$ inicio $S_2$.
* **Secuencia**: Fijación ($400\text{–}1600\text{ ms}$) $\to$ Tono ($50\text{ ms}$) $\to$ ISI ($400\text{ ms}$) [$\mathbf{\text{SOA}_{\text{Alerta}} = 450\text{ ms}}$] $\to$ Asterisco ($50\text{ ms}$) $\to$ ISI ($50\text{ ms}$) [$\mathbf{\text{SOA}_{\text{Orientación}} = 100\text{ ms}}$] $\to$ Target ($\text{TR}$ o máx. $1700\text{ ms}$).
* **Diseño factorial**: **$2 \times 3 \times 2 = 12$ condiciones** (VD = TR en ms).

### 3. Efectos Principales e Interacciones
* **Efecto Alerta** ($\text{TR}_{\text{No tono}} - \text{TR}_{\text{Tono}}$): el tono reduce el TR (aumenta la activación).
* **Efecto Orientación / *Cueing*** ($\text{TR}_{\text{Uncued}} - \text{TR}_{\text{Cued}}$): la señal válida (*cued*) reduce el TR.
* **Efecto Control Ejecutivo / Congruencia** ($\text{TR}_{\text{Incongruente}} - \text{TR}_{\text{Congruente}}$): ensayos incongruentes tienen mayor TR por la inhibición de flancos.

| Interacción ($2 \times 2$) | Qué ocurre en los TRs e Interpretación | Ejemplo de clase |
| :--- | :--- | :--- |
| **Alerta $\times$ Orientación** | El tono **AUMENTA el efecto *cueing*** (la alerta potencia la orientación espacial hacia el asterisco). | **GPS (alerta) + cartel azul (orientación)**: coges la salida más rápido. |
| **Alerta $\times$ Control Ejecutivo** | El tono **ACENTÚA el efecto de congruencia** (en la diapo: bloquea el control ejecutivo —TR más largo en incongruentes— para priorizar rapidez). | **Disparos (alerta) en un examen (control)**: contestas aún más lento las preguntas difíciles. |
| **Orientación $\times$ Control Ejecutivo** | La señal válida (*cued*) **DISMINUYE el efecto de congruencia** (orientar al lugar del target facilita ignorar flancos y reduce el TR en incongruentes). | **Ruta difícil en bici (control) señalizada con luces (orientación)**: sorteas obstáculos más rápido. |
