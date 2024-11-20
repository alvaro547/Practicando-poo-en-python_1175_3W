print("Alvaro Campechano 3W")
class Marino():
    def hablar(self):
        print("Hola soy un animal marino!")  # Cambié las comillas

class Pulpo(Marino):
    def hablar(self):
        print("Hola soy un pulpo!")  # Cambié las comillas

class Foca(Marino):
    def hablar(self, mensaje):
        print(mensaje)  # No es necesario asignar mensaje a un atributo

# Crear objetos e invocar el método hablar
marino = Marino()
marino.hablar()

pulpo = Pulpo()
pulpo.hablar()

foca = Foca()
foca.hablar("Hola soy una foca!")  # Pasé el mensaje directamente al método
