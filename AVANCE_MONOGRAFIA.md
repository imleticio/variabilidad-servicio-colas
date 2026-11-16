# Avance de la monografía

**Tema:** influencia de la variabilidad de los tiempos de servicio en los sistemas de colas.

**Estado actual:** secciones 1–5 desarrolladas. El usuario ejecutó la versión anterior del notebook y se preservó su archivo con salidas. La nueva versión incorpora Drive, guardado incremental y cuatro gráficos a color; diez pruebas locales aprobadas y una numérica omitida. Verificación independiente sin bloqueantes reproducidos en el alcance examinado. Autorización y escritura reales en Drive, ejecución completa y revisión visual de esta versión pendientes. No se generó PDF ni se publicó un enlace.

**Próximo paso:** subir `simulacion/colas_variabilidad_colab.ipynb` a Colab, ejecutar todas las celdas, revisar y guardar las salidas. Después se podrán redactar los resultados del apartado 6 y compartir el enlace de lectura con el docente.

## Cómo mantener este registro

- `[x]` indica una tarea realizada y comprobada; `[ ]`, una tarea pendiente.
- Si una sección está parcialmente desarrollada, mantener su casilla general pendiente y marcar únicamente los subítems terminados.
- Actualizar este archivo al completar cada sección o cambiar el alcance. Registrar debajo la evidencia y las decisiones relevantes.
- Distinguir entre sección redactada y sección revisada. La revisión de contenido no equivale a compilación o validación visual.
- Desarrollar las secciones una por una, sin dar por terminado un apartado solo porque exista su título o un borrador parcial.

## 1. Preparación realizada

- [x] Leer la consigna del Trabajo Final Integrador y la planilla de propuestas grupales.
- [x] Elegir el tema y delimitar la pregunta de trabajo.
- [x] Reunir cuatro fuentes fundacionales: tres PDF y un capítulo HTML.
- [x] Reunir cuatro artículos seleccionados, incluidos preprint y manuscrito de autores, e identificar sus limitaciones.
- [x] Registrar referencias, enlaces, incidencias de descarga y documentos excluidos.
- [x] Acordar el uso de `thesis-writing` para redacción y revisión en LaTeX.
- [x] Acordar el uso de `thesis-scientific-figures` para diagramas y figuras cuando aporten claridad.
- [x] Registrar la prohibición de generar PDF hasta autorización expresa del usuario.
- [x] Definir la estructura inicial y el orden de redacción.
- [x] Crear este registro de avance.

**Evidencia:** `METODOLOGIA_MONOGRAFIA.md`, `bibliografia/REFERENCIAS.md` y `bibliografia/articulos/REFERENCIAS_ARTICULOS.md`.

**Pendiente:** leer y analizar en profundidad los pasajes de las fuentes que se utilicen en cada sección. Haber descargado e identificado un documento no significa haber completado su lectura crítica.

## 2. Estructura y redacción

### Elementos preliminares

- [ ] Portada completada: título definitivo, integrantes, institución, carrera, materia, docente y fecha.
- [ ] Resumen redactado y revisado **al terminar el cuerpo del trabajo**.

**Título provisorio:** *Influencia de la variabilidad de los tiempos de servicio en los sistemas de colas: análisis comparativo y demostración mediante simulación.*

### 1. Introducción

- [x] Explicar el contexto y la relevancia de los sistemas de colas.
- [x] Plantear por qué la media de servicio no basta para explicar las esperas.
- [x] Justificar el tema y formular la pregunta de investigación.
- [x] Delimitar alcance y supuestos iniciales: un servidor, llegadas Poisson y disciplina FCFS.
- [x] Guardar el apartado como fragmento LaTeX con citas verificadas en `monografia/secciones/01_introduccion.tex` y entradas en `monografia/referencias.bib`.
- [x] Revisar claridad, precisión y correspondencia con la consigna.

**Comprobaciones:** citas existentes en `.bib`, etiquetas únicas, llaves y entornos balanceados; respaldo conceptual cotejado con Virtamo (pp. 1–6) y Lauber Bonomo y colaboradores (preprint v1, introducción y sección II). Sin cifras ni resultados experimentales anticipados. La introducción está incluida desde `monografia/main.tex`; inclusión y rutas comprobadas estáticamente. Compilación y revisión visual pendientes.

