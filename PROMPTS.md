# Bitácora de Co-programación con IA

Este documento registra el uso ético y educativo de herramientas de Inteligencia Artificial durante el desarrollo del Hito 1 del proyecto TI-Metrics.

## Registro de Prompt # 1

* **Fecha:** 2026-10-18
* **Módulo/Función:** Configuración del entorno (Git/PowerShell)
* **Prompt Enviado:** "Estoy configurando el repositorio en Windows usando PowerShell. Al intentar crear los archivos base con el comando 'touch', el sistema lanza un error de comando no encontrado. ¿Cuál es la mejor práctica para crear estos archivos en este entorno sin perder la estructura que pide la guía?"
* **Respuesta de la IA:** La IA explicó que PowerShell no tiene el binario `touch` nativo de Unix y sugirió usar Git Bash o el cmdlet nativo `New-Item -ItemType File`.
* **Análisis Crítico:** Aunque la IA sugirió Git Bash, preferí usar `New-Item` en PowerShell para mantener la consistencia en mi entorno de trabajo en VS Code. Además, la IA me advirtió sobre el nuevo sistema de autenticación de GitHub (Tokens), lo cual evité configurando el inicio de sesión por navegador integrado en VS Code.
* **Solución Final Aplicada:** Se utilizó `New-Item` para crear los archivos del proyecto y se autenticó Git mediante el flujo OAuth del navegador.

## Registro de Prompt # 2

* **Fecha:** 2026-10-19
* **Módulo/Función:** src/parsers/csv_parser.py
* **Prompt Enviado:** "Necesito implementar la ingesta de un archivo logs.csv. Quiero usar la clase `csv.DictReader` por su eficiencia, pero necesito deduplicar los registros de manera óptima en memoria y manejar el caso en que el archivo no exista. ¿Cuál sería la estructura de clase más eficiente usando estructuras de datos de Python?"
* **Respuesta de la IA:** La IA propuso una clase que abre el archivo en un bloque `try...except FileNotFoundError`. Para la deduplicación, sugirió convertir cada fila a una tupla y agregarla a un `set`.
* **Análisis Crítico:** La solución con `set` fue acertada para el rendimiento (búsquedas en tiempo O(1)). Sin embargo, el código de la IA devolvía el set de tuplas, lo cual no era compatible con el resto de mi arquitectura. Tuve que refactorizar el retorno para que añadiera el diccionario original a una lista final si no estaba duplicado. Además, adapté las llaves a las columnas reales de mi CSV (`path`, `memory_percent`).
* **Solución Final Aplicada:** 
```python
import csv

class CsvParser:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_y_deduplicar(self):
        ips_unicas = set()
        registros = []

        try:
            with open(self.ruta_archivo, mode="r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    ip = fila.get("ip")
                    status = int(fila.get("status", 0))
                    
                    if ip:
                        ips_unicas.add(ip)

                    registros.append({
                        "ip": ip,
                        "status_code": status, 
                        "endpoint": fila.get("path"),
                        "memoria": fila.get("memory_percent") 
                    })
            return registros, ips_unicas

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {self.ruta_archivo}")
            return [], set()
```

## Registro de Prompt # 3

* **Fecha:** 2026-10-19

* **Módulo/Función:** src/services/api_client.py

* **Prompt Enviado:** "Voy a consumir la API pública de ip-api.com usando la librería requests. ¿Cómo puedo implementar un cliente robusto que maneje excepciones de red, configure un timeout y evite consultar direcciones IP de la red local (como 192.168.x.x)?"

* **Respuesta de la IA:** La IA proporcionó una clase ApiClient con un método que usa requests.get(url, timeout=5) dentro de un try...except requests.exceptions.RequestException. También sugirió usar ip.startswith("192.168") para las IPs locales.

* **Análisis Crítico:** El código era correcto, pero la IA omitió un detalle crucial: la versión gratuita de ip-api.com tiene un límite de 45 peticiones por minuto. Si el script itera rápido por un set grande de IPs, la API bloqueará mi dirección IP. Por lo tanto, importé el módulo time y agregué una pausa de 1.5 segundos. También agregué una validación para revisar que el JSON devuelva "status": "success".
* **Solución Final Aplicada:** 
```python
import requests
import time

class ApiClient:
    def __init__(self):
        self.base_url = "http://ip-api.com/json/"

    def obtener_ubicacion(self, ip):
        if ip.startswith("192.168") or ip.startswith("127."):
            return "Local, Red Interna"

        url = f"{self.base_url}{ip}"
        try:
            respuesta = requests.get(url, timeout=5)
            if respuesta.status_code == 200:
                datos = respuesta.json()
                time.sleep(1.5)
                if datos.get("status") == "success":
                    return f"{datos.get('country')}, {datos.get('city')}"
                return "Desconocido"
            else:
                return None
        except requests.exceptions.RequestException as error_red:
            print("Se generó un problema de conexión:", error_red)
            return None
```

