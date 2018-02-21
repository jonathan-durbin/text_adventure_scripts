import items

''' Parent class for all enemies'''

class enemy:
    def __init__(self, name, hp, damage, type_boss):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.type_boss = type_boss
        
    def is_alive(self):
        return self.hp > 0
    
''' Sub-classes for two types of enemies '''

class reg_enemy(enemy):
    def __init__(self, name, hp, damage, type_boss):
        type_boss = False
        super().__init__(name, hp, damage, type_boss)

class boss(enemy):
    def __init__(self, name, hp, damage, type_boss, weapon):
        type_boss = True
        self.weapon = weapon
        super().__init__(name, hp, damage, type_boss)
        
''' Regular enemies '''

class sketchy_guy(reg_enemy):
    def __init__(self):
        super().__init__(name = 'Sketchy Guy',
                         hp = 10,
                         damage = 7, 
                         type_boss = False)

class crazy_guy(reg_enemy):
    def __init__(self):
        super().__init__(name = 'Crazy Guy',
                         hp = 12,
                         damage = 9,
                         type_boss = False)

class zombie(reg_enemy):
    def __init__(self):
        super().__init__(name = 'Zombie',
                         hp = 15,
                         damage = 4,
                         type_boss = False)

class stitched_monster(reg_enemy):
    def __init__(self):
        super().__init__(name = 'Stitched Monstrosity',
                         hp = 17,
                         damage = 12,
                         type_boss = False)

''' Bosses '''

class huge_floating_skull(boss):
    def __init__(self):
        super().__init__(name = 'Huge Floating Skull',
                         hp = 28,
                         damage = 19,
                         type_boss = True,
                         weapon = items.second_law)

class huge_judge(boss):
    def __init__(self):
        super().__init__(name = 'The Judge',
                         hp = 35,
                         damage = 29,
                         type_boss = True,
                         weapon = items.third_law)

class little_boy(boss):
    def __init__(self):
        super().__init__(name = 'Little Boy',
                         hp = 50,
                         damage = 39,
                         type_boss = True,
                         weapon = items.zeroth_law)
