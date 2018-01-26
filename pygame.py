class meeps:

    health = 10
    energy = 10

    def getHurtPistol(self):
        self.health = self.health - 5

    def getHurtFeather(self):
        self.health = self.health - 10

    def getHurtRPG(self):
        self.health = self.health - 1

    def looseEnergy(self):
        self.energy = self.energy - 3

    def sayEnergy(self):
        print("meeps energy is " + str(self.energy))

    def sayHealth(self):
        print("meeps health is " + str(self.health))

meep = meeps()
meep1 = meeps()

from time import sleep

choice = input("You have to pick a weapon to try hurt my meep, pick either a pistol, feather or rpg..")

if choice == "pistol":
    print("You hurt my meep, that was mean")
    meep.getHurtPistol()
    sleep(1)
    meep.sayHealth()
    print("My meep now has a hole in his stomach, he lost some of his energy")
    meep.sayEnergy()
    
elif choice == "feather":
    print("My meep is alergic to feathers")
    meep.getHurtFeather()
    sleep(1)
    print("you killed him :(")
    meep.sayHealth()
    
elif choice == "rpg":
    print("My meep eats rpg's for breakfast, Haw Haw Haw")
    meep.getHurtRPG()
    sleep(1)
    print("you barely hurt my meep, HAW HAW HAW")
    meep.sayHealth()

else:
    print("You need to type the wepons in lower case")
    sleep(1)
    print("try again")
