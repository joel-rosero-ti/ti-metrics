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
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.ruta_archivo} no tiene un formato JSON válido") 
            return []. set()
                     