**Revisión del usuario:** realizada favorablemente. Indicó: «estuve leyendo la introduccion y me gustoó, vamos con el otro item».

**Pregunta de trabajo:** ¿cómo afecta la variabilidad de los tiempos de servicio al tiempo medio de espera cuando se mantienen constantes la tasa de llegada y el tiempo medio de atención?

### 2. Objetivos

- [x] Redactar el objetivo general.
- [x] Redactar objetivos específicos alcanzables y vinculados con el análisis.
- [x] Integrar y revisar el apartado en LaTeX.

**Evidencia:** `monografia/secciones/02_objetivos.tex`, incluido desde `monografia/main.tex`. Un objetivo general y cinco específicos: fundamentos, comparación analítica, revisión crítica, demostración reproducible y discusión de límites. Cotejados con la pregunta y el alcance de la introducción. Inclusión, etiquetas, llaves y entornos comprobados estáticamente; sin compilación ni inspección del renderizado.

**Revisión del usuario:** realizada favorablemente. Indicó: «ok, me gustaroin los objetivos, pasemos a lo que sigue».

### 3. Marco conceptual

- [x] Explicar componentes del sistema y notación de Kendall.
- [x] Definir llegadas, tiempos de servicio y disciplina FCFS.
- [x] Explicar media, varianza y coeficiente de variación.
- [x] Definir utilización y condición de estabilidad.
- [x] Distinguir espera en cola y tiempo total en el sistema; presentar la ley de Little.
- [x] Presentar M/D/1 y M/M/1 como casos particulares de M/G/1.
- [x] Desarrollar Pollaczek–Khinchine con sus supuestos y notación consistente.
- [x] Incorporar un esquema conceptual para distinguir cola, servicio y permanencia, editable en TikZ.
- [x] Integrar y revisar el apartado en LaTeX con fuentes comprobadas.

**Evidencia:** `monografia/secciones/03_marco_conceptual.tex`, `monografia/figuras/cola_un_servidor.tex` y su inclusión desde `monografia/main.tex`, que carga TikZ. Seis subsecciones y una tabla simbólica M/D/1–M/M/1; fuente principal Virtamo, pp. 1–6.

**Comprobaciones:** inclusiones recursivas, claves de cita, etiquetas/referencias, llaves, entornos y delimitadores matemáticos comprobados. Dieciocho casos racionales de las identidades de Pollaczek–Khinchine, Little y servicio residual, y del factor dos para espera en cola, sin resultados de simulación ni parámetros experimentales nuevos. Revisión nativa automatizada no disponible por archivos sin seguimiento Git y alcance no declarado; no se modificó autoridad de revisión.

**Revisión del usuario:** realizada favorablemente. Indicó: «ok, lo estuve leyendo y me gusto vamos al sigguiente item». Compilación y comprobación visual de figura, tabla y páginas diferidas por la restricción vigente; no se afirma que el resultado renderizado esté validado.

### 4. Revisión de la literatura

- [x] Leer los pasajes pertinentes y registrar qué afirmaciones respalda cada fuente.
- [x] Comparar aportes sobre variabilidad y espera, organizados por ideas.
- [x] Examinar aplicaciones y estrategias de reducción de congestión.
- [x] Diferenciar resultados al cambiar disciplina, estructura o medida de desempeño.
- [x] Integrar y revisar la síntesis crítica en LaTeX; evitar una sucesión de resúmenes por autor.

**Evidencia:** `monografia/secciones/04_revision_literatura.tex`, incluido desde `monografia/main.tex`; tres entradas bibliográficas nuevas en `monografia/referencias.bib` (cinco en total). Cinco subsecciones organizadas por ideas. Lecturas y límites registrados en `bibliografia/articulos/REFERENCIAS_ARTICULOS.md`: Joustra, pp. 448–463; Lauber Bonomo y colaboradores, pp. 1–13 del preprint v1; Koole y colaboradores, pp. 1–12; Bondi–Whitt limitado a resumen y comienzo de introducción de p. 219.

