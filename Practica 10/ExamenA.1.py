class LineaTeleferico:
    def __init__(self, color, tramo, nroCabinas):
        self.color = color
        self.tramo = tramo
        self.nroCabinas = nroCabinas
        self.nroEmpleados = 0
        self.empleados = []   # Lista de tuplas: (nombre, apellido, edad, sueldo)

    def agregar_empleado(self, nombre, apellido, edad, sueldo):
        self.empleados.append((nombre, apellido, edad, sueldo))
        self.nroEmpleados += 1

    # (b) Eliminar empleados con apellido X
    def eliminar_empleado_por_apellido(self, apellido_buscado):
        self.empleados = [e for e in self.empleados if e[1] != apellido_buscado]
        self.nroEmpleados = len(self.empleados)

    # (c) Sobrecargar operador + para transferir empleado por apellido
    def __add__(self, otro):
        def transferir_empleado(empleado_apellido):
            for i, e in enumerate(self.empleados):
                if e[1] == empleado_apellido:
                    otro.agregar_empleado(*e)
                    self.empleados.pop(i)
                    self.nroEmpleados -= 1
                    break
        return transferir_empleado

    # (d.1) Mostrar empleados con mayor edad
    def mostrar_empleados_mayor_edad(self):
        if not self.empleados:
            print("No hay empleados.")
            return
        max_edad = max(e[2] for e in self.empleados)
        for e in self.empleados:
            if e[2] == max_edad:
                print(f"{e[0]} {e[1]} - Edad: {e[2]}")

    # (d.2) Mostrar empleados con mayor sueldo
    def mostrar_empleados_mayor_sueldo(self):
        if not self.empleados:
            print("No hay empleados.")
            return
        max_sueldo = max(e[3] for e in self.empleados)
        for e in self.empleados:
            if e[3] == max_sueldo:
                print(f"{e[0]} {e[1]} - Sueldo: {e[3]}")


# (a) Instanciar 2 objetos LineaTeleferico de diferente forma
linea1 = LineaTeleferico("Rojo", "Estación Central, Cementerio, 16 de Julio", 20)
linea2 = LineaTeleferico(color="Verde", tramo="Irpavi, Alto Obrajes, Del Libertador", nroCabinas=15)

# Agregar empleados al primer objeto
linea1.agregar_empleado("Pedro", "Rojas", 35, 2500)
linea1.agregar_empleado("Lucy", "Sosa", 43, 3250)
linea1.agregar_empleado("Ana", "Perez", 26, 2700)
linea1.agregar_empleado("Saul", "Arce", 29, 2500)

# (b) Eliminar empleados con apellido 'Perez'
linea1.eliminar_empleado_por_apellido("Perez")

# (c) Transferir empleado con apellido 'Rojas' de linea1 a linea2
transferir = linea1 + linea2  # devuelve función transferir_empleado
transferir("Rojas")

# (d) Mostrar empleados con mayor edad
print("Empleado(s) con mayor edad en linea1:")
linea1.mostrar_empleados_mayor_edad()

# (d) Mostrar empleados con mayor sueldo
print("\nEmpleado(s) con mayor sueldo en linea1:")
linea1.mostrar_empleados_mayor_sueldo()
