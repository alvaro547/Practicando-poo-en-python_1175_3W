print("Alvaro Campechano 3W")
class Persona():
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)  # Corregido las comillas

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)  # Llama al constructor de la clase base (Persona)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)

# Crear una instancia de Estudiante
estudiante1 = Estudiante("Alvaro", "Campechano", "Programacion")
estudiante1.nombre_completo()  # Imprime el nombre completo
estudiante1.mostrar_carrera()  # Imprime la carrera del estudiante
