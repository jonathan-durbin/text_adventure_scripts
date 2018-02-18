import items, world

class player():
    def __init__(self):
        self.inventory = [items.chalk, 
                          items.first_law, 
                          items.gold_item(7)]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        
    def is_alive(self):
        return self.hp > 0
    
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)
            
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n ========== ')
            
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.told_exists(self.location_x, self_location_y).intro_text())
        
    def move_north(self):
        self.move(dx=0, dy=-1)
        
    def move_south(self):
        self.move(dx=0, dy=1)
        
    def move_east(self):
        self.move(dx=-1, dy=0)
        
    def move_west(self):
        self.move(dx=-1, dy=0)
        
    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0

        for i in self.inventory:
            if isinstance(i, items.weapon_item):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("I use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage

        if not enemy.is_alive():
            print("I killed {}.".format(enemy.name))
        else:
            print("{} health is {}.".format(enemy.name, enemy.hp))

    def flee(self, tile):
        '''Move to a random available tile. '''
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
        
    def heal(self):
        edibles = [item for item in self.inventory if isinstance(item, items.heal_item)]
        
        if not edibles:
            print('I don\'t have anything to eat...')
            return
        
        for i, item in enumerate(edibles, 1):
            print('Choose an item to heal: ')
            print('{}. {}'.format(i, item))
            
        valid = False
        while not valid:
            choice = input('I choose: ')
            try:
                to_eat = edibles[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.healing_points)
                self.inventory.remove(to_eat)
                print('My HP: {}'.format(self.hp))
                valid = True
            except(ValueError, IndexError):
                print('Invalid choice, try again.')