## Registro de Prompt # 4

* **Fecha:** 2026-10-19

* **Módulo/Función:** src/parsers/json_parser.py

* **Prompt Enviado:** "Para el archivo events.json, necesito leer la lista de eventos y eliminar los duplicados basándome en su atributo 'event_id'. ¿Cuál es la forma más pitónica de hacer esto y cómo puedo blindar el código contra archivos JSON corruptos?"

* **Respuesta de la IA:** La IA sugirió cargar el archivo con json.load(), iterar sobre los eventos y usar un set para rastrear los IDs. Para el blindaje, sugirió usar except json.JSONDecodeError.

* **Análisis Crítico:** La respuesta de la IA fue muy buena. Implementé el JSONDecodeError para cumplir con el manejo de excepciones del Hito 1. Además, tuve un error de tipeo propio al nombrar el método (leer_yDeduplicar en vez de leer_y_deduplicar), el cual solucioné al integrarlo en el main.
* **Solución Final Aplicada:** 
```python
import json

class JsonParser:
    def __init__(self, ruta_archivo):
        self.ruta_archivo = ruta_archivo

    def leer_y_deduplicar(self):
        eventos_unicos = set()
        lista_eventos = []

        try:
            with open(self.ruta_archivo, mode="r", encoding="utf-8") as archivo:
                datos = json.load(archivo)

                for evento in datos:
                    id_evento = evento.get("event_id")

                    if id_evento:
                        eventos_unicos.add(id_evento)

                    lista_eventos.append(evento)
            
            return lista_eventos, eventos_unicos
            
        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {self.ruta_archivo}")
            return [], set()
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.ruta_archivo} no tiene un formato JSON válido") 
            return [], set()
```

## Registro de Prompt # 5

* **Fecha:** 2026-10-19

* **Módulo/Función:** src/services/metrics.py

* **Prompt Enviado:**  "Necesito crear una clase de métricas. Debe calcular el porcentaje de errores HTTP 500, identificar las IPs que acumulan errores (status >= 400) y calcular el promedio de memoria. ¿Cómo evito la división por cero y cómo convierto los strings de memoria a float de forma segura?"

* **Respuesta de la IA:** La IA proporcionó un código usando list comprehensions y sum(). Para la memoria, sugirió usar isdigit() para validar los strings antes de convertirlos.

* **Análisis Crítico:** El método isdigit() sugerido falla si hay números decimales (como "40.5"). Tuve que cambiar la validación a str(mem).replace('.','',1).isdigit(). Además, agregué un if not self.registros: return 0.0 para evitar el error de división por cero.
* **Solución Final Aplicada:** 
```python
class MetricsCalculator:
    def __init__(self, registros):
        self.registros = registros

    def calcular_porcentaje_500(self):
        if not self.registros:
            return 0.0
        total = len(self.registros)
        errores_500 = sum(1 for r in self.registros if r.get("status_code") == 500)
        return (errores_500 / total) * 100

    def identificar_ips_criticas(self, umbral=1):
        conteo_errores_por_ip = {}
        for r in self.registros:
            ip = r.get("ip")
            status = r.get("status_code", 0)

            if ip and status >= 400:
                conteo_errores_por_ip[ip] = conteo_errores_por_ip.get(ip, 0) + 1
                
        ips_criticas = {ip: conteo for ip, conteo in conteo_errores_por_ip.items() if conteo >= umbral}
        return ips_criticas

    def calcular_promedio_memoria(self):
        if not self.registros:
            return 0.0
        
        memorias = []
        for r in self.registros:
            mem = r.get("memoria")
            if mem and str(mem).replace('.','',1).isdigit():
                memorias.append(float(mem))
                
        if not memorias:
            return 0.0
            
        return sum(memorias) / len(memorias)
```

## Registro de Prompt # 6

* **Fecha:** 2026-10-19

* **Módulo/Función:** src/main.py

* **Prompt Enviado:** "¿Cómo puedo aplicar el principio de responsabilidad única en mi archivo main.py? Quiero que actúe solo como un orquestador que instancie mis clases y genere el reporte JSON final sin acoplar la lógica de negocio."

