class Ministerio:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.nroEmpleados = 0
        self.empleados = []   # Lista de listas (nombre, apellido)
        self.edades = []
        self.sueldos = []

    def agregar_empleado(self, nombre, apellido, edad, sueldo):
        self.empleados.append([nombre, apellido])
        self.edades.append(edad)
        self.sueldos.append(sueldo)
        self.nroEmpleados += 1

    def eliminar_por_edad(self, edad_x):
        nuevos_empleados = []
        nuevas_edades = []
        nuevos_sueldos = []
        for i in range(self.nroEmpleados):
            if self.edades[i] != edad_x:
                nuevos_empleados.append(self.empleados[i])
                nuevas_edades.append(self.edades[i])
                nuevos_sueldos.append(self.sueldos[i])
        self.empleados = nuevos_empleados
        self.edades = nuevas_edades
        self.sueldos = nuevos_sueldos
        self.nroEmpleados = len(self.empleados)

    def __add__(self, otro):
        # Transferir primer empleado del otro ministerio al actual
        if otro.nroEmpleados > 0:
            self.agregar_empleado(*otro.empleados[0], otro.edades[0], otro.sueldos[0])
            otro.empleados.pop(0)
            otro.edades.pop(0)
            otro.sueldos.pop(0)
            otro.nroEmpleados -= 1

    def mostrar_menor_edad(self):
        if not self.edades: return
        min_edad = min(self.edades)
        print("Empleado(s) con menor edad:")
        for i in range(self.nroEmpleados):
            if self.edades[i] == min_edad:
                print(f"{self.empleados[i][0]} {self.empleados[i][1]} - Edad: {self.edades[i]}")

    def mostrar_menor_sueldo(self):
        if not self.sueldos: return
        min_sueldo = min(self.sueldos)
        print("Empleado(s) con menor sueldo:")
        for i in range(self.nroEmpleados):
            if self.sueldos[i] == min_sueldo:
                print(f"{self.empleados[i][0]} {self.empleados[i][1]} - Sueldo: {self.sueldos[i]}")


# === USO DEL PROGRAMA ===

# Instanciar dos ministerios
m1 = Ministerio("Ministerio de Trabajo", "La Paz")
m2 = Ministerio("Ministerio de Educación", "Cochabamba")

# Agregar empleados
m1.agregar_empleado("Pedro", "Rojas", 35, 2500)
m1.agregar_empleado("Lucy", "Sosa", 43, 3250)
m1.agregar_empleado("Ana", "Perez", 26, 2700)
m1.agregar_empleado("Saul", "Arce", 29, 2500)

m2.agregar_empleado("Juan", "Castro", 28, 2000)
m2.agregar_empleado("Maria", "Luna", 30, 3100)

# a) Mostrar datos antes
print("Ministerio 1 antes de eliminar:")
m1.mostrar_menor_edad()

# b) Eliminar por edad = 43
m1.eliminar_por_edad(43)

print("\nMinisterio 1 después de eliminar edad 43:")
m1.mostrar_menor_edad()

# c) Transferir empleado de m2 a m1
m1 + m2

print("\nMinisterio 1 después de transferencia:")
m1.mostrar_menor_sueldo()

print("\nMinisterio 2 después de transferencia:")
print(m2.empleados)

# d) Mostrar con menor edad y menor sueldo
print("\n--- Empleados con menor edad ---")
m1.mostrar_menor_edad()

print("\n--- Empleados con menor sueldo ---")
m1.mostrar_menor_sueldo()
