# Bibliografía de trabajo

Tema: influencia de la variabilidad de los tiempos de servicio en las esperas de sistemas de colas con un servidor, manteniendo constantes la tasa de llegada y el tiempo medio de servicio.

Esta carpeta reúne cuatro fuentes fundacionales: tres PDF y un capítulo HTML. Además, `articulos/` contiene cuatro artículos académicos seleccionados (incluidas versiones de autor/preprint) y una tesis descargada por un enlace mal identificado, que queda excluida. Consultar `articulos/REFERENCIAS_ARTICULOS.md` para referencias, aportes y limitaciones. Los archivos `.txt` son extracciones auxiliares, no fuentes adicionales. Cada `descargas.json` registra las descargas y sus incidencias.

## 1. Virtamo: teoría M/G/1 — fuente central

- **Referencia provisional:** Virtamo, J. (s. f.). *M/G/1 queue* [Apuntes del curso 38.143 Queueing Theory].
- **Archivo:** `01_virtamo_mg1.pdf`.
- **Texto auxiliar:** `01_virtamo_mg1.txt`.
- **Procedencia:** https://ecs.syr.edu/faculty/fawcett/handouts/CSE681summer/Lecture10/queueNotes/E_lect11.pdf
- **Metadatos comprobados:** el documento identifica a J. Virtamo y el curso. No se confirmó una fecha; no inventarla. Syracuse aloja esta copia, pero eso no prueba que sea la institución autora.
- **Utilidad:** notación M/G/1, carga y estabilidad; derivación de Pollaczek–Khinchine; tiempo residual de servicio; comparación de los casos M/M/1 y M/D/1. Empezar por las páginas 1–7.

## 2. Larson y Odoni: interpretación y aplicación — fuente central

- **Referencia:** Larson, R. C., & Odoni, A. R. (1981). *Urban operations research*. Prentice-Hall. Sección 4.7: “Spatially Distributed Queues and the M/G/1 Queueing System”.
- **Archivo:** `02_larson_odoni_mg1.html`.
- **Capítulo original:** https://web.mit.edu/course/other/urban_or_book/OldFiles/www/book/chapter4/4.7.html
- **Confirmación de autores, editorial y año:** https://web.mit.edu/urban_or_book/www/book/
- **Utilidad:** explica por qué la media del tiempo de servicio no basta para describir la espera; relaciona la varianza con el desempeño; compara servicio general, exponencial y determinista; aporta un ejemplo aplicado.
- **Limitación de la copia local:** el HTML utiliza imágenes externas para varias fórmulas y figuras. No es una copia autónoma completa; consultar el enlace original con conexión para verlas. Para fórmulas utilizables sin conexión, recurrir al PDF de Virtamo.

## 3. Stanford EE384X: fundamentos y contraste — apoyo

- **Referencia provisional:** *EE384X Packet Switch Architectures I: apuntes de teoría de colas* [Diapositivas, archivo H10]. (s. f.). Stanford University.
- **Archivo:** `03_stanford_pollaczek_khinchine.pdf`.
- **Texto auxiliar:** `03_stanford_pollaczek_khinchine.txt`.
- **Procedencia:** https://web.stanford.edu/class/ee384x/EE384X/handouts/H10.pdf
- **Metadatos comprobados:** curso, institución de alojamiento y contenido; no se confirmó autor personal ni fecha. El nombre del archivo local describe su contenido, no constituye un título bibliográfico verificado.
- **Utilidad:** notación de colas, M/M/1, ley de Little, PASTA y explicación de por qué el servicio determinista minimiza la espera bajo los supuestos estudiados. Contiene también material de tiempo discreto que no necesitamos desarrollar.

## 4. Banks, Carson, Nelson y Nicol: análisis de simulación — metodología

- **Referencia provisional:** Banks, J., Carson, J. S., Nelson, B. L., & Nicol, D. M. (s. f.). *Output analysis for a single model* [Diapositivas del capítulo 11 de Discrete-Event System Simulation].
- **Archivo:** `04_nicol_analisis_salidas.pdf`.
- **Texto auxiliar:** `04_nicol_analisis_salidas.txt`.
- **Procedencia:** https://dmnicol.web.engr.illinois.edu/ece541/slides/output-analysis.pdf
- **Metadatos comprobados:** título del capítulo, apellidos de los autores y título del libro en la portada. No se confirmó año ni edición de estas diapositivas. No citarlas como si se hubiera consultado el libro completo.
- **Utilidad:** réplicas, intervalos de confianza, dependencia entre observaciones, condiciones iniciales y análisis de estado estacionario. Sirve para justificar cómo se obtendrían e interpretarían resultados de una demostración computacional.

## Orden de lectura recomendado

1. Virtamo: entender el resultado central y sus supuestos.
2. Larson y Odoni: interpretar el efecto de la variabilidad y sus consecuencias prácticas.
3. Stanford: contrastar conceptos y preparar explicaciones para la defensa.
4. Banks y colaboradores: diseñar y analizar una eventual simulación pequeña.

## Criterios para la futura monografía

- Las fuentes de esta carpeta principal son fundacionales y docentes. Se complementaron con cuatro artículos en `articulos/`; el conjunto es una selección acotada, no una revisión exhaustiva del estado del arte. Antes de redactar conclusiones, leer críticamente los artículos y respetar las diferencias de modelo, métrica y versión indicadas en su índice.
- No confundir tiempo de espera en cola con tiempo total en el sistema.
- Comparar distribuciones con igual media, igual tasa de llegada y la misma disciplina de atención.
- Explicitar llegadas Poisson, un servidor, atención FCFS, independencia y condiciones de estabilidad y momentos finitos requeridos por la fórmula de espera media.
- No generalizar el resultado a cualquier sistema de colas o a cualquier indicador de desempeño.
- No presentar un ejemplo hipotético como datos de un sistema real, ni resultados analíticos como resultados de simulaciones ejecutadas.
- No agregar referencias a partir de bibliografías de terceros sin consultar los documentos correspondientes.

## Enlace no disponible

El intento de descargar *A Practical Introduction to Analysis of Simulation Output Data* desde una copia de TU Delft devolvió HTTP 404. El enlace está registrado en `descargas.json`. No se descargó el documento y no debe figurar como fuente consultada a partir de esta carpeta.
