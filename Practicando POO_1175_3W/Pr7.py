print("Alvaro Campechano 3W")
class Universidad():
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def __init__(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, Nombre, nombre, edad, especialidad):
        Universidad.__init__(self, Nombre)  # Inicializamos la clase Universidad
        Carrera.__init__(self, especialidad)  # Inicializamos la clase Carrera
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")

# Crear un objeto Estudiante
persona = Estudiante("Harvard", "Mike", 19, "Ingeniería mecatrónica")
persona.datos()
