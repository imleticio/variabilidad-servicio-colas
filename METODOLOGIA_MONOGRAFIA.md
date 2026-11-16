# Forma de trabajo para la monografía

La monografía se redactará en español y en **LaTeX**, utilizando `thesis-writing` para la estructura, la redacción y la revisión, y `thesis-scientific-figures` para diagramas y figuras científicas cuando sean necesarios. **No se compilará ni se generará ningún PDF hasta que el usuario lo indique expresamente**, incluidas las figuras por separado.

Este archivo registra la forma de trabajo acordada. Su creación no inicia la redacción de la monografía: se esperará la indicación del usuario para comenzar.

## Contexto y prioridad de instrucciones

- **Materia:** Modelos y Simulación, Trabajo Final Integrador 2026.
- **Modalidad:** monografía de investigación, no tesis experimental completa.
- **Tema elegido:** influencia de la variabilidad de los tiempos de servicio en los sistemas de colas.
- **Pregunta de trabajo:** ¿cómo afecta la variabilidad de los tiempos de servicio al tiempo medio de espera cuando se mantienen constantes la tasa de llegada y el tiempo medio de atención?
- **Alcance inicial:** comparación de colas con un servidor, con énfasis en M/D/1, M/M/1 y M/G/1, explicitando supuestos y límites de aplicación.
- La consigna institucional de `Trabajo Final Integrador MyS2026 (1).pdf` tiene prioridad sobre las estructuras genéricas de las skills. Los demás grupos orientan la elección del tema, pero no reemplazan la consigna.

## 1. `thesis-writing`: redacción y revisión en LaTeX

**Skill:** `/Users/leonel/.agents/skills/thesis-writing/SKILL.md`.

### Uso previsto

1. Delimitar objetivos, pregunta de investigación y alcance antes de desarrollar las secciones.
2. Organizar el texto según la consigna: título e integrantes, resumen, introducción, objetivos, desarrollo y metodología, resultados cuando correspondan, discusión, conclusiones y referencias.
3. Integrar marco conceptual, comparación de la literatura y análisis crítico, sin convertir la revisión en una sucesión de resúmenes por autor.
4. Redactar con una secuencia clara de afirmación, evidencia e interpretación. Justificar las decisiones metodológicas y responder a los objetivos en las conclusiones.
5. Revisar tanto la precisión de cada párrafo como la coherencia entre secciones. Separar resultados propios de su interpretación cuando exista un experimento.

### Archivos y evidencia

- La redacción se guardará en archivos editables `.tex`; la bibliografía estructurada, en `.bib` cuando se prepare el sistema de citas.
- Antes de crear el documento raíz o su preámbulo, comprobar si existe una plantilla institucional o una estructura previa. El documento raíz es `monografia/main.tex`, creado por pedido del usuario para compilar desde VS Code. Incluye los apartados disponibles y usa BibTeX con estilo numérico `unsrt`. No se ha comprobado su compilación.
- Mantener español académico, notación consistente y referencias cruzadas mediante `\label` y `\ref` cuando corresponda.
- Usar claves de cita verificables. Si falta evidencia o un dato bibliográfico, señalar el pendiente; nunca inventar una cita para completar el texto.
- Consultar los apoyos `structure.md`, `writing-guide.md` y `review-checklist.md` de la skill al abordar estructura, redacción y revisión, respectivamente.
- No trasladar requisitos propios de tesis empíricas o doctorales a esta monografía si la consigna no los exige.

## 2. `thesis-scientific-figures`: diagramas cuando aporten claridad

**Skill:** `/Users/leonel/.agents/skills/thesis-scientific-figures/SKILL.md`.

### Elección del recurso

| Necesidad | Recurso |
|---|---|
| Representar llegadas, cola, servidor y salida; explicar un procedimiento | Diagrama conceptual editable en TikZ |
| Mostrar curvas o comparar cantidades | PGFPlots o gráficos originales con datos y generación trazables |
| Comunicar valores exactos | Tabla en LaTeX |
| Ilustrar un concepto sin datos observados | Esquema identificado explícitamente como conceptual o hipotético |

