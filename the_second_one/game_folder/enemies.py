import items

''' Parent class for all enemies'''

class enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0
    
''' Sub-classes for two types of enemies '''

class reg_enemy(enemy):
    pass

class boss(enemy):
    def __init__(self, name, hp, damage, type_boss, weapon):
        type_boss = True
        self.weapon = weapon
        super().__init__(name, hp, damage)
        
''' Regular enemies '''

sketchy_guy = reg_enemy(name = 'Sketchy Guy',
                        hp = 10,
                        damage = 7)

crazy_guy = reg_enemy(name = 'Crazy Guy',
                      hp = 12,
                      damage = 9)

zombie = reg_enemy(name = 'Zombie',
                   hp = 15,
                   damage = 4)

stitched_monster = reg_enemy(name = 'Stitched Monstrosity',
                             hp = 17,
                             damage = 12)

''' Bosses '''

huge_floating_skull = boss(name = 'Huge Floating Skull',
                           hp = 28,
                           damage = 19,
                           type_boss = True,
                           weapon = items.second_law)

huge_judge = boss(name = 'The Judge',
                  hp = 35,
                  damage = 29,
                  type_boss = True,
                  weapon = items.third_law)

little_boy = boss(name = 'Little Boy',
                  hp = 50,
                  damage = 10,
                  type_boss = True,
                  weapon = items.zeroth_law)