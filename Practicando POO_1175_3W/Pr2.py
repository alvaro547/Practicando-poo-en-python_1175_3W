print("Alvaro Campechano 3W")
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Crear un objeto de la clase Persona
p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))

# Llamamos al método cumpleaños dos veces
p.cumpleaños()
p.cumpleaños()

# Imprimir la edad de la persona después de dos cumpleaños
print(f"{p.nombre} cumple {p.edad} años")