**Regla obligatoria para todos los agentes:** todos los diagramas de la monografía, tanto nuevos como modificados, deben elaborarse siguiendo `thesis-scientific-figures` y sus referencias. No es una recomendación opcional. En cada delegación que incluya diagramas, indicar la ruta de la skill y exigir su lectura y aplicación. Usar TikZ por sí solo no acredita el cumplimiento: también deben respetarse las reglas científicas, visuales y de verificación de la skill. La compilación y la inspección del renderizado continúan diferidas hasta autorización del usuario.

No se añadirán diagramas por decoración. Cada figura tendrá un propósito explicativo y deberá estar vinculada con el texto.

### Reglas científicas y visuales

- Leer primero el apartado correspondiente, sus fuentes y, si existe, el código del experimento.
- Conservar notación, idioma y tipografía del documento. Diferenciar tiempo de espera en cola y tiempo total en el sistema.
- Mantener fuentes editables, rótulos legibles, fondo blanco, trazos finos neutros, flechas simples y colores discretos comprensibles también en escala de grises.
- Ajustar la composición al ancho del texto; reorganizar o dividir una figura antes de reducir excesivamente los rótulos.
- Añadir título o leyenda, etiqueta de referencia y procedencia: elaboración propia, adaptación de una fuente o resultados de un experimento identificado, según corresponda.
- No inventar datos, resultados, probabilidades ni simulaciones ejecutadas. No presentar valores analíticos como mediciones o resultados simulados.
- Aplicar la guía `references/scientific-figures-guide.md`. El archivo `assets/architecture-reference.tex` es únicamente una referencia visual histórica: no copiar su contenido de redes neuronales al tema de colas.

## 3. Restricción vigente: solo fuentes, sin PDF

Hasta una nueva indicación explícita del usuario:

- Se permite redactar y editar fuentes LaTeX, bibliografía y figuras editables cuando se autorice comenzar la monografía.
- Se permiten revisiones de texto, fórmulas, citas, referencias y estructura del código fuente.
- **No se ejecutarán motores ni herramientas de compilación o conversión a PDF**, tampoco para pruebas de figuras, vistas previas o compilaciones automáticas.
- Los PDF bibliográficos ya descargados pueden consultarse: la restricción corresponde a generar o compilar nuevos PDF del trabajo y de sus figuras.
- La compilación independiente de figuras, la compilación integrada y la inspección del resultado renderizado previstas por la skill de figuras quedan **diferidas**, no omitidas ni aprobadas.
- No se afirmará que el documento compila, que cumple una paginación final o que una figura está visualmente validada mientras no se hayan realizado esas comprobaciones.

Cuando el usuario autorice generar el PDF, se comprobarán dependencias, compilación, referencias, ancho de figuras y aspecto real de las páginas, corrigiendo los problemas encontrados.

## 4. Fuentes disponibles y límites de interpretación

Consultar estos índices antes de redactar:

- `bibliografia/REFERENCIAS.md`: fuentes fundacionales y metodología.
- `bibliografia/articulos/REFERENCIAS_ARTICULOS.md`: artículos seleccionados, versiones consultadas y limitaciones.

Trabajar sobre el contenido de los documentos, no solo sus títulos o resúmenes. Distinguir apuntes, libros, artículos publicados, manuscritos y preprints. No citar la tesis de Pearce como un artículo de Kingman.

La comparación principal mantendrá constantes la tasa de llegada y la media de servicio. Los trabajos sobre redes cerradas, reinicios, disciplinas LCFS o máximos de cola podrán apoyar la discusión, pero no deben confundirse con resultados sobre espera media en una cola M/G/1 FCFS.

## 5. Demostración computacional: Google Colab

