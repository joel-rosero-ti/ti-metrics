import requests
import time

class ApiClient:
    def __init__(self):
        self.base_url ="http://ip-api.com/json/"

    def obtener_ubicacion(self, ip):
        url = f"{self.base_url}{ip}"
        try:
            respuesta = requests.get(url, timeout=5)
            if respuesta.status_code ==200:
                datos = respuesta.json()
                return datos
            else:
                print("EL servidor respodió con un código a 200")
                return None
        except requests.exceptions.RequestException as error_red:
            print("Se genro un problema de conexión:", error_red)
            return None
        

