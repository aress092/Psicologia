# Introducción a la Psicofísica y Teoría de Detección de Señales (TDS)
**Autor:** Pío Tudela (Departamento de Psicología Experimental, Universidad de Granada, 2007) — *Unidad Didáctica 2: Psicofísica*

---

## 1. Introducción
* El estudio científico de las sensaciones se inicia con la publicación en **1860** del libro *Elementos de Psicofísica* de **Gustav Theodor Fechner** (primer libro de psicología experimental).
* **Objetivo de la Psicofísica**: relacionar cuantitativamente dos dimensiones de la realidad:
  * **Dimensión física**: concretada en el **estímulo ($E$)** (medible directamente en escalas físicas).
  * **Dimensión psíquica**: concretada en la **sensación ($S$)** (medida a través de los estímulos).
* **Paralelismo psicofísico y panpsiquismo**: Fechner rechazaba el materialismo reduccionista y defendía que materia y mente son dos aspectos de una única realidad viva (como el lado cóncavo y convexo de un arco de circunferencia). Su postura filosófica sobre la naturaleza última psíquica de la realidad se denomina *panpsiquismo*.
* La psicofísica distingue entre **nivel de tarea** y **nivel de proceso** (centrándose en **detección** y **discriminación**), demostrando que se pueden establecer relaciones cuantitativas entre el mundo físico y el psíquico **sin necesidad de recurrir a la fisiología** (nivel de mecanismo).

---

## 2. Psicofísica Clásica

### 2.1. Conceptos Fundamentales
* **Medir**: asignar números a objetos según propiedades que determinan la **escala de medida**.
* Fechner quiso aplicar a las sensaciones una **escala de razón**, para lo cual necesitaba:
  1. Un **punto cero de la sensación ($S_0$)**: medido indirectamente por el **Umbral Absoluto ($UA$ o $E_0$)**.
  2. Una **unidad de medida**: la **Diferencia Mínima Perceptible ($DMP$)**, medida indirectamente por el intervalo que determina el **Umbral Diferencial ($UD$)**.
* **Umbral Absoluto ($UA$ o $E_0$)**: también llamado *umbral de detección*; valor de las dimensiones físicas de los estímulos por debajo del cual el estímulo no es detectado y por encima del cual sí es detectado (cantidad mínima de estimulación capaz de producir una sensación). Define un **punto** ($E_0 \to S_0$).
* **Umbral Diferencial ($UD$)**: también llamado *umbral de discriminación*; valor mínimo de cambio en la dimensión física de los estímulos capaz de producir un cambio en la sensación. Ese cambio subjetivo se denomina **Diferencia Mínima Perceptible ($DMP$)**. Tanto $UD$ como $DMP$ definen un **intervalo**, no un punto ($UD$ en el continuo físico, que crece progresivamente; $DMP$ en el continuo subjetivo, que Fechner asume constante).

### 2.2. Tareas Psicofísicas
* **Tareas de detección**: presentación de un **único estímulo** y emisión de una respuesta por el observador (en psicofísica clásica, respuesta verbal **SÍ** o **NO** para medir el $UA$). Los ensayos con estímulo se mezclan aleatoriamente con **ensayos trampa (*catch trials*)** sin estímulo para evitar aciertos por repetición rutinaria.
* **Tareas de discriminación**: presentación de **dos o más estímulos** asociados cada uno a una respuesta (para medir el $UD$). Se mantiene constante el **Estímulo Estándar ($EE$)** y se varía el **Estímulo de Prueba ($EP$)**. El observador responde si el $EP$ es **MAYOR (`+`)**, **IGUAL (`=`)** o **MENOR (`-`)** que el $EE$. Si se presentan simultáneamente y se pide responder si son **IGUALES** o **DIFERENTES**, se denomina **tarea de igualación (*matching task*)**.
* **Parámetros**: **precisión** (aciertos/errores; único parámetro considerado habitualmente en psicofísica clásica) y **velocidad** (o su inversa, el **tiempo de reacción**).

### 2.3. Métodos Psicofísicos: El Método de los Límites
Los métodos psicofísicos tradicionales propuestos por Fechner son el **método de los límites**, el **método de los estímulos constantes** y el **método de los ajustes**.
En el **Método de los Límites**, el experimentador ordena los valores de menor a mayor y los presenta paso a paso en **series ascendentes ($A$)** y **series descendentes ($D$)** (comenzando en valores distintos para evitar rutinas). En cuanto el observador cambia su respuesta, la serie termina.