**Decisión acordada con el usuario:** la demostración se desarrollará en Python dentro de un único notebook `.ipynb` compatible con Google Colab. Colab será el entorno de ejecución previsto; el informe continuará redactándose en LaTeX.

- Mantener la modalidad de **monografía de investigación**: la simulación es una demostración complementaria de la teoría, no una aplicación completa ni un estudio de un servicio real.
- Utilizar NumPy, pandas y Matplotlib, con SciPy únicamente para el cuantil de Student de los intervalos, y un simulador pequeño de eventos discretos propio, entendible y reproducible. No exigir Arena, una aplicación con interfaz ni instalaciones locales para el uso previsto en Colab.
- Representar una cola con un servidor y disciplina FCFS. Mantener constantes la tasa de llegada y la media de servicio.
- Comparar servicio constante, exponencial y una mezcla hiperexponencial H₂: con probabilidad 0,8, exponencial de media m/2; con probabilidad 0,2, exponencial de media 3m. Las tres distribuciones tienen media m, con coeficientes de variación al cuadrado 0, 1 y 3, respectivamente. La mezcla es un diseño hipotético propio, no una distribución ajustada a un servicio real.
- Calcular esperas medias y contrastarlas con Pollaczek–Khinchine; realizar réplicas y evaluar la incertidumbre estadística.
- Incluir explicaciones, parámetros, semillas, código, tablas y gráficos trazables en el notebook; conservarlo como archivo complementario del trabajo.
- Identificar los parámetros como hipotéticos. No requerir datos de una empresa ni afirmar validación de un sistema real.
- No presentar resultados hasta ejecutar y comprobar el experimento. Diferenciar comprobaciones locales, si las hubiera, de una ejecución efectivamente verificada en Colab.
- Diseño previsto en `monografia/secciones/05_metodologia.tex`: λ = 0,8 entidades/minuto, m = 1 minuto y ρ = 0,8; 40 réplicas por escenario, 140 000 entidades por réplica, descarte principal de 20 000 y medición de las siguientes 100 000. No reiniciar la cola al comenzar la medición.
- Control de inicialización apareado sobre la misma realización: descarte alternativo de 40 000 y medición de las siguientes 100 000. Evaluar diferencias entre ventanas con un intervalo aproximado y un umbral práctico del 2 % de la espera analítica. Es un diagnóstico, no prueba de ausencia de sesgo compartido.
- Intervalos aproximados del 95 % calculados entre medias de réplica, no suponiendo independientes las esperas consecutivas. Meta diagnóstica de semiamplitud relativa del 5 %; si no se alcanza con el presupuesto fijado, informar la limitación, sin reintentos automáticos ilimitados.
- Semilla maestra 2026; derivar flujos reproducibles con `SeedSequence([2026, escenario, replica])` y `spawn` para llegadas, elección de componente y servicio. No compartir flujos entre escenarios; aparear solo las ventanas del diagnóstico dentro de una realización.
- El notebook está creado en `simulacion/colas_variabilidad_colab.ipynb`, con explicaciones, comentarios y mensajes en español. `simulacion/README.md` indica cómo abrirlo, ejecutarlo, guardar salidas y compartir una copia de lectura. El usuario ejecutó la versión anterior; su archivo con salidas se conserva intacto en `simulacion/ejecuciones/colas_variabilidad_colab_ejecutado_original.ipynb`, con SHA-256 registrado. La versión ampliada se entrega sin salidas y requiere una ejecución nueva para comprobar Drive y cuatro gráficos. Diez pruebas locales aprobadas y una numérica omitida por dependencias ausentes; revisión independiente de consentimiento y límites de escritura sin bloqueantes reproducidos. No equivalen a una ejecución completa en Colab. Los presupuestos y umbrales siguen pendientes de evaluación, no son precisión demostrada.
- Por aprobación del usuario, el almacenamiento predeterminado será Drive, con permiso interactivo de Colab, subcarpeta `Monografia_MyS/resultados` y carpeta exclusiva por ejecución, sin sobrescribir ejecuciones anteriores. Registrar configuración y estado antes de calcular y CSV por réplica; indicar datos parciales hasta la exportación final. Guardar el notebook no sustituye guardar sus archivos. No publicar, descargar ni compartir automáticamente.
- Preparar cuatro gráficos científicos con colores discretos por escenario (azul, terracota y verde), marcas y estilos distinguibles sin color: CDF teóricas de servicio, espera media con IC y teoría, CDF descriptiva de esperas y diagnóstico de inicialización. Esta decisión no modifica la paleta vigente de los diagramas TikZ. Para la CDF de esperas, acumular conteos de la ventana principal en 321 umbrales de 0 a 100m, informar el denominador y la masa que excede ese rango; no fingir independencia entre observaciones ni una ECDF completa.
- No exportar gráficos ni el notebook a PDF por iniciativa del agente: sigue vigente la restricción de generación de PDF.

