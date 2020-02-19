from random import randint

class Character():

    
    def __init__(self, char_name, char_description):
        """ Creates a character with name, description and conversation"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """ Gives the character a description """
        print( self.name + " is here!" )
        print( self.description )
        
    def set_conversation(self, conversation):
        """ Sets what this character will say when talked to """
        self.conversation = conversation

    def talk(self):
        """ prints out character's name and what they say """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    def fight(self, combat_item):
        """ Enables you to fight with this character """
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):

    enemies_defeated = 0

    def __init__(self, char_name, char_description):
        """ Creates an instance of an enemy and gives it a name, description, weakness and item """
        super().__init__(char_name, char_description)

        self.weakness = None
        self.has_item = None

    def set_item(self, item):
        """ Sets the item that the enemy has """
        self.has_item = item

    def get_item(self):
        """ Returns the item that the enemy has """
        return has_item

    def get_weakness(self):
        """ Returns the enemies weakness """
        return self.weakness

    def set_weakness(self, weakness):
        """ Set the enemy's weakness """
        self.weakness = weakness

    def get_enemies_defeated(self):
        """ returns the number of enemies that have been defeated """
        return Enemy.enemies_defeated

    def set_enemies_defeated(self, enemies_defeated):
        """ Sets the number of enemies that have been defeated """
        Enemy.enemies_defeated = enemies_defeated

    def fight(self, combat_item):
        """ Checks if the item that is being used to fight with is the enemy's weakness or not """
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False

    def steal(self):
        """ Determines if the enemy has something to steal and gives a random chance to steal"""
        chance  = randint(1,10)
        if chance > 5:
            if self.get_item is not None:
                print("You stole " + self.has_item + " from " + self.name)
            else:
                print(self.name + " has nothing to steal.")
        else:
            print("You failed to steal their stuff")

class Friend(Character):
    
    def __init__(self, char_name, char_description):

        """ Initialises an instance of a Friend taking the attributes from Character(the super class) and also giving it a feeling """
        
        super().__init__(char_name, char_description)
        self.feeling = None

    def hug(self):
        """ prints out that the friend hugs you """
        print(self.name + " hugs you back.")