* **Respuesta de la IA:** La IA sugirió estructurar el flujo en pasos comentados y usar json.dump(reporte, archivo, indent=4, ensure_ascii=False) para generar un JSON limpio.

* **Análisis Crítico:** La IA acertó con el flujo. Sin embargo, no tenía en cuenta si el CSV estaba vacío. Agregué un bloque de control de flujo (if not registros:) para detener la ejecución tempranamente y evitar errores.

* **Solución Final Aplicada:** 
```python
import json
from parsers.csv_parser import CsvParser
from parsers.json_parser import JsonParser
from services.api_client import ApiClient
from services.metrics import MetricsCalculator

def generar_reporte():
    print("--- INICIANDO MOTOR TI-METRICS ---")

    parser_csv = CsvParser("data/logs.csv")
    registros, ips_unicas = parser_csv.leer_y_deduplicar()
    
    parser_json = JsonParser("data/events.json")
    eventos, eventos_unicos = parser_json.leer_y_deduplicar()

    if not registros:
        print("No hay logs para procesar.")
        return

    metricas = MetricsCalculator(registros)
    porcentaje_errores = metricas.calcular_porcentaje_500()
    ips_criticas = metricas.identificar_ips_criticas()
    promedio_memoria = metricas.calcular_promedio_memoria()

    api = ApiClient()
    ubicaciones = {}
    print(f"Consultando {len(ips_unicas)} IPs a la API...")
    for ip in ips_unicas:
        ubicaciones[ip] = api.obtener_ubicacion(ip)

    reporte = {
        "metricas": {
            "total_logs": len(registros),
            "total_eventos_unicos": len(eventos_unicos),
            "porcentaje_errores_500": f"{porcentaje_errores:.2f}%",
            "ips_criticas": ips_criticas,
            "promedio_memoria": f"{promedio_memoria:.2f}%"
        },
        "geolocalizacion_ips": ubicaciones
    }

    with open("data/reporte_resumen.json", "w", encoding="utf-8") as f:
        json.dump(reporte, f, indent=4, ensure_ascii=False)
    
    print("✅ Reporte guardado en data/reporte_resumen.json")

if __name__ == "__main__":
    generar_reporte()
```

## Registro de Prompt # 7

* **Fecha:** 2026-10-20

* **Módulo/Función:** tests/test_parsers.py

* **Prompt Enviado:** "¿Cómo puedo empezar a implementar pruebas unitarias en Python usando pytest? Quiero validar que mi CsvParser lea el archivo y maneje las excepciones de archivos inexistentes."

* **Respuesta de la IA:** La IA explicó cómo estructurar funciones que empiecen con test_ y cómo usar assert para verificar longitudes de listas y retornos vacíos.

* **Análisis Crítico:** Comprendí que el uso de assert es crucial para asegurar la integridad del código. Aunque las pruebas son sencillas, preparan el terreno para el Hito 3, donde se exigirá una cobertura mayor al 80%.

* **Solución Final Aplicada:** 
```python
import pytest
from src.parsers.csv_parser import CsvParser

def test_leer_csv_correctamente():
    parser = CsvParser("data/logs.csv")
    registros, ips_unicas = parser.leer_y_deduplicar()
    assert len(registros) > 0, "El parser no devolvió registros"
    assert "ip" in registros[0], "El registro no tiene la llave 'ip'"

def test_archivo_inexistente():
    parser = CsvParser("data/no_existe.csv")
    registros, ips = parser.leer_y_deduplicar()
    assert registros == []
    assert ips == set()
```

## Registro de Prompt # 8

* **Fecha:** 2026-10-20
* **Módulo/Función:** README.md
* **Prompt Enviado:** "Necesito documentar mi repositorio para el Hito 1. ¿Cómo puedo estructurar el README.md usando Markdown para incluir tablas de resultados, bloques de código con resaltado de sintaxis y badges de estado?"
* **Respuesta de la IA:** La IA proporcionó la sintaxis para tablas, negritas, badges de shields.io y bloques de código usando comillas invertidas triples.
* **Análisis Crítico:** Aprendí que Markdown es sensible a los espacios (si falta una línea en blanco, los títulos se fusionan con las tablas). Corregí el formato y aseguré que los datos de la tabla coincidieran exactamente con la ejecución real de mi código.
* **Solución Final Aplicada:** Se implementó la documentación completa con 10 secciones, badges, tablas y ejemplos de instalación.








