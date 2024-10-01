# 22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se cono-
# ce el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino

# F) –por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Ro-
# manoff, Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.

class PersonajeMCU:
    def __init__(self, nombre, superheroe, genero):
        self.nombre = nombre
        self.superheroe = superheroe
        self.genero = genero

    def __str__(self):
        return f'{self.nombre}, {self.superheroe}, {self.genero}'

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

cola_personajes_mcu = Cola()
cola_personajes_mcu.encolar(PersonajeMCU("Tony Stark", "Iron Man", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Steve Rogers", "Capitán América", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Natasha Romanoff", "Black Widow", "F"))
cola_personajes_mcu.encolar(PersonajeMCU("Peter Parker", "Spider-Man", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Carol Danvers", "Capitana Marvel", "F"))
cola_personajes_mcu.encolar(PersonajeMCU("Wanda Maximoff", "Scarlet Witch", "F"))
cola_personajes_mcu.encolar(PersonajeMCU("Stephen Strange", "Doctor Strange", "M"))
cola_personajes_mcu.encolar(PersonajeMCU("Scott Lang", "Ant-Man", "M"))

# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
def capitana_marvel(cola):
    for personaje in cola.cola:
        if personaje.superheroe == "Capitana Marvel":
            print(f'El personaje de Capitana Marvel es {personaje.nombre}')
            return
    print("Capitana Marvel no se encuentra en la cola.")

capitana_marvel(cola_personajes_mcu)

print()
# b. mostrar los nombre de los superhéroes femeninos;
def superheroes_fem(cola):
    print("Superheroes femeninos:")
    for personaje in cola.cola:
        if personaje.genero == "F":
            print(personaje.superheroe)

superheroes_fem(cola_personajes_mcu)

print()
# c. mostrar los nombres de los personajes masculinos;
def personajes_masculinos(cola):
    print("Personajes masculinos:")
    for personaje in cola.cola:
        if personaje.genero == "M":
            print(personaje.nombre)

personajes_masculinos(cola_personajes_mcu)

print()
# d. determinar el nombre del superhéroe del personaje Scott Lang;
def super_scott_lang(cola):
    for personaje in cola.cola:
        if personaje.nombre == "Scott Lang":
            print(f'Scott Lang es {personaje.superheroe}')
            return
    print("Scott Lang no se encuentra en la cola.")

super_scott_lang(cola_personajes_mcu)

print()
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
# con la letra S;
def comienzan_s(cola):
    print("Personajes o superheroes que comienzan con S:")
    for personaje in cola.cola:
        if personaje.nombre.startswith('S') or personaje.superheroe.startswith('S'):
            print(personaje)

comienzan_s(cola_personajes_mcu)

print()
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
# de superhéroes.
def encontrar_CarolDanvers(cola):
    for personaje in cola.cola:
        if personaje.nombre == "Carol Danvers":
            print(f'Carol Danvers es {personaje.superheroe}')
            return
    print("Carol Danvers no se encuentra en la cola.")

encontrar_CarolDanvers(cola_personajes_mcu)