#### A) Cálculo del Umbral Absoluto ($UA$) (Tabla 1 del texto)
1. Se calcula el umbral de cada serie como el **punto medio del intervalo donde cambia la respuesta** (ej. entre $27$ `+` y $26$ `-` es $26,5$).
2. Se calcula el promedio por separado de las series ascendentes ($\text{Media Series } A = 24,9$) y descendentes ($\text{Media Series } D = 24,3$).
3. Se calcula el **Umbral Absoluto ($UA$)** como el promedio de todas las series ($24,6$).
* **Detección de sesgos comparando series descendentes ($UD$) y ascendentes ($UA$)**:
  * **Sesgo de habituación**: tendencia a repetir la misma respuesta más allá del punto real de cambio $\implies$ produce umbrales más bajos en series $D$ y más altos en series $A$ $\implies \mathbf{UD - UA < 0}$ (**negativa**).
  * **Sesgo de anticipación**: tendencia a adelantar el cambio antes de tiempo $\implies$ produce umbrales más altos en series $D$ y más bajos en series $A$ $\implies \mathbf{UD - UA > 0}$ (**positiva**).
  * Si $\mathbf{UD - UA = 0}$, no hay sesgo ($UD = UA = \text{Umbral Absoluto}$).

#### B) Cálculo del Umbral Diferencial ($UD$) (Tabla 2 del texto, con $EE = 60$)
La serie termina cuando aparece la respuesta opuesta a la de partida (pasa por dos transiciones: de MAYOR a IGUAL y de IGUAL a MENOR, o viceversa):
* **Umbral Superior ($US$)**: punto medio de la transición entre MAYOR (`+`) e IGUAL (`=`) (en Tabla 2: $US_A = 65$, $US_D = 67$, $US = 66$).
* **Umbral Inferior ($UI$)**: punto medio de la transición entre IGUAL (`=`) y MENOR (`-`) (en Tabla 2: $UI_A = 51$, $UI_D = 49$, $UI = 50$).
* **Intervalo de Incertidumbre ($II$)**: diferencia entre $US$ y $UI$, donde los $EP$ se perciben iguales al $EE$ (abarca dos discriminaciones):
  $$II = US - UI = 66 - 50 = 16$$
* **Umbral Diferencial ($UD$)**: mitad del intervalo de incertidumbre:
  $$UD = \frac{II}{2} = \frac{16}{2} = 8$$
* **Punto de Igualdad Subjetiva ($PIS$)**: punto medio entre $US$ y $UI$ (valor que el observador considera igual al $EE$):
  $$PIS = \frac{US + UI}{2} = UI + UD = 58$$
* **Error Constante ($EC$)**: diferencia entre el $PIS$ y el $EE$:
  $$EC = PIS - EE = 58 - 60 = -2$$
  Si $EC > 0$, sobreestima el $EE$; si $EC < 0$, subestima el $EE$ (aquí lo subestima en 2 unidades).

### 2.4. Las Leyes Psicofísicas de Weber y Fechner
* **Ley de Weber (Ernst Heinrich Weber)**: el $UD$ es una fracción constante del $EE$:
  $$\frac{UD}{EE} = c \quad \Longleftrightarrow \quad \frac{\Delta EE}{EE} = c \quad \Longleftrightarrow \quad UD = c \cdot EE$$
  Con los datos de la Tabla 2 ($EE = 60, UD = 8 \implies c = 8/60 = 0,133$).
* **Deducción de la Ley de Fechner**:
  * Por inducción desde $E_0$ ($UA$): $E_1 = E_0(1+c)$, $E_2 = E_0(1+c)^2$, $\dots$, $E_i = E_0(1+c)^r$, donde $r$ es el valor de la sensación en número de $DMP\text{s}$ por encima de $S_0$.
  * Aplicando logaritmos y despejando $r$:
    $$\log E_i = \log E_0 + r \log(1+c) \implies r = \frac{1}{\log(1+c)} \cdot \log\left(\frac{E_i}{E_0}\right)$$
  * Haciendo $k = \frac{1}{\log(1+c)}$ (**constante de Fechner**):
    $$r = k \cdot \log\left(\frac{E_i}{E_0}\right)$$
* **Limitaciones**:
  1. La Ley de Weber se cumple en **valores intermedios** de intensidad, pero no en los **valores extremos**.
  2. La constancia de la $DMP$ depende del tipo de continuo sensorial:
     * **Continuos protéticos (cuantitativos/aditivos)**: varía la cantidad/intensidad pero no la cualidad (ej. intensidad de sonido o luz acromática). No cumplen la Ley de Fechner (cada $DMP$ añade cada vez más sensación), sino la de Stevens.
     * **Continuos metatéticos (cualitativos)**: varía la cualidad (ej. tono auditivo según la frecuencia). Sí cumplen la Ley de Fechner.

