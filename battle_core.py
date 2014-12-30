from pet_base import PetInBattle


class BattleManager:
    def __init__(self):
        pass
    
    def initBattle(self, team1, team2):
        self.player = []
        self.enemy = []
        for pet in team1:
            self.player.append(PetInBattle(pet))
        for pet in team2:
            self.enemy.append(PetInBattle(pet))
    
    def startBattle(self):
        self.display()
        self.round = 1
        while(not self.isLost(self.player) and not self.isLost(self.enemy)):
            print("Round:%d"%self.round)
            #TODO: Get command and use skill
            #command = 1
            if(self.player[0].speed >= self.enemy[0].speed):
                self.attack(self.player,self.enemy)
                self.display()
                if(self.enemy[0].currentHealth <= 0):
                    continue
                self.attack(self.enemy, self.player)
                self.display()
            else:
                self.attack(self.enemy, self.player)
                self.display()
                if(self.enemy[0].currentHealth <= 0):
                    continue
                self.attack(self.player,self.enemy)
                self.display()
            self.endRound()

    def endRound(self):
        self.round += 1
        #TODO: account buff

    def isLost(self, team):
        for pet in team:
            if pet.currentHealth > 0:
                return False
        return True
    
    def attack(self, attacker, defencer):
        #TODO:Get skill damage and perform skill
        damage = attacker[0].power
        defencer[0].currentHealth -= damage
    
    def display(self):
        print("Player:%3d  Enemy:%3d"%(self.player[0].currentHealth,self.enemy[0].currentHealth))
