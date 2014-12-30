from pet_base import Pet
from battle_core import BattleManager

def main():
    p1 = Pet()
    p2 = Pet()
    p2.setProperty(quantity=1.5)
    bm = BattleManager()
    bm.initBattle([p1], [p2])
    bm.startBattle()
     
if __name__ == '__main__':
    main()
