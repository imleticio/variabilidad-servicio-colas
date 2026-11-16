# Demostración de colas en Google Colab

**Notebook:** `colas_variabilidad_colab.ipynb`, con explicaciones, comentarios y mensajes en español. Implementa el diseño del apartado 5 de la monografía, guarda resultados en Drive y prepara cuatro gráficos a color. No requiere archivos locales del proyecto ni instala paquetes.

La versión anterior ejecutada por el usuario se conserva intacta en `ejecuciones/colas_variabilidad_colab_ejecutado_original.ipynb`, con su SHA-256 en `ejecuciones/original_manifest.json`. La versión nueva se entrega sin salidas: las imágenes anteriores no se presentan como resultado del nuevo código.

## Abrir y ejecutar la nueva versión

1. Entrá a https://colab.research.google.com/ y elegí **Archivo → Subir notebook**. Subí el `.ipynb` actualizado, no la copia original de `ejecuciones/`.
2. Guardá una copia en Drive. Usá un entorno Python con CPU; no hace falta GPU.
3. Elegí **Entorno de ejecución → Ejecutar todas**. En la sección de almacenamiento, Colab te pedirá autorización para montar Drive. Revisá el permiso y autorizá solo si querés conectar ese entorno a tu Drive. El código no concede permisos por vos.
4. Antes del cálculo aparecerá la ruta exclusiva de esta ejecución. Por defecto es:

   ```text
   /content/drive/MyDrive/Monografia_MyS/resultados/<fecha_UTC_y_UUID>/
   ```

   En la interfaz de Google Drive corresponde a **Mi unidad → Monografia_MyS → resultados → carpeta de ejecución**. Si el montaje o la escritura fallan, el experimento no empieza. No hay cambio silencioso a almacenamiento temporal.
5. Esperá a que terminen los tres escenarios, las tablas, las cuatro figuras y la exportación final. El diseño procesa 16 800 000 entidades; la duración depende del entorno. No hace falta cambiar el presupuesto ni reintentar para conseguir diagnósticos favorables.
6. Revisá los archivos en Drive y el campo `estado` de `metadata.json`: debe indicar **`completo; productos exportados`**. Guardá también el notebook con las salidas de esa ejecución.

**Guardar el notebook y guardar sus archivos son acciones diferentes.** Drive conserva ahora los CSV y PNG en una carpeta propia. Para conservar las salidas visibles del notebook, también tenés que guardar tu copia `.ipynb` después de ejecutar.

## Persistencia y ejecuciones parciales

- Cada ejecución crea una carpeta distinta; no se borran ni reutilizan las anteriores.
- Configuración y estado se escriben antes del cálculo. Tras cada réplica se agregan métricas y conteos de distribución a CSV, y se actualiza el progreso.
- Una interrupción puede dejar una réplica sin completar o sus archivos parcialmente escritos. Esos productos no se presentan como un experimento completo. La última réplica confirmada se registra en `metadata.json`.
- Los CSV incrementales conservan una etiqueta `parcial`; la finalización del conjunto se consulta en `metadata.json`, que solo cambia a completo después de exportar todos los productos.
- No hay reanudación automática desde un checkpoint. Para una ejecución nueva, reiniciá el entorno y ejecutá en orden; se creará otra carpeta. No reejecutes solo la simulación o la exportación sobre una carpeta ya utilizada.
- Si rechazás el permiso de Drive, no continúes esperando persistencia. Existe una opción explícita `GUARDAR_EN_DRIVE = False`, pero el modo local es **temporal en Colab** y no es el recomendado para entregar resultados.
- `SUBCARPETA` debe ser relativa a Mi unidad, no vacía y sin `..`. No uses rutas absolutas.

## Cuatro gráficos con funciones distintas

Los escenarios usan azul, terracota y verde, junto con marcas y estilos de línea para distinguirlos también sin color. Fondo blanco y ejes con unidades.

| Archivo | Procedencia y utilidad |
|---|---|
| `servicios.png` | **CDF teóricas** del servicio: misma media, distinta dispersión. El servicio constante tiene un salto en su valor, no una densidad continua. No contiene resultados simulados. |
| `esperas.png` | Medias simuladas e intervalos aproximados del 95 % entre réplicas, frente a referencias analíticas. Es la comparación principal. |
| `distribucion_esperas.png` | Distribución acumulada descriptiva de las esperas de la ventana principal, agregada entre réplicas. Permite examinar diferencias que la media oculta. |
| `inicializacion.png` | Diferencias apareadas entre ventanas, intervalos y tolerancia práctica. No prueba ausencia de sesgo ni estacionariedad. |