## 6. Claridad visual del procedimiento

Por indicación del usuario, el inicio del apartado 5 debe ser breve y centrarse en el enfoque del trabajo, no en incidencias de búsqueda o descarga. Los límites de lectura de fuentes se conservan en la revisión de literatura y el índice bibliográfico.

Dos diagramas elaborados con `thesis-scientific-figures` complementan el método y se incluyen desde `monografia/secciones/05_metodologia.tex`:

- `monografia/figuras/procedimiento_simulacion.tex`: flujo previsto de configuración, generación, simulación FCFS, medición, resumen entre réplicas y contraste analítico. Representa el flujo científico, no una arquitectura desplegada; el notebook implementa ahora ese procedimiento.
- `monografia/figuras/ventanas_medicion.tex`: escala común de índices de entidad para las ventanas principal y alternativa de una misma realización; mediciones de 100 000 entidades con 80 000 de solapamiento, sin reiniciar la cola. El eje no representa minutos.

Ambos son fuentes TikZ editables, con leyendas de elaboración propia y diseño previsto. No se añadieron bibliotecas adicionales ni se modificó el diseño experimental. Las conexiones y proporciones fueron comprobadas en fuente; compilación, ajuste tipográfico y aceptación visual permanecen diferidos. Los gráficos de resultados solo se elaborarán a partir de experimentos efectivamente ejecutados.

## Próximo paso

La redacción se inició por indicación del usuario con la introducción, guardada en `monografia/secciones/01_introduccion.tex`. Consultar `AVANCE_MONOGRAFIA.md` para el estado vigente y las secciones pendientes. La sección de objetivos está redactada en `monografia/secciones/02_objetivos.tex` e incluida en el documento raíz. El marco conceptual está redactado en `monografia/secciones/03_marco_conceptual.tex`, con un diagrama TikZ en `monografia/figuras/cola_un_servidor.tex`; ambos están incluidos en el documento principal. La compilación y comprobación visual no fueron ejecutadas por el agente. La revisión de la literatura está redactada en `monografia/secciones/04_revision_literatura.tex` e incluida en el documento principal; el alcance real de lectura se registra en el índice de artículos. La metodología está redactada en `monografia/secciones/05_metodologia.tex` e incluida en el documento principal, con el diseño prospectivo resumido en la sección 5 de este archivo. Continuar una sección por vez; el siguiente apartado previsto es Demostración y resultados. El notebook ya fue implementado y su núcleo fue probado localmente, pero falta ejecutar en Colab la versión ampliada, autorizar y comprobar Drive, revisar los cuatro gráficos y conservar sus salidas antes de redactar resultados. La ejecución original aportada no demuestra las funciones nuevas. La publicación del enlace de lectura la realizará el usuario desde su copia de Drive; el agente no subió ni compartió archivos. Mantener la prohibición de generar PDF hasta una autorización posterior específica.
