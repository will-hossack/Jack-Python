# Import necessary packages etc.
from enum import IntEnum
from collections import namedtuple
from random import randint

# Base class Creature that will be used as the base for the derived classes creature and player
class Creature(object):

    # Constructor which initialises base class variables
    def __init__(self,name,symbol,health,damage,gold):
        self.name   = name
        self.symbol = symbol
        self.health = health
        self.damage = damage
        self.gold   = gold

    # Various getters necessary for implementation of game logic later
    def getName(self):
        return self.name

    def getSymbol(self):
        return self.symbol

    def getHealth(self):
        return self.health

    def getDamage(self):
        return self.damage

    def getGold(self):
        return self.gold

    # Method to test whether the creature is dead (creature dead if health reaches 0)
    def isDead(self):
        return self.health<=0
    # Method to add given amount of gold to the creature
    def addGold(self,gold):
        self.gold+=gold
    # Method to reduce the health of creature by given amount
    def reduceHealth(self,health):
        self.health-=health

# Player class, inherits from Creature, used to implement the player of the game
class Player(Creature):
    # Constructor to call base constructor with supplied name and other fixed variables
    def __init__(self,name):
        # call base Creature constructor with name supplied to Player constructor and the symbol: @, health: 10,
        # damage:1, gold: 0, these provide the starting conditions for the player.
        Creature.__init__(self,name,'@',10,1,0)
        # we also add to the Player class a class member to represent the player level.
        self.level = 1

    # Method to level up the player, which increases the level member variable and damage member variables by 1.
    def levelUp(self):
        self.level+=1
        self.damage+=1

    # Getter to return player level.
    def getLevel(self):
        return self.level

    # Method to check whether the player has won, we consider the player as having won if they exceed level 20.
    def hasWon(self):
        return self.level>=20

# Monster class, inherits from Creature used to implement enemies in the game
class Monster(Creature):


    # The IntEnum Type will be used to index a list containing the data for our 3 monsters
    # it is useful to represent the monsters in this way since it avoids remembering numbers in order to access the
    # corresponding data. IntEnum is essentially a number that can be in one of four states, 0,1,2,3. Each state
    # representing the name of the monster given below. MAX_TYPES gives us the total number of monsters. Using IntEnum
    # instead of Enum allows us to use instances of Type directly as an int, rather than having to do any conversions.
    class Type(IntEnum):
        DRAGON    = 0
        ORC       = 1
        SLIME     = 2
        MAX_TYPES = 3


    # This namedtuple allows us to construct tuples where each element in the tuple has a name. Here the namedtuple
    # is called MonsterData and the elements are name, symbol, health, damage, gold.
    MonsterData = namedtuple("MonsterData","name symbol health damage gold")

    # We construct a list of length MAX_TYPES (number of monsters) where each element is a namedtuple MonsterData.
    # We set the value of each element in the named tuple, so we now have a list containing the traits of each monster.
    monsterData = [MonsterData("dragon",'D',20,4,100),MonsterData("orc",'o',6,2,25),
                   MonsterData("Slime",'s',1,1,5)]


    # Monster constructor. We now use the monsterData list and access the MonsterData namedtuple for the given Type of
    # monster from the provided Type IntEnum to the constructor.
    def __init__(self,type):
        Creature.__init__(self,Monster.monsterData[type].name,Monster.monsterData[type].symbol,
                          Monster.monsterData[type].health,Monster.monsterData[type].damage,
                          Monster.monsterData[type].gold)
        # We also initialise member varible called type, which is a Type (above enum) representing the type of monster
        self.type = type

    # static method to return a random monster. Made static so we don't need an instance of monster to call it, but
    # kept in monster class so we can keep everything contained.
    @staticmethod
    def getRandomMonster():

        # randint is called here with MAX_TYPES in one of its arguments. Since MAX_TYPES is an instance of an IntEnum
        # it behaves like an int.
        return Monster(randint(0,Monster.Type.MAX_TYPES - 1))

# function to deal with player attacking a monster
def attackMonster(player,monster):
    # if the player is dead stop since they cant attack
    if(player.isDead()):
        return
    # print what is going to happen
    print("You hit the " + monster.getName() + " for " + str(player.getDamage()) + " damage.")
    # reduce monster health by player's damage
    monster.reduceHealth(player.getDamage())
    # if the monster dies
    if(monster.isDead()):
        # tell player who they've killed
        print("You killed the " + monster.getName())
        # level player up
        player.levelUp()
        print("You are now level " + str(player.getLevel()))
        # give the player the monster's gold
        print("You found " + str(monster.getGold())+ " gold")
        player.addGold(monster.getGold())
# function to deal with monster attacking player
def attackPlayer(monster, player):
    # if the monster is dead stop the function since monster cannot attack
    if(monster.isDead()):
        return
    # reduce player health by the monster's damage
    player.reduceHealth(monster.getDamage())
    print("The " + monster.getName() + " hit you for " + str(monster.getDamage()))

# function to deal with actual fight between player and a monster
def fightMonster(player):
    # generate a monster for player to fight
    monster = Monster.getRandomMonster()
    print("You have encountered a " + monster.getName() + " (" + monster.getSymbol()+")")

    # while both monster and player are alive the fight goes on!
    while( not (monster.isDead()) and  not (player.isDead())):
        # ask user whether they want to run or fight
        userInput = str(input("(R)un or (F)ight: "))
        # if player decides to run 50:50 chance of success
        if(userInput=='R' or userInput=='r'):
            if(randint(0,1) == 1):
                print('You have successfully fled')
                return
            # otherwise monster gets a free hit on player
            else:
                print("You failed to flee!")
                attackPlayer(monster,player)
        # if player decides to fight
        if(userInput=='F' or userInput =='f'):
            # player attacks first
            attackMonster(player,monster)
            # then monster gets to attack player. Cases where one of player or monster have died are taken care of
            # in the attack functions we defined above.
            attackPlayer(monster,player)

# This is where the actual game gets played

# ask player for name and welcome them
playerName = str(input("Enter your name: "))
p = Player(playerName)
print("Welcome " + p.getName())

# While the player hasn't won or isn't dead player keeps fighting monster
while(not p.hasWon() and not p.isDead()):
    fightMonster(p)

# if the player dies tell them how well they did
if(p.isDead()):
    print("You died at level " + str(p.getLevel())+ " and with " + str(p.getGold())+ " gold.")
# if the payer wins tell them how much gold they got
else:
    print("You won the game with " + str(p.getGold())+ " gold!")


