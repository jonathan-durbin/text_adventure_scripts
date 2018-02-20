import items, world

class player():
    def __init__(self):
        self.inventory = [items.chalk(), 
                          items.first_law]
        self.hp = 100
        self.gold = 7
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
            print(item, '\n ========== \n')
            
    def quit(self):
        self.victory = True
            
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        next_tile = world.tile_exists(self.location_x, self.location_y)
        print(next_tile.intro_text())
        
    def move_north(self):
        self.move(dx=0, dy=-1)
        
    def move_south(self):
        self.move(dx=0, dy=1)
        
    def move_east(self):
        self.move(dx=1, dy=0)
        
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

        print("\nI use {} against {}!\n".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage

        if not enemy.is_alive():
            print("\nI killed {}.\n".format(enemy.name))
        else:
            print("\n{} health is {}.\n".format(enemy.name, enemy.hp))

    def flee(self, tile):
        '''Move to a random available tile. '''
        available_moves = tile.adjacent_moves()
        r = random.randint(0, len(available_moves) - 1)
        self.do_action(available_moves[r])
        
    def heal(self):
        edibles = [item for item in self.inventory if isinstance(item, items.heal_item)]
        
        if not edibles:
            print('\nI don\'t have anything to eat...\n')
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
                
                
    def trade(self):
        room = world.tile_exists(self.x, self.y)
        room.check_if_trade(self)