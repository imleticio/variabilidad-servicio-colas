# Artículos académicos para la monografía

Se descargaron cuatro artículos pertinentes. Para redactar la revisión de literatura se leyeron las secciones sustantivas de Joustra, Lauber Bonomo y colaboradores, y Koole y colaboradores; de Bondi y Whitt solo se consultaron el resumen y el comienzo de la introducción de la primera página. El alcance de cada lectura se registra debajo; no se afirma una revisión exhaustiva del campo. Tres PDF tienen texto extraíble; el de Bondi y Whitt es un escaneo y requiere lectura visual u OCR.

## Lecturas para la sección 4

- **Joustra y colaboradores:** secciones 1–5 y apéndices 1–2, páginas 448–463 antes de las referencias. Se analizaron la combinación teoría–simulación y la diferencia entre variabilidad de capacidad y de duración.
- **Lauber Bonomo y colaboradores:** secciones I–VII y apéndice A, páginas 1–13 del preprint v1. Se distinguió su tiempo desde llegada hasta fin de servicio de nuestra espera en cola, y el efecto conjunto del reinicio sobre media y dispersión.
- **Koole y colaboradores:** secciones 1–5, páginas 1–12 antes de las referencias. Se distinguieron orden convexo y comparación de varianzas, máximos y medias, disciplinas LCFS y FCFS, teoremas y conjeturas.
- **Bondi y Whitt:** página 219 únicamente, mediante `09_portada.png`. Uso limitado a los principios anunciados para redes cerradas; demostraciones y resultados detallados no revisados.

**Texto resultante:** `../../monografia/secciones/04_revision_literatura.tex`. No se ejecutaron simulaciones propias al realizar esta lectura.

## 1. Joustra y colaboradores — aplicación con teoría de colas y simulación

**Referencia:** Joustra, P. E., Kolfin, R., van Dijk, N. M., Koning, C. C. E., & Bakker, P. J. M. (2012). Reduce fluctuations in capacity to improve the accessibility of radiotherapy treatment cost-effectively. *Flexible Services and Manufacturing Journal, 24*, 448–464. https://doi.org/10.1007/s10696-011-9119-y

- **PDF:** `05_joustra_et_al_2012_radioterapia.pdf` (17 páginas).
- **Texto:** `05_joustra_et_al_2012_radioterapia.txt`.
- **Descarga:** https://ris.utwente.nl/ws/files/6473255/2012-XJoustraKolfinDijkKoningBakker.pdf
- **Comprobación:** autores, título, revista, páginas y DOI aparecen en la portada. Publicado en línea en 2011; el volumen corresponde a 2012.
- **Aporte:** ejemplo real de combinación de teoría de colas y simulación de eventos discretos para estudiar un proceso de radioterapia. Incluye fundamentos sobre variabilidad y esperas en un apéndice.
- **Límite:** su intervención principal reduce fluctuaciones de capacidad en un proceso de varias etapas. No presentarlo como un experimento que mantiene constantes todos los factores salvo la varianza del tiempo de servicio.

## 2. Lauber Bonomo, Pal y Reuveni — variabilidad y reinicio del servicio

**Versión efectivamente descargada:** Lauber Bonomo, O., Pal, A., & Reuveni, S. (2021). *Mitigating long queues and waiting times with service resetting* [Preprint, arXiv:2111.02097v1]. https://arxiv.org/abs/2111.02097

- **PDF:** `08_bonomo_pal_reuveni_service_resetting_arxiv.pdf`.
- **Texto:** `08_bonomo_pal_reuveni_service_resetting_arxiv.txt`.
- **Descarga:** https://arxiv.org/pdf/2111.02097
- **Comprobación:** el PDF descargado identifica arXiv:2111.02097v1, envío del 3 de noviembre de 2021; la cabecera interna está fechada el 4 de noviembre de 2021. Se verificaron título, tres autores y planteamiento M/G/1.
- **Publicación posterior identificada:** *PNAS Nexus* (2022), 1(3), pgac070; DOI https://doi.org/10.1093/pnasnexus/pgac070 . No confundir el preprint local con el PDF editorial, cuya descarga devolvió HTTP 403. Para atribuir detalles a la versión publicada, cotejar primero esa versión.
- **Aporte:** relación entre fluctuaciones del servicio y congestión; analiza cuándo reiniciar servicios puede reducir la media y la variabilidad del tiempo efectivo de atención.
- **Límite:** el reinicio modifica el mecanismo de servicio y puede modificar también su media. Es una extensión para la discusión, no una comparación controlada de distribuciones con igual media.

