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