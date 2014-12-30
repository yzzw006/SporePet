class Pet:
    icon = "temp.png"
    skill = [0,0,0,-1,-1,-1]
    #private
    _type = 0
    _health = 10
    _power = 10
    _speed = 10
    _quantity = 1.5
    _level = 25

    #TODO: experience
    #_exp...
    
    def __init__(self):
        self._refreshProperty()
    
    def setProperty(self, health=10, power=10, speed=10, quantity=1.5, level=25):
        self._health = health
        self._power = power
        self._speed = speed
        self._level = level
        self._quantity = quantity
        self._refreshProperty()
    
    def _refreshProperty(self):
        self.health = 100 + self._health * self._level * self._quantity * 5
        self.power = self._power * self._level * self._quantity
        self.speed = self._speed * self._level * self._quantity
        self.currentHealth = self.health
    
class PetInBattle:
    def __init__(self, pet):
#         if(type(pet) != Pet):
#             return
        self.health = pet.health
        self.currentHealth = pet.currentHealth
        self.power = pet.power
        self.speed = pet.speed
        self.skill = pet.skill[:3]
        
        
