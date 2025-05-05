class ComunidadIndigena:
    def __init__(self, nombre, region, contaminantes_detectados, poblacion_afectada):
        self.nombre = nombre
        self.region = region
        self.contaminantes_detectados = contaminantes_detectados
        self.poblacion_afectada = poblacion_afectada

    def exigir_compensacion(self, empresa):
        return f"{self.nombre} exige compensación a {empresa.nombre}."

    def denunciar_inaccion_gubernamental(self, gobierno):
        return f"{self.nombre} denuncia inacción del gobierno de {gobierno.presidente}."


class EmpresaMinera:
    def __init__(self, nombre, concesiones_activas, ganancias_anuales, zonas_de_operacion):
        self.nombre = nombre
        self.concesiones_activas = concesiones_activas
        self.ganancias_anuales = ganancias_anuales
        self.zonas_de_operacion = zonas_de_operacion

    def calcular_fondo_compensacion(self):
        return self.ganancias_anuales * 0.05

    def reducir_concesiones(self, cantidad):
        if cantidad <= self.concesiones_activas:
            self.concesiones_activas -= cantidad
        return self.concesiones_activas


class Gobierno:
    def __init__(self, presidente, ministerio_medio_ambiente, presupuesto_ambiental, politicas_ambientales):
        self.presidente = presidente
        self.ministerio_medio_ambiente = ministerio_medio_ambiente
        self.presupuesto_ambiental = presupuesto_ambiental
        self.politicas_ambientales = politicas_ambientales

    def responder_denuncia(self, comunidad):
        return f"El gobierno responderá la denuncia de {comunidad.nombre}."

    def asignar_presupuesto(self, monto):
        self.presupuesto_ambiental += monto
        return self.presupuesto_ambiental


# EJEMPLO DE USO
comunidad = ComunidadIndigena("CPILAP", "La Paz", ["mercurio", "plomo", "arsénico"], 3000)
empresa = EmpresaMinera("Empresa X", 10, 5000000, ["La Paz", "Potosí"])
gobierno = Gobierno("Luis Arce", "MMAyA", 1000000, ["Control de mercurio", "Regulación minera"])

print(comunidad.exigir_compensacion(empresa))
print(comunidad.denunciar_inaccion_gubernamental(gobierno))
print(empresa.calcular_fondo_compensacion())
print(gobierno.asignar_presupuesto(200000))
