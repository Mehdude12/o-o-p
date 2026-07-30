class parrot:
    species = "bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age


commando = parrot("Commando", 10)
print(commando.name, commando.age, commando.species)
commandee = parrot("Trooper", 4)
print(commandee.name, commandee.age, commandee.species)