**Comprobaciones:** claves de cita y referencias internas resueltas en fuente, etiquetas únicas, llaves y entornos balanceados y delimitadores matemáticos comprobados recursivamente. Cotejadas las distinciones entre tiempo total y espera en cola, capacidad y duración de servicio, orden convexo y varianza. Evaluación nativa no disponible por archivos sin seguimiento Git y alcance no declarado. No se ejecutaron compilación, inspección visual ni simulaciones.

**Continuidad indicada por el usuario:** «ok, vamos con el apartado 5». No se registraron correcciones al apartado 4.

### 5. Metodología

- [x] Describir el enfoque de monografía y la búsqueda y selección realmente realizadas, sin atribuirles exhaustividad no demostrada.
- [x] Definir criterios de comparación entre modelos.
- [x] Acordar Google Colab como entorno previsto: un notebook Python con NumPy, pandas y Matplotlib, con simulador pequeño propio y función demostrativa dentro de la monografía; SciPy se utilizará únicamente para el cuantil de Student.
- [x] Completar el diseño experimental: tercera distribución, parámetros, duración, tratamiento del período inicial y cantidad de réplicas.
- [x] Definir parámetros constantes y distribuciones de servicio con igual media y distinta variabilidad.
- [x] Definir verificación, réplicas y análisis estadístico de la futura simulación.
- [x] Integrar y revisar el apartado en LaTeX.

**Evidencia:** `monografia/secciones/05_metodologia.tex`, incluido en `monografia/main.tex`, y referencia `banksAnalisisSalidas` añadida a `monografia/referencias.bib` (seis entradas en total). Siete subsecciones, redactadas prospectivamente para el experimento.

**Diseño previsto:** λ = 0,8 entidades/minuto; m = 1 minuto; ρ = 0,8. Servicio constante, exponencial e hiperexponencial H₂ (probabilidad 0,8 con media m/2 y 0,2 con media 3m). Cuarenta réplicas de 140 000 entidades por escenario; descarte de 20 000 y medición de las siguientes 100 000, sin reiniciar la cola. Control apareado con descarte alternativo de 40 000; intervalos aproximados del 95 % entre medias de réplica y umbrales diagnósticos propios del diseño. Semilla maestra 2026 y flujos separados. La política completa se conserva en el apartado LaTeX y en la sección 5 de `METODOLOGIA_MONOGRAFIA.md`.

**Comprobaciones:** momentos exactos de la mezcla (media m, varianza 3m²), ρ y referencias analíticas de espera 2/4/8 minutos; ventanas de medición dentro del presupuesto; citas, referencias, etiquetas, llaves y entornos comprobados en siete fuentes LaTeX. Estas comprobaciones no son experimentos ni garantizan precisión o eliminación de sesgo. Evaluación nativa no disponible por alcance Git sin declarar. Compilación, inspección visual y ejecución en Colab pendientes.

**Revisión solicitada por el usuario:** simplificar el inicio y añadir apoyos visuales, autorizada con «me guta el enfoque lo hagamos».

- [x] Sustituir el inicio extenso sobre selección bibliográfica por un párrafo de enfoque metodológico y retirar detalles internos de descarga.
- [x] Añadir el procedimiento previsto de simulación como diagrama TikZ de seis etapas, siguiendo `thesis-scientific-figures`.
- [x] Añadir el esquema TikZ de ventanas apareadas sobre la misma realización, con escala proporcional por índice, siguiendo `thesis-scientific-figures`.
- [x] Comprobar inclusiones, referencias, conservación del diseño y límites de las ventanas sin compilar.

**Evidencia de la revisión:** `monografia/figuras/procedimiento_simulacion.tex` y `monografia/figuras/ventanas_medicion.tex`, incluidos desde `05_metodologia.tex` con texto explicativo y leyendas de elaboración propia. Las figuras representan el diseño previsto, no resultados ni software implementado. No se añadieron dependencias. Verificación recursiva de nueve fuentes LaTeX aprobada; dos mediciones de 100 000 entidades con 80 000 de solapamiento y sin reinicios. Evaluación nativa no disponible por alcance Git sin declarar.

**Lectura de la versión revisada por el usuario:** pendiente. Compilación e inspección del resultado renderizado diferidas; las comprobaciones de fuente no equivalen a aceptación visual.

### 6. Demostración y resultados