---

## 3. La Teoría de Detección de Señales (TDS)
* Surge a mediados del s. XX (inicialmente en audición) y analiza la detección como una **toma de decisiones en contexto de incertidumbre** (análoga al diagnóstico médico de un radiólogo).
* Distingue dos clases de procesos en una tarea de detección: **procesos sensoriales** (medidos por $d'$) y **procesos de decisión** (medidos por $\beta$).
* **Matriz de confusión ($2 \times 2$)**: filas $=$ estados del mundo (**Señal $SR$** vs. **Ruido $R$**); columnas $=$ respuestas del observador (**SÍ** vs. **NO**).
  *Con Señal ($SR$)*: **Acierto ($A$, proporción $p$)** y **Fallo ($F$, proporción $1-p$)**.
  *Con Ruido ($R$)*: **Falsa Alarma ($FA$, proporción $q$)** y **Rechazo Correcto ($RC$, proporción $1-q$)**. Tiene **2 grados de libertad** (basta conocer $A$ y $FA$).
* **Supuestos sensoriales**: prescinde del umbral sensorial; los sistemas sensoriales están **siempre activos**, generando dos distribuciones normales sobre el continuo de sensaciones: la del **Ruido ($R$)** y la de la **Señal ($SR$, desplazada a la derecha)**.
  * **Razón de verosimilitud ($p/q$)**: cociente entre la probabilidad de que $S_i$ proceda de $SR$ ($p$) y de que proceda de $R$ ($q$). Vale $1$ en el punto de cruce, $<1$ a la izquierda y $>1$ a la derecha.
  * **Índice $d'$ («d prima»)**: distancia en puntuaciones $z$ entre las medias de las distribuciones $R$ y $SR$ (mide el grado de solapamiento o discriminabilidad sensorial).
* **Supuestos de decisión**: el observador adopta un valor fijo de razón de verosimilitud como **criterio ($\beta$, punto de corte)**:
  * **$\beta = 1$**: criterio **neutro** (en el punto de cruce, sin sesgo).
  * **$\beta > 1$**: criterio **estricto** (a la derecha; sesgado hacia el NO $\implies$ menos aciertos y menos falsas alarmas).
  * **$\beta < 1$**: criterio **laxo** (a la izquierda; sesgado hacia el SÍ $\implies$ más aciertos y más falsas alarmas).
* **Cálculo de parámetros (Cuadro 3, p. 22)**: $150$ ensayos $SR$ ($90$ aciertos $\implies TA = 0,60$) y $150$ ensayos $R$ ($30$ FA $\implies TFA = 0,20$):
  * Ruido: $z(FA) = 0,842$, $q[z(FA)] = 0,280$.
  * Señal: $z(A) = -0,253$, $p[z(A)] = 0,386$.
  * $d' = z(FA) - z(A) = 0,842 - (-0,253) = \mathbf{1,095}$.
  * $\beta = p[z(A)] / q[z(FA)] = 0,386 / 0,280 = \mathbf{1,38}$.
* **Independencia experimental**: variables sensoriales (intensidad, dificultad) afectan a **$d'$ pero no a $\beta$**; variables motivacionales (incentivos) afectan a **$\beta$ sin modificar $d'$**.

---

## 4. La Nueva Psicofísica (S. S. Stevens)
* Introduce los **métodos directos** basados en juicios cuantitativos directos del observador sobre sus sensaciones:
  1. **Estimación de Magnitud**: se presenta un estímulo de referencia con un valor numérico (**módulo**, ej. $50$) y el sujeto asigna números a otros estímulos manteniendo la razón entre magnitudes (o sin módulo inicial).
  2. **Producción de Magnitud**: el experimentador da un número y el observador ajusta un estímulo continuo hasta alcanzar esa sensación.
* **Ley Potencial de Stevens**:
  $$S = c \cdot E^k \quad \Longleftrightarrow \quad \log S = \log c + k \cdot \log E$$
  donde $c$ es una constante de escala y $k$ es el exponente propio de cada modalidad sensorial ($k=1$ lineal; $k>1$ positivamente acelerada; $k<1$ negativamente acelerada). En coordenadas logarítmicas son rectas de pendiente $k$. Funciona en **continuos protéticos** (aditivos), pero no en los metatéticos.