La distribución de esperas se representa en **321 umbrales entre 0 y 100 veces el servicio medio**, expresados en minutos. Los conteos en cada umbral son exactos; la curva entre ellos es una representación discretizada, no la ECDF completa. Se informa y exporta la fracción que queda por encima del último umbral, sin forzar que la curva llegue a 1. Las esperas de una trayectoria están correlacionadas: no se calculan intervalos como si cada observación fuera independiente.

Las nuevas figuras no añaden sorteos ni cambian las semillas. La primera es analítica y las otras tres requieren ejecutar el experimento.

## Archivos en cada carpeta

| Archivo | Contenido |
|---|---|
| `config.csv` | Parámetros efectivos. |
| `metadata.json` | Estado, número de réplicas confirmadas, fechas, entorno, versiones, semillas y configuración. |
| `metricas_replicas.csv` | Medias por réplica, momentos empíricos de servicio y configuración; guardado incremental. |
| `cdf_replicas.csv` | Conteos, umbrales y denominadores por réplica; guardado incremental. |
| `summary.csv` | Estimaciones, intervalos, referencias y diagnósticos. |
| `cdf.csv` | Conteos acumulados, denominadores y distribución descriptiva final; incluye masa fuera del rango mostrado. |
| Cuatro archivos `.png` | Las figuras anteriores, a 200 dpi. |

Podés descargar los archivos desde Google Drive. No se descargan ni publican automáticamente, y no se genera PDF.

## Compartir con el docente

Guardá el notebook ejecutado y usá **Compartir** con permiso de **lector**, por correo o mediante enlace según las reglas de la institución. Verificá el acceso con otra cuenta o ventana privada. Si el docente necesita los CSV y PNG, compartí también la carpeta de resultados: compartir el notebook no comparte automáticamente esa carpeta. No hace falta permitir edición.

El agente no inició sesión en Google, conectó Drive ni creó un enlace público. Esas acciones se realizan desde tu cuenta y con tu autorización.

## Diseño científico conservado

- λ = **0,8 entidades/minuto**, servicio medio **1 minuto**, utilización **0,8**.
- Servicio constante, exponencial y H₂: probabilidad 0,8 de exponencial de media 0,5 minutos y probabilidad 0,2 de exponencial de media 3 minutos.
- **40 réplicas de 140 000 entidades por escenario**; semilla maestra **2026**, con flujos separados para llegadas, componente y servicio.
- Ventanas `[20000:120000]` y `[40000:140000]` de la misma trayectoria, sin reiniciar la cola.
- Intervalos aproximados del 95 % entre medias de réplica. Metas diagnósticas: semiamplitud relativa del 5 % y sensibilidad inicial del 2 % de la espera teórica; no son garantías de precisión o convergencia.
- Referencias analíticas **2, 4 y 8 minutos**: no son resultados simulados anticipados.

Las pruebas analíticas usan una configuración fija distinta de la configuración editable del experimento. Si cambiás parámetros, reiniciá y ejecutá todo; actualizá también el informe si cambia su diseño.

## Verificación y límites

Localmente se ejecutaron **11 pruebas: 10 aprobadas y 1 numérica omitida**, por ausencia de NumPy, pandas, Matplotlib, SciPy e IPython. No se instalaron dependencias. Se comprobaron núcleo FCFS, entradas, configuración, teoría, sintaxis, carpetas exclusivas, CSV y rechazo de rutas inseguras. Una verificación independiente no reprodujo bloqueantes en el consentimiento y confinamiento examinados.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s simulacion/tests -v
```

Las pruebas ejecutan el código de las celdas reales; sus archivos temporales se crean y limpian dentro de `simulacion/`.

**Pendiente en la nueva versión:** autorización y escritura reales de Drive, ejecución científica completa, exportaciones y revisión visual de los cuatro gráficos en Colab. La ejecución anterior fue aportada por el usuario y se conserva, pero no comprueba estas funciones nuevas. No redactar resultados nuevos ni afirmar que se guardaron en Drive hasta comprobar esa ejecución.