- [x] Definir el ejemplo hipotético con parámetros explícitos y unidades consistentes en la metodología.
- [x] Obtener y comprobar cálculos teóricos de referencia (2/4/8 minutos); no son resultados de simulación.
- [x] Crear el notebook `.ipynb` para Google Colab con explicaciones, código y dependencias indicadas en español.
- [x] Implementar el generador, núcleo FCFS, réplicas, estimación, gráficos y exportaciones del diseño en las celdas del notebook.
- [x] Verificar localmente el núcleo FCFS, casos deterministas, entradas rechazadas, configuración, momentos teóricos y sintaxis de todas las celdas.
- [ ] Verificar numéricamente el flujo completo con NumPy, pandas, Matplotlib y SciPy; la prueba opcional se omitió localmente por dependencias ausentes.
- [x] Preservar sin cambios la versión anterior ejecutada por el usuario, con manifiesto SHA-256.
- [x] Implementar almacenamiento explícito en Drive, carpetas exclusivas y guardado incremental con identificación de datos parciales.
- [x] Ampliar el código a cuatro gráficos con colores por escenario, diferenciando teoría, resultados y diagnósticos.
- [ ] Comprobar la ejecución completa de la versión ampliada del notebook en Google Colab, su persistencia real en Drive y sus cuatro figuras; no confundir una comprobación local con esta validación.
- [ ] Ejecutar los experimentos y conservar parámetros, semillas y resultados reproducibles.
- [ ] Preparar tablas y gráficos trazables; diferenciar resultados analíticos y simulados.
- [ ] Integrar y revisar el apartado en LaTeX, sin anticipar resultados no obtenidos.

**Notebook entregado:** `simulacion/colas_variabilidad_colab.ipynb`, con 12 celdas Markdown y 12 de código, sin salidas antiguas en el código actualizado. Copia exacta de la ejecución anterior: `simulacion/ejecuciones/colas_variabilidad_colab_ejecutado_original.ipynb`; manifiesto `original_manifest.json` en la misma carpeta. Guía: `simulacion/README.md`. Pruebas: `simulacion/tests/test_notebook.py`, sobre el código real de las celdas.

**Verificación local observada:** `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s simulacion/tests -v`, salida final 0; once pruebas, diez aprobadas y una numérica omitida. Para persistencia se observó RED por ausencia de la nueva celda y GREEN tras implementarla. Las pruebas comprueban carpetas diferentes, CSV y rechazo de rutas absolutas, traversal y escapes por enlaces simbólicos. Una verificación independiente no reprodujo bloqueantes, confirmó el SHA-256 original y examinó consentimiento, límites de escritura y coherencia científica. No se instalaron paquetes ni se conectó Drive desde el agente. Evaluación nativa no disponible por alcance Git sin declarar; no se alteró autoridad de revisión.

**Prueba pendiente y acción requerida:** subir y ejecutar la nueva versión en Colab, autorizar Drive, comprobar carpeta, estado final y cuatro PNG. La ejecución anterior no comprueba esas funciones nuevas. Los conteos descriptivos de esperas no cambian las semillas ni las ventanas del diseño. No usar pruebas locales como evidencia de persistencia real, renderizado o validación de un servicio real.

### 7. Discusión y análisis crítico

- [ ] Interpretar los resultados en relación con la literatura.
- [ ] Explicar las implicaciones prácticas de la variabilidad.
- [ ] Examinar los supuestos que sostienen las conclusiones y los límites de generalización.
- [ ] Explicitar limitaciones de la revisión y de la demostración.
- [ ] Integrar y revisar el apartado en LaTeX.

### 8. Conclusiones

- [ ] Responder la pregunta de investigación.
- [ ] Vincular conclusiones con objetivos y evidencia desarrollada.
- [ ] Identificar posibles continuaciones sin incorporar resultados nuevos.
- [ ] Integrar y revisar el apartado en LaTeX.

### Referencias bibliográficas

- [x] Crear `monografia/referencias.bib` con las dos fuentes citadas en la introducción, sin asignar fecha no verificada a Virtamo ni confundir el preprint con su publicación posterior.
- [x] Configurar BibTeX con estilo numérico `unsrt` en `monografia/main.tex`.
- [ ] Completar las referencias de las siguientes secciones.
- [ ] Verificar metadatos y versiones de todas las fuentes citadas.
- [ ] Comprobar correspondencia entre citas del texto y referencias finales.

