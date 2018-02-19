from player_file import player

class action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
        
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class move_north(action):
    def __init__(self):
        super().__init__(method=player.move_north, 
                         name='Move north', 
                         hotkey='n')

class move_south(action):
    def __init__(self):
        super().__init__(method=player.move_south, 
                         name='Move south', 
                         hotkey='s')

class move_east(action):
    def __init__(self):
        super().__init__(method=player.move_east, 
                         name='Move east', 
                         hotkey='e')

class move_west(action):
    def __init__(self):
        super().__init__(method=player.move_west, 
                         name='Move west', 
                         hotkey='w')

class view_inventory(action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=player.print_inventory, 
                         name='View inventory', 
                         hotkey='i')

class Attack(action):
    def __init__(self, enemy):
        super().__init__(method=player.attack, 
                         name="Attack", 
                         hotkey = 'a', 
                         enemy=enemy)

class Flee(action):
    def __init__(self, tile):
        super().__init__(method=player.flee, 
                         name="Flee", 
                         hotkey='f', 
                         tile=tile)

class Heal(action):
    def __init__(self, heal_item):
        super().__init__(method=player.heal,
                         hotkey = 'h', 
                         heal_item = heal_item)