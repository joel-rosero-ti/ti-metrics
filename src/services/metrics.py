class MetricsCalculator:
    def __init__(self, registros):
        self.registros = registros

    def calcular_porcentaje_500(self):
        """Calcula el porcentaje de peticiones con error HTTP 500."""
        if not self.registros:
            return 0.0

        total = len(self.registros)
        errores_500 = sum(1 for r in self.registros if r.get("status_code") == 500)
        return(errores_500/ total) * 100

    def identificar_ips_criticas(self, umbral=1):
        """Idetifica aquellas IPs que acumulan errores (status_code <= 400)."""
        conteo_errores_por_ip = {}

        for r in self.registros:
            ip= r.get("ip")
            status = r.get("status_code", 0)

            if ip and status >= 400:
                conteo_errores_por_ip[ip] = conteo_errores_por_ip.get(ip, 0) + 1
        ips_criticas = {ip: conteo for ip, conteo in conteo_errores_por_ip.items() if conteo >=umbral}

        return ips_criticas

    def calcular_promedio_memoria(self):
        if not self.registros:
            return 0.0
        
        memorias = []
        for r in self.registros:
            mem = r.get("memoria")
            if mem and str(mem).isdigit():
                memorias.append(int(mem))
                
        if not memorias:
            return 0.0
            
        return sum(memorias) / len(memorias)


        

