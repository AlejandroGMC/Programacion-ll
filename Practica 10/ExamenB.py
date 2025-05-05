class Planta:
    def __init__(self, nombre, tipo, adaptacion_climatica, region):
        self.nombre = nombre
        self.tipo = tipo  # Ej: arbusto, hierba, árbol
        self.adaptacion_climatica = adaptacion_climatica
        self.region = region

    def dispersarse(self, nueva_region):
        print(f"{self.nombre} se ha dispersado a {nueva_region}")
        self.region = nueva_region

    def es_apta_para_clima(self, clima):
        return clima in self.adaptacion_climatica


class Clima:
    def __init__(self, tipo, temperatura_promedio, humedad, precipitacion):
        self.tipo = tipo
        self.temperatura_promedio = temperatura_promedio
        self.humedad = humedad
        self.precipitacion = precipitacion

    def es_favorable_para(self, planta: Planta):
        return planta.es_apta_para_clima(self.tipo)

    def comparar_con_otro(self, otro):
        return {
            "temperatura_diferencia": self.temperatura_promedio - otro.temperatura_promedio,
            "humedad_diferencia": self.humedad - otro.humedad
        }


class BarreraGeografica:
    def __init__(self, tipo, ubicacion, longitud_km, altura_m):
        self.tipo = tipo  # Montaña, lago, océano, etc.
        self.ubicacion = ubicacion
        self.longitud_km = longitud_km
        self.altura_m = altura_m

    def impide_dispersión(self, planta: Planta):
        print(f"La barrera {self.tipo} puede impedir la dispersión de {planta.nombre}")
        return True if self.tipo in ["océano", "cordillera", "zona inhóspita"] else False

    def informacion_general(self):
        return f"{self.tipo} ubicada en {self.ubicacion}, longitud: {self.longitud_km} km, altura: {self.altura_m} m"


# === USO Y SALIDA ===

# Crear una planta
planta1 = Planta("Quinoa", "Hierba", ["templado", "frío"], "Altiplano")

# Crear climas
clima1 = Clima("templado", 15.0, 60, 800)
clima2 = Clima("tropical", 28.0, 80, 1200)

# Crear una barrera
barrera1 = BarreraGeografica("cordillera", "Andes", 5000, 4000)

# Usar métodos con impresión de salida
print(planta1.es_apta_para_clima(clima1.tipo))  # True

planta1.dispersarse("Valles")

print(clima1.es_favorable_para(planta1))        # True

print(clima2.comparar_con_otro(clima1))         # {'temperatura_diferencia': 13.0, 'humedad_diferencia': 20}

print(barrera1.impide_dispersión(planta1))      # True

print(barrera1.informacion_general())           # "cordillera ubicada en Andes, longitud: 5000 km, altura: 4000 m"