### Anexos y archivos complementarios

- [ ] Determinar qué contenido necesita anexo; no añadirlo solo para aumentar extensión.
- [ ] Incluir código, parámetros e instrucciones de reproducción si se desarrolla el experimento.
- [ ] Verificar correspondencia entre archivos complementarios y resultados presentados.

## 3. Revisión del conjunto, sin generar PDF

- [ ] Comprobar cobertura de los requisitos de la modalidad monografía.
- [ ] Revisar coherencia entre pregunta, objetivos, método, resultados y conclusiones.
- [ ] Unificar terminología, símbolos, unidades y referencias cruzadas.
- [ ] Verificar que no haya citas, datos ni resultados inventados o pendientes presentados como definitivos.
- [ ] Revisar el código fuente LaTeX y las fuentes editables de las figuras, sin compilar.

## 4. Etapa diferida: requiere autorización del usuario

**No ejecutar esta etapa todavía.** La restricción incluye las compilaciones de prueba y las figuras independientes. Consultar PDF bibliográficos existentes sí está permitido.

- [ ] Recibir autorización expresa para generar PDF.
- [ ] Comprobar dependencias y compilar el documento y las figuras que correspondan.
- [ ] Revisar advertencias, citas, referencias y numeración.
- [ ] Inspeccionar visualmente páginas, fórmulas, tablas y figuras; corregir recortes o superposiciones.
- [ ] Comprobar la extensión orientativa de 15–25 páginas, sin bibliografía ni anexos, priorizando calidad sobre cantidad.
- [ ] Generar la versión final después de las correcciones.

## 5. Registro de avances y decisiones

| Registro | Avance o decisión | Evidencia |
|---|---|---|
| A1 | Tema elegido: efecto de la variabilidad del servicio en las esperas, a tasa de llegada y media de servicio constantes. | Conversación y `METODOLOGIA_MONOGRAFIA.md`. |
| A2 | Bibliografía inicial descargada y artículos seleccionados identificados; lectura crítica completa pendiente. | Índices de `bibliografia/` y `bibliografia/articulos/`. |
| A3 | Redacción en LaTeX y figuras científicas editables; no generar PDF hasta indicación expresa. | `METODOLOGIA_MONOGRAFIA.md`. |
| A4 | Índice inicial definido y acuerdo de desarrollar las secciones una por una. | Sección 2 de este archivo. |
| A5 | Registro de avance creado; no existe todavía una sección de la monografía redactada. | `AVANCE_MONOGRAFIA.md`. |

| A6 | Introducción redactada y revisada: contexto, problema, pregunta, alcance y enfoque. Citas y estructura de fuente comprobadas; revisión del usuario e integración en documento raíz pendientes. | `monografia/secciones/01_introduccion.tex` y `monografia/referencias.bib`. Sin compilación ni PDF. |

| A7 | Documento principal creado para compilación por el usuario desde VS Code; incluye introducción y referencias. Directiva raíz añadida al fragmento. Portada provisional con datos personales pendientes. Comprobación estática aprobada; no se compiló. | `monografia/main.tex`, `monografia/secciones/01_introduccion.tex` y `monografia/referencias.bib`. |

| A8 | El usuario revisó favorablemente la introducción y autorizó continuar con el siguiente apartado. Objetivos redactados e incluidos en main.tex; cinco objetivos específicos coherentes con el alcance. Comprobaciones estáticas aprobadas, revisión del usuario pendiente. | `monografia/secciones/02_objetivos.tex` y `monografia/main.tex`. Sin compilación por el agente. |

| A9 | El usuario acordó utilizar Google Colab para la demostración: un notebook Python con NumPy, pandas y Matplotlib y simulador propio pequeño. Se conserva la modalidad monografía y el informe LaTeX. Diseño detallado, creación del notebook y ejecución pendientes. | Sección 5 de `METODOLOGIA_MONOGRAFIA.md`. |

