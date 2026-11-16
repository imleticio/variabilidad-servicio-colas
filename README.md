# Variabilidad del servicio y espera en sistemas de colas

Monografía y simulación reproducible sobre la **influencia de la variabilidad de los tiempos de servicio en la espera media de una cola M/G/1**. Trabajo académico para la asignatura **Modelos y Simulación — UCASAL, 2026**, con documento en LaTeX y desarrollo computacional explicado en español en Google Colab.

La comparación mantiene constantes la tasa de llegada y el tiempo medio de servicio, y modifica la variabilidad del servicio. Se busca comprender por qué dos sistemas con igual utilización pueden presentar esperas medias diferentes.

## Ejecutar la demostración

1. Descargá el notebook [`simulacion/colas_variabilidad_colab.ipynb`](simulacion/colas_variabilidad_colab.ipynb).
2. Abrí [Google Colab](https://colab.research.google.com/) y seleccioná **Archivo → Subir notebook**.
3. Guardá una copia en Drive y elegí **Entorno de ejecución → Ejecutar todas**. Al llegar a la conexión con Drive, revisá y autorizá el permiso si querés utilizar el almacenamiento persistente.
4. Esperá a que finalicen los tres escenarios y la exportación. Revisá las tablas, los cuatro gráficos y el estado final de `metadata.json`.

No se necesita GPU ni instalar Python localmente. El notebook utiliza NumPy, pandas, Matplotlib, SciPy e IPython, y no instala paquetes automáticamente.

**Guía detallada:** [`simulacion/README.md`](simulacion/README.md), con instrucciones de almacenamiento, descarga, interpretación de ejecuciones parciales y compartición con el docente.

## Modelo y pregunta de estudio

Se considera un sistema con llegadas Poisson, un servidor, atención por orden de llegada (**FCFS**) y servicios independientes e idénticamente distribuidos dentro de cada escenario. Los parámetros son hipotéticos; no provienen de una empresa ni representan la validación de un servicio real.

- Tasa de llegada: **λ = 0,8 entidades/minuto**.
- Tiempo medio de servicio: **E[S] = 1 minuto**.
- Utilización: **ρ = λ E[S] = 0,8**.
- Variable principal: **Wq**, tiempo de espera en cola antes de comenzar el servicio; no incluye el tiempo de atención.

La fórmula de Pollaczek–Khinchine proporciona la referencia analítica, bajo los supuestos del modelo y con segundo momento de servicio finito:

$$
E[W_q] = \frac{\lambda E[S^2]}{2(1-\rho)}, \qquad \rho < 1.
$$

Como se mantiene fija la media, aumentar la varianza del servicio aumenta su segundo momento y, en este modelo, la espera media teórica.

| Escenario | Distribución del servicio | Media (min) | Varianza (min²) | Espera media teórica (min) |
|---|---|---:|---:|---:|
| M/D/1 | Constante | 1 | 0 | 2 |
| M/M/1 | Exponencial | 1 | 1 | 4 |
| M/H₂/1 | Mezcla de dos exponenciales | 1 | 3 | 8 |

La mezcla H₂ elige, con probabilidad **0,8**, una exponencial de **media 0,5 minutos** y, con probabilidad **0,2**, una exponencial de **media 3 minutos**. Esas cifras son medias de componentes, no tasas.

**Los valores 2, 4 y 8 son referencias teóricas, no resultados simulados.** No se extrapola esta relación a cualquier red de colas o disciplina de atención.

## Diseño de la simulación

El notebook implementa la evolución cronológica de una cola FCFS y sigue cada entidad hasta completar su servicio.

| Elemento | Configuración |
|---|---|
| Réplicas | 40 independientes por escenario |
| Entidades | 140 000 por réplica; 16 800 000 en total |
| Ventana principal | Descartar las primeras 20 000 y medir las siguientes 100 000 |
| Ventana alternativa | Descartar las primeras 40 000 y medir las siguientes 100 000 de la misma trayectoria |
| Inicialización | Sistema vacío; sin reiniciar la cola al comenzar una ventana |
| Semilla maestra | 2026, con flujos separados por escenario, réplica y tipo de generación |
| Incertidumbre | Intervalos aproximados del 95 % de Student entre medias de réplica |

Las ventanas se superponen y su comparación es **apareada**. No se consideran independientes las esperas sucesivas de una trayectoria. Los diagnósticos de precisión y sensibilidad inicial pueden resultar desfavorables: se informan como limitaciones, sin repetir automáticamente hasta obtener una salida conveniente.

## Gráficos y archivos de resultados

Se preparan cuatro figuras con colores consistentes por escenario y marcas o estilos que también permitan distinguirlos sin color:

| Figura | Qué muestra |
|---|---|
| `servicios.png` | Distribuciones acumuladas **teóricas** del servicio, incluido el salto del servicio constante. |
| `esperas.png` | Espera media simulada e intervalos frente a las referencias analíticas. |
| `distribucion_esperas.png` | Distribución acumulada descriptiva de las esperas medidas; permite examinar diferencias que el promedio oculta. |
| `inicializacion.png` | Sensibilidad al descarte inicial mediante diferencias apareadas e intervalos. |

La distribución de esperas se representa en una grilla finita; el notebook informa la masa que excede el rango mostrado. No se presenta como una ECDF completa ni se calculan intervalos suponiendo independientes todas las observaciones.

Con Drive autorizado, los productos se guardan en una carpeta exclusiva por ejecución:

```text
Mi unidad/Monografia_MyS/resultados/<identificador_de_ejecucion>/
```

Se conservan configuración, versiones, semillas, métricas por réplica, conteos de distribución, tablas resumen y los cuatro PNG. Hay guardado incremental; una interrupción deja datos identificados como parciales. El conjunto solo se marca completo después de terminar la exportación.

**Guardar el notebook no equivale a guardar o compartir su carpeta de resultados.** Para entregar el trabajo, guardá también la copia ejecutada con sus salidas y verificá los permisos de lectura de cada recurso que compartas.

## Estructura del proyecto

```text
.
├── monografia/
│   ├── main.tex                 # Documento principal
│   ├── secciones/               # Desarrollo por apartados
│   ├── figuras/                 # Diagramas científicos editables en TikZ
│   └── referencias.bib          # Referencias bibliográficas
├── simulacion/
│   ├── colas_variabilidad_colab.ipynb
│   ├── README.md                # Guía de ejecución y resultados
│   ├── tests/                  # Pruebas del código del notebook
│   └── ejecuciones/            # Copia preservada de la ejecución anterior
├── bibliografia/               # Material de consulta e índices de fuentes
├── AVANCE_MONOGRAFIA.md         # Estado y decisiones del trabajo
└── METODOLOGIA_MONOGRAFIA.md    # Criterios y acuerdos metodológicos
```

Para leer el informe, comenzá por [`monografia/main.tex`](monografia/main.tex). El desarrollo se realiza por secciones; los archivos de avance documentan qué está terminado y qué falta. No se generan ni compilan PDF automáticamente desde el notebook.

## Verificación y estado actual

La versión anterior ejecutada por el usuario se conserva por separado. La versión ampliada incorpora persistencia en Drive y cuatro figuras, pero **su ejecución completa, las escrituras reales en Drive y la inspección visual de los nuevos gráficos siguen pendientes de comprobación**. El apartado de resultados de la monografía todavía no está desarrollado.

La última comprobación local registró **10 pruebas aprobadas y 1 prueba numérica omitida** por falta de dependencias científicas. Comprueba el núcleo FCFS, casos conocidos, entradas inválidas, teoría, sintaxis y funciones de almacenamiento. No sustituye ejecutar todo el notebook en Colab.

Para repetir las pruebas desde la raíz del proyecto:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s simulacion/tests -v
```

Las pruebas numéricas requieren las dependencias científicas; su omisión no equivale a una aprobación. El estado detallado se encuentra en [`AVANCE_MONOGRAFIA.md`](AVANCE_MONOGRAFIA.md).

## Fuentes y alcance académico

Las referencias se registran en [`monografia/referencias.bib`](monografia/referencias.bib), el [índice bibliográfico](bibliografia/REFERENCIAS.md) y el [índice de artículos](bibliografia/articulos/REFERENCIAS_ARTICULOS.md), con las limitaciones de lectura o acceso correspondientes.

Los documentos bibliográficos y materiales de la asignatura conservan los derechos de sus respectivos titulares. Antes de publicar copias de terceros, corresponde comprobar sus condiciones de redistribución; su inclusión en la carpeta de trabajo no otorga permiso para publicarlas.
