#Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
#de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
#a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
#b. indicar el plantea natal de Luke Skywalker y Han Solo
#c. insertar un nuevo personaje antes del maestro Yoda
#d. eliminar el personaje ubicado después de Jar Jar Binks

class Personaje:
    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return f'{self.nombre} ({self.planeta})'

class Cola:
    def __init__(self):
        self.cola = []

    def encolar(self, personaje):
        self.cola.append(personaje)

    def desencolar(self):
        if not self.esta_vacia():
            return self.cola.pop(0)
        return None

    def esta_vacia(self):
        return len(self.cola) == 0

    def mostrar(self):
        for personaje in self.cola:
            print(personaje)


personajes = Cola()

personajes.encolar(Personaje('Luke Skywalker', 'Tatooine'))
personajes.encolar(Personaje('Han Solo', 'Corellia'))
personajes.encolar(Personaje('Leia Organa', 'Alderaan'))
personajes.encolar(Personaje('Yoda', 'Dagobah'))
personajes.encolar(Personaje('Jar Jar Binks', 'Naboo'))
personajes.encolar(Personaje('Chewbacca', 'Kashyyyk'))
personajes.encolar(Personaje('Wicket', 'Endor'))

print()
#a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrar_personajes_por_planeta(cola, planetas):
    print(f"Personajes de {', '.join(planetas)}:")
    for personaje in cola.cola:
        if personaje.planeta in planetas:
            print(personaje)

mostrar_personajes_por_planeta(personajes, ["Alderaan", "Endor", "Tatooine"])

print()
#b. indicar el plantea natal de Luke Skywalker y Han Solo
def planeta_de_luke_y_han(cola):
    for personaje in cola.cola:
        if personaje.nombre == "Luke Skywalker" or personaje.nombre == "Han Solo":
            print(f'{personaje.nombre} es de {personaje.planeta}')

planeta_de_luke_y_han(personajes)

print()
#c. insertar un nuevo personaje antes del maestro Yoda
def insertar_antes_de_yoda(cola, nuevo_personaje):
    index = -1
    for i, personaje in enumerate(cola.cola):
        if personaje.nombre == "Yoda":
            index = i
            break
    if index != -1:
        cola.cola.insert(index, nuevo_personaje)
    else:
        print("Yoda no está en la cola.")

nuevo_personaje = Personaje("Ahsoka Tano", "Shili")
insertar_antes_de_yoda(personajes, nuevo_personaje)

print()
#d. eliminar el personaje ubicado después de Jar Jar Binks
def eliminar_despues_de_jar_jar(cola):
    for i, personaje in enumerate(cola.cola):
        if personaje.nombre == "Jar Jar Binks" and i + 1 < len(cola.cola):
            eliminado = cola.cola.pop(i + 1)
            print(f'Se ha eliminado a {eliminado.nombre}')
            break


eliminar_despues_de_jar_jar(personajes)

print()
print('Cola de personajes actualizada')
personajes.mostrar()

