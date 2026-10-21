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

## 📌 1. Descripción del Proyecto

**TI-Metrics** es un proyecto desarrollado en Python para analizar registros de eventos de infraestructura tecnológica. Permite leer archivos CSV y JSON, validar registros, identificar duplicados y calcular métricas relacionadas con errores HTTP 500.

También consulta información geográfica aproximada de direcciones IP mediante una API y genera un reporte con los resultados.

## 🎯 2. Objetivos

* Leer archivos CSV y JSON.
* Validar registros e identificar datos inválidos.
* Detectar registros duplicados.
* Procesar datos mediante estructuras de Python (listas, diccionarios, sets).
* Calcular la cantidad y el porcentaje de errores HTTP 500.
* Identificar las direcciones IP con más errores.
* Consultar información geográfica aproximada mediante una API.
* Generar reportes en formato JSON.

## 🛠️ 3. Tecnologías utilizadas

* **Python 3**
* **Archivos CSV y JSON**
* **Biblioteca `requests`** (para el consumo de la API)
* **API IP-API** (para geolocalización)
* **Git y GitHub** (control de versiones)
* **VS Code** (entorno de desarrollo)
* **Pytest** (para las pruebas automatizadas en los próximos hitos)

## 📂 4. Estructura del Proyecto

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