| A10 | El usuario revisó favorablemente los objetivos. Marco conceptual desarrollado con seis subsecciones, diagrama conceptual y tabla analítica; incluido en main.tex. Comprobaciones estáticas y matemáticas aprobadas. Sin simulación, compilación ni inspección visual; lectura del usuario pendiente. | `monografia/secciones/03_marco_conceptual.tex`, `monografia/figuras/cola_un_servidor.tex` y `monografia/main.tex`. |

| A11 | El usuario revisó favorablemente el marco conceptual. Revisión de literatura redactada por ideas e incluida en main.tex; tres referencias nuevas verificadas. Lectura de Bondi limitada explícitamente a primera página. Comprobación estática aprobada; lectura del usuario y verificación renderizada pendientes. | `monografia/secciones/04_revision_literatura.tex`, `monografia/referencias.bib` e índice de artículos. Sin compilación ni simulación. |

| A12 | Apartado 5 desarrollado y diseño de Colab concretado: tres distribuciones de igual media, λ = 0,8, m = 1, 40 réplicas, control de inicialización e intervalos entre medias. Referencias analíticas comprobadas sin generar datos aleatorios. Notebook y resultados aún no creados. Lectura del usuario pendiente. | `monografia/secciones/05_metodologia.tex`, `monografia/referencias.bib`, `monografia/main.tex` y sección 5 de `METODOLOGIA_MONOGRAFIA.md`. |

| A13 | Inicio de Metodología simplificado y dos diagramas incorporados por solicitud del usuario: flujo previsto y ventanas apareadas. Se aplicó `thesis-scientific-figures`; parámetros, fórmulas, semillas y umbrales conservados. Comprobación estática aprobada. Lectura e inspección visual pendientes. | `monografia/secciones/05_metodologia.tex`, `monografia/figuras/procedimiento_simulacion.tex` y `monografia/figuras/ventanas_medicion.tex`. Sin compilación ni PDF. |

| A14 | Paleta blanca y morada unificada en los tres diagramas por indicación del usuario. Rellenos `violet!12`, bordes y flechas gris oscuro; descartes grises/discontinuos y tramos no utilizados blancos. Solo se cambiaron los rellenos de los diagramas; contenido y geometría conservados. Criterio registrado para futuros diagramas. Comprobación de fuente aprobada; color renderizado pendiente. | Los tres archivos de `monografia/figuras/` y reglas visuales de `METODOLOGIA_MONOGRAFIA.md`. Sin compilación ni PDF. |

| A15 | El usuario rechazó el cambio de paleta de A14 y solicitó volver al estado anterior. Restaurados bloques blancos en cola y procedimiento y `blue!10` en las ventanas de medición; eliminada la regla de morado obligatorio. A14 queda como antecedente histórico sin vigencia. Seguir `thesis-scientific-figures` sin imponer esa paleta. | Los tres archivos de `monografia/figuras/` y `METODOLOGIA_MONOGRAFIA.md`. Sin compilación ni PDF. |

| A16 | Notebook explicativo en español creado por pedido del usuario para compartir su desarrollo con el docente. Ocho pruebas locales aprobadas y una numérica omitida; sin dependencias científicas locales ni instalaciones. No hay resultados experimentales ni enlace publicado. Pendiente ejecución integral en Colab antes de redactar resultados. | `simulacion/colas_variabilidad_colab.ipynb`, `simulacion/tests/test_notebook.py` y `simulacion/README.md`. Sin PDF. |

| A17 | Usuario ejecutó el notebook anterior, reportó falta de persistencia y pidió color y más gráficos. Aprobó Drive y cuatro figuras. Preservada copia exacta ejecutada y manifiesto SHA-256; nuevo código con autorización interactiva, carpeta exclusiva, guardado incremental y cuatro gráficos (servicios teóricos, espera media, distribución descriptiva de esperas e inicialización). Diez pruebas locales aprobadas y una numérica omitida; verificación independiente sin bloqueantes reproducidos. Nueva ejecución Colab y comprobación visual pendientes. | `simulacion/`, guía y registros; descripción de productos en el apartado 5 actualizada. No PDF ni publicación. |

Añadir los siguientes registros al finalizar cada sección o ante cambios de alcance, indicando archivos y comprobaciones. No registrar como realizada una compilación o revisión visual que esté pendiente.
