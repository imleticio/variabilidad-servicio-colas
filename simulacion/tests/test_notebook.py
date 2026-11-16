"""Pruebas del código real del cuaderno, sin dependencias científicas."""
import copy
import json
import importlib.util
from fractions import Fraction as F
from pathlib import Path
import unittest
import tempfile
import csv


class Persistencia(unittest.TestCase):
    def setUp(self):
        nb = json.loads(RUTA.read_text(encoding='utf-8'))
        celdas = {c['id']: ''.join(c['source']) for c in nb['cells']}
        self.ns = {}
        exec(celdas['persistencia-core'], self.ns)
        self.tmp = tempfile.TemporaryDirectory(dir=RUTA.parent)
        self.addCleanup(self.tmp.cleanup)
        self.raiz = Path(self.tmp.name)

    def test_persistencia_unica_y_csv(self):
        crear = self.ns['crear_ejecucion']
        uno = crear(self.raiz, 'resultados')
        dos = crear(self.raiz, 'resultados')
        self.assertNotEqual(uno, dos)
        agregar = self.ns['agregar_csv']
        agregar(uno, 'replicas.csv', [{'replica': 0, 'estado': 'parcial'}])
        agregar(uno, 'replicas.csv', [{'replica': 1, 'estado': 'parcial'}])
        with (uno/'replicas.csv').open() as archivo:
            self.assertEqual(list(csv.DictReader(archivo)), [
                {'replica': '0', 'estado': 'parcial'}, {'replica': '1', 'estado': 'parcial'}])
        previo = (uno/'replicas.csv').read_bytes()
        agregar(dos, 'replicas.csv', [{'replica': 0}])
        self.assertEqual((uno/'replicas.csv').read_bytes(), previo)

    def test_persistencia_rechaza_rutas_sin_escrituras(self):
        for ruta in ('../escape', '/absoluta', 'a/../b', ''):
            with self.assertRaises(ValueError):
                self.ns['crear_ejecucion'](self.raiz, ruta)
            self.assertEqual(list(self.raiz.iterdir()), [])
        destino = self.ns['crear_ejecucion'](self.raiz, 'resultados')
        for nombre in ('../escape.csv', '/absoluta.csv', 'a/b.csv', ''):
            with self.assertRaises(ValueError):
                self.ns['agregar_csv'](destino, nombre, [{'x': 1}])
        self.assertEqual(list(destino.iterdir()), [])
        (self.raiz/'enlace').symlink_to(self.raiz.parent, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.ns['crear_ejecucion'](self.raiz, 'enlace/escape')
        (destino/'enlace.csv').symlink_to(self.raiz/'externo.csv')
        with self.assertRaises(ValueError):
            self.ns['agregar_csv'](destino, 'enlace.csv', [{'x': 1}])
        self.assertFalse((self.raiz/'externo.csv').exists())

RUTA = Path(__file__).resolve().parents[1] / 'colas_variabilidad_colab.ipynb'


class Cuaderno(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.nb = json.loads(RUTA.read_text(encoding='utf-8'))
        cls.celdas = {c['id']: ''.join(c['source']) for c in cls.nb['cells']}
        cls.ns = {}
        for identificador in ('configuracion', 'nucleo-fcfs'):
            exec(cls.celdas[identificador], cls.ns)

    def test_formato_y_sintaxis(self):
        self.assertEqual((self.nb['nbformat'], self.nb['nbformat_minor']), (4, 5))
        self.assertEqual(len(self.celdas), len(self.nb['cells']))
        for celda in self.nb['cells']:
            if celda['cell_type'] == 'code':
                self.assertEqual(celda['outputs'], [])
                self.assertIsNone(celda['execution_count'])
                compile(''.join(celda['source']), celda['id'], 'exec')

    def test_fcfs_con_espera(self):
        self.assertEqual(self.ns['simular_fcfs']([0, .5, 2], [1, 1, 1]),
                         dict(inicios=[0, 1, 2], salidas=[1, 2, 3],
                              esperas=[0, .5, 0], totales=[1, 1.5, 1]))

    def test_fcfs_sin_espera_e_invariantes(self):
        f = self.ns['simular_fcfs']
        r = f([0, 2, 4], [1, 1, 1])
        self.assertEqual(r['esperas'], [0, 0, 0])
        self.assertEqual(r['salidas'], [1, 3, 5])
        a, s = [0, 0, .5, 9], [0, 2, 3, 1]
        r = f(a, s)
        for i in range(len(a)):
            self.assertGreaterEqual(r['esperas'][i], 0)
            self.assertEqual(r['totales'][i], r['esperas'][i] + s[i])
            self.assertGreaterEqual(r['inicios'][i], a[i])
            if i:
                self.assertGreaterEqual(r['inicios'][i], r['salidas'][i-1])
        self.assertEqual(f([], [])['esperas'], [])

    def test_entradas_rechazadas_sin_mutacion(self):
        for a, s in [([1], []), ([1, 0], [1, 1]), ([-1], [1]),
                     ([0], [-1]), ([float('nan')], [1]),
                     ([0], [float('inf')]), ([float('inf')], [1]),
                     ([1e308, 1e308], [1e308, 1e308])]:
            originales = repr((a, s))
            with self.assertRaisesRegex(ValueError, '.+'):
                self.ns['simular_fcfs'](a, s)
            self.assertEqual(repr((a, s)), originales)

    def test_configuracion_y_ventanas(self):
        c = self.ns['CONFIG']
        self.ns['validar_configuracion'](c)
        self.assertEqual((c['replicas'], c['entidades'], c['semilla']), (40, 140000, 2026))
        self.assertEqual((c['descarte'], c['alternativo'], c['medicion']), (20000, 40000, 100000))
        for clave, valor in [('lambda', 0), ('lambda', 1), ('m', -1),
                             ('m', float('nan')), ('replicas', 1),
                             ('replicas', True), ('entidades', 119999),
                             ('descarte', -1), ('alternativo', 50000),
                             ('medicion', 0), ('semilla', -1)]:
            otro = copy.deepcopy(c)
            otro[clave] = valor
            with self.assertRaisesRegex(ValueError, '.+'):
                self.ns['validar_configuracion'](otro)
        self.assertEqual(c, self.ns['CONFIG'])

    def test_momentos_analiticos(self):
        media = F(4, 5)*F(1, 2) + F(1, 5)*3
        segundo = 2*(F(4, 5)*F(1, 2)**2 + F(1, 5)*9)
        self.assertEqual((media, segundo, segundo-media**2), (1, 4, 3))
        for escenario, esperado in enumerate((2, 4, 8)):
            teoria = self.ns['momentos_teoricos'](escenario, self.ns['CONFIG'])
            self.assertAlmostEqual(teoria['espera_teorica'], esperado)
        with self.assertRaises(ValueError):
            self.ns['momentos_teoricos'](3, self.ns['CONFIG'])

    def test_pruebas_visibles(self):
        exec(self.celdas['verificaciones'], self.ns)

    def test_pruebas_visibles_no_confunden_parametros_editados_con_referencia(self):
        ns = {}
        for identificador in ('configuracion', 'nucleo-fcfs'):
            exec(self.celdas[identificador], ns)
        ns['CONFIG']['lambda'] = 0.4
        exec(self.celdas['verificaciones'], ns)
        self.assertEqual(ns['CONFIG']['lambda'], 0.4)


DEPENDENCIAS = ('numpy', 'pandas', 'matplotlib', 'scipy', 'IPython')
DISPONIBLES = all(importlib.util.find_spec(p) is not None for p in DEPENDENCIAS)


@unittest.skipUnless(DISPONIBLES, 'Faltan dependencias científicas; ejecución numérica pendiente.')
class Numericas(unittest.TestCase):
    def test_generacion_reproducible_y_resumen(self):
        nb = json.loads(RUTA.read_text(encoding='utf-8'))
        celdas = {c['id']: ''.join(c['source']) for c in nb['cells']}
        ns = {}
        for clave in ('importaciones', 'configuracion', 'generacion', 'nucleo-fcfs'):
            exec(celdas[clave], ns)
        # Ejecutar la definición pública, no la llamada al experimento completo.
        import ast
        modulo = ast.parse(celdas['estimacion'])
        funcion = ast.Module(body=[n for n in modulo.body if isinstance(n, ast.FunctionDef)], type_ignores=[])
        exec(compile(funcion, 'estimacion', 'exec'), ns)
        c = dict(ns['CONFIG'], replicas=3, entidades=30, descarte=5, alternativo=10, medicion=20)
        for e in range(3):
            a, s = ns['generar_entradas'](e, 0, c)
            aa, ss = ns['generar_entradas'](e, 0, c)
            ns['np'].testing.assert_array_equal(a, aa)
            ns['np'].testing.assert_array_equal(s, ss)
        filas = [{'escenario_id': e, 'Y': y, 'delta': d}
                 for e in range(3) for y, d in zip((1., 2., 3.), (-.1, 0., .1))]
        resultado = ns['resumir'](ns['pd'].DataFrame(filas), c)
        for _, fila in resultado.iterrows():
            self.assertAlmostEqual(fila['media_espera'], 2)
            self.assertAlmostEqual(fila['varianza_entre_replicas'], 1)
            self.assertAlmostEqual(fila['h_95'], float(ns['t'].ppf(.975, 2))/3**.5)
            self.assertAlmostEqual(fila['media_delta'], 0)
            self.assertAlmostEqual(fila['varianza_delta'], .01)


if __name__ == '__main__':
    unittest.main()