## 3. Bondi y Whitt — variabilidad en redes cerradas

**Referencia:** Bondi, A. B., & Whitt, W. (1986). The influence of service-time variability in a closed network of queues. *Performance Evaluation, 6*, 219–234.

- **PDF:** `09_bondi_whitt_1986_service_time_variability.pdf` (16 páginas).
- **Vista de portada comprobada:** `09_portada.png`.
- **Descarga:** https://www.columbia.edu/~ww2040/Bondi1986.pdf
- **Comprobación:** título, autores, revista, volumen, año y páginas verificados visualmente en la primera página del escaneo. No se confirmó DOI.
- **Formato:** PDF escaneado. El `.txt` generado está vacío o casi vacío y NO representa una extracción utilizable. El registro de descarga distingue este caso de un PDF fallido.
- **Aporte:** permite discutir por qué los efectos de la variabilidad dependen de la estructura del sistema: estudia redes cerradas con servidores FCFS y una clase de trabajos.
- **Límite:** no es una cola abierta M/G/1 aislada; no trasladar sus resultados directamente a la comparación principal. Usarlo como contraste y delimitación, no como base de los cálculos del ejemplo.

## 4. Koole, Nuyens y Righter — límites de la generalización

**Referencia de la versión descargada:** Koole, G., Nuyens, M., & Righter, R. (2005). *The effect of service time variability on maximum queue lengths in M^X/G/1 queues* [Manuscrito de autores, fechado el 29 de abril de 2005].

- **PDF:** `10_variabilidad_maximo_cola_2005.pdf`.
- **Texto:** `10_variabilidad_maximo_cola_2005.txt`.
- **Descarga:** https://www.math.vu.nl/~koole/publications/2005jap/art.pdf
- **Comprobación:** título, autores y fecha en la primera página. No se agregan revista, paginación editorial ni DOI sin cotejar el registro publicado.
- **Aporte:** estudia el máximo de longitud de cola durante un período ocupado en colas con llegadas por lotes y disciplinas LCFS con interrupción. Muestra que, en ese contexto, mayor variabilidad puede producir máximos de cola estocásticamente menores.
- **Límite esencial:** NO contradice el resultado sobre espera media en M/G/1 FCFS a media fija. Cambian la disciplina, el modelo y la variable de desempeño. Es útil para explicar por qué “más variabilidad siempre empeora cualquier cola” sería una conclusión incorrecta.

## Cómo usarlos sin ampliar demasiado el trabajo

- **Marco teórico y comparación principal:** los apuntes de Virtamo y el capítulo de Larson y Odoni que están en la carpeta superior.
- **Aplicación:** Joustra y colaboradores, explicando las diferencias respecto del modelo del ejemplo.
- **Extensión:** Lauber Bonomo y colaboradores; describir brevemente el reinicio, sin implementar ni prometer reproducir su estudio.
- **Discusión crítica y alcance:** Bondi–Whitt y Koole–Nuyens–Righter permiten mostrar qué cambia cuando cambian la red, la disciplina o la métrica.
- No es necesario desarrollar toda la matemática de los cuatro artículos. La prioridad sigue siendo la pregunta acotada sobre espera media con igual tasa de llegada e igual media de servicio.

## Incidencias y exclusiones

1. El enlace de Oxford al PDF publicado de Lauber Bonomo y colaboradores devolvió **HTTP 403**. Se descargó una versión pública de arXiv, claramente identificada como preprint.
2. El enlace del repositorio ANU presentado inicialmente como Kingman (1961) devolvió en realidad **Moving Average Processes in Queueing Theory**, tesis doctoral de **C. E. M. Pearce (1965)**, de 193 páginas. Se conservó como `07_pearce_1965_tesis_NO_KINGMAN.pdf` y se excluye de la selección. **El artículo de Kingman no se descargó.**
3. El PDF de Bondi–Whitt pasó la validación de formato, pero no la extracción automática de texto por ser un escaneo. La inspección visual de portada confirmó su identidad y permitió leer resumen y comienzo de la introducción; no se afirma haber leído íntegramente el artículo.
4. `descargas.json` conserva los resultados técnicos y la corrección de identidad. Una descarga técnicamente exitosa no garantiza que la referencia sea correcta; la identificación se cotejó con los documentos.
