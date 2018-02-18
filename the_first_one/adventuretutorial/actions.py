
# coding: utf-8

# In[ ]:


from player import Player


# In[ ]:


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
        
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)


# In[ ]:


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, 
                         name='Move north', 
                         hotkey='n')

class MoveSouth(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, 
                         name='Move south', 
                         hotkey='s')

class MoveEast(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, 
                         name='Move east', 
                         hotkey='e')

class MoveWest(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, 
                         name='Move west', 
                         hotkey='w')


# In[ ]:


class ViewInventory(Action):
    """Prints the player's inventory"""
    def __init__(self):
        super().__init__(method=Player.print_inventory, 
                         name='View inventory', 
                         hotkey='i')


# In[ ]:


class Attack(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.attack, 
                         name="Attack", 
                         hotkey = 'a', 
                         enemy=enemy)

class Flee(Action):
    def __init__(self, tile):
        super().__init__(method=Player.flee, 
                         name="Flee", 
                         hotkey='f', 
                         tile=tile)

# In[ ]:


class Heal(Action):
    def __init__(self, consumable):
        super().__init__(method=Player.heal,
                         hotkey = 'h', 
                         consumable = consumable)

