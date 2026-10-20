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
                    # Leemos "status" de tu nueva tabla
                    status = int(fila.get("status", 0))
                    
                    if ip:
                        ips_unicas.add(ip)

                    registros.append({
                        "ip": ip,
                        "status_code": status, # Internamente lo llamamos status_code para no dañar metrics.py
                        "endpoint": fila.get("path"),
                        "memoria": fila.get("memory_percent") 
                    })
            return registros, ips_unicas

        except FileNotFoundError:
            print(f"Error: No se encontró el archivo en {self.ruta_archivo}")
            return [], set()


