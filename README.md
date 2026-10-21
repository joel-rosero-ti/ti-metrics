# TI-Metrics: Engine de Analítica de Logs

**Asignatura:** Programación II  
**Estudiante:** Joel Rosero  
**Carrera:** Ingeniería en Tecnologías de la Información

## Cuadro de Logros y Badges

| Badge | Estado | Hito Asociado |
| :--- | :--- | :--- |
| **Data Wrangler** | ![Data Wrangler](https://img.shields.io/badge/Data_Wrangler-Bloqueado-inactive?style=for-the-badge&logo=python) | Hito 1: Persistencia & APIs |
| **OOP Architect** | ![OOP Architect](https://img.shields.io/badge/OOP_Architect-Bloqueado-inactive?style=for-the-badge&logo=diagrams.net) | Hito 2: Arquitectura POO |
| **PyTest Guardian** | ![PyTest Guardian](https://img.shields.io/badge/PyTest_Guardian-Bloqueado-inactive?style=for-the-badge&logo=pytest) | Hito 3: Cobertura > 80% |
| **AI Auditor** | ![AI Auditor](https://img.shields.io/badge/AI_Auditor-Bloqueado-inactive?style=for-the-badge&logo=openai) | Hito 3: PROMPTS.md & TDD |
| **Git Flow Master** | ![Git Flow Master](https://img.shields.io/badge/Git_Flow_Master-Bloqueado-inactive?style=for-the-badge&logo=github) | Transversal: Commits Semánticos |

---

##  1. Descripción del Proyecto

**TI-Metrics** es un proyecto desarrollado en Python para analizar registros de eventos de infraestructura tecnológica. Permite leer archivos CSV y JSON, validar registros, identificar duplicados y calcular métricas relacionadas con errores HTTP 500.

También consulta información geográfica aproximada de direcciones IP mediante una API y genera un reporte con los resultados.

##  2. Objetivos

* Leer archivos CSV y JSON.
* Validar registros e identificar datos inválidos.
* Detectar registros duplicados.
* Procesar datos mediante estructuras de Python (listas, diccionarios, sets).
* Calcular la cantidad y el porcentaje de errores HTTP 500.
* Identificar las direcciones IP con más errores.
* Consultar información geográfica aproximada mediante una API.
* Generar reportes en formato JSON.

##  3. Tecnologías utilizadas

* **Python 3**
* **Archivos CSV y JSON**
* **Biblioteca `requests`** (para el consumo de la API)
* **API IP-API** (para geolocalización)
* **Git y GitHub** (control de versiones)
* **VS Code** (entorno de desarrollo)
* **Pytest** (para las pruebas automatizadas en los próximos hitos)

##  4. Estructura del Proyecto

```text
ti-metrics/
├── data/                      # Archivos de entrada y salida
│   ├── logs.csv               # Registros de accesos HTTP
│   ├── events.json            # Eventos del servidor
│   └── reporte_resumen.json   # Reporte generado por el script
├── src/                       # Código fuente
│   ├── __init__.py
│   ├── main.py                # Orquestador principal (une todas las clases)
│   ├── parsers/               # Módulos de lectura
│   │   ├── csv_parser.py
│   │   └── json_parser.py
│   ├── services/              # Lógica de negocio y API
│   │   ├── api_client.py
│   │   └── metrics.py
│   └── utils/                 # Funciones auxiliares
├── tests/                     # Pruebas unitarias
├── PROMPTS.md                 # Bitácora de IA
├── README.md                  # Documentación
├── requirements.txt           # Dependencias
└── .gitignore

##  5. Instalación y ejecución

Para instalar las dependencias, ejecutar desde la carpeta principal del proyecto:
bash

python -m pip install -r requirements.txt

Para ejecutar el programa:
bash

python src/main.py

##  6. Resultados de ejecución

En una ejecución de prueba con nuestros archivos actuales se obtuvieron los siguientes resultados:
Indicador	Resultado
Registros leídos del CSV	4 (se descartó 1 duplicado)
Registros leídos del JSON	2 (únicos)
Registros inválidos	0
Errores HTTP 500	2
Porcentaje de errores HTTP 500	50.00 %
Promedio de uso de memoria	66.34 %

Estos resultados corresponden a los archivos procesados durante esa ejecución. Los valores pueden cambiar si se modifican los datos de entrada.

El reporte se guarda en data/reporte_resumen.json.

##  7. API utilizada

El proyecto utiliza IP-API para consultar información geográfica aproximada de las direcciones IP.

Página del servicio: http://ip-api.com/

La disponibilidad de las consultas depende del servicio externo. La ubicación obtenida es aproximada.

##  8. Bitácora de inteligencia artificial

El archivo PROMPTS.md documenta el uso de herramientas de inteligencia artificial durante el desarrollo. La bitácora refleja las consultas realizadas, las sugerencias recibidas y las comprobaciones efectuadas sobre el código.

##  9. Control de versiones

El proyecto utiliza Git para registrar los cambios y GitHub para mantener el repositorio remoto.

Los commits siguen los prefijos semánticos establecidos en la guía de Programación II:

    feat: agregar funcionalidades.

    fix: corregir errores.

    refactor: reorganizar el código sin cambiar su comportamiento.

    docs: actualizar documentación.

    test: agregar o modificar pruebas.

Repositorio del proyecto: joel-rosero-ti/ti-metrics

##  10. Estado del proyecto

El primer avance contempla la lectura de archivos CSV y JSON, la validación de datos, la identificación de duplicados, el cálculo de métricas, la consulta de la API y la generación del reporte JSON.

Los siguientes hitos incorporarán las mejoras de arquitectura, las pruebas automatizadas y los demás requisitos establecidos por la asignatura.