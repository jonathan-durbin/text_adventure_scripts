
# coding: utf-8

# In[ ]:


import random
import items, world


# In[ ]:


class Player():
    def __init__(self):
        self.inventory = [items.gold(5),items.rock(),items.moldy_bread()]
        self.hp = 100
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        
    def is_alive(self):
        return self.hp > 0
    
    def print_inventory(self):
        for item in self.inventory:
            print(item, '\n')


# In[ ]:


    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)


# In[ ]:


    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)


# In[ ]:


    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0

        for i in self.inventory:
            if isinstance(i, items.weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i

        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}!".format(enemy.name))
        else:
            print("{} HP is {}".format(enemy.name, enemy.hp))


# In[ ]:


    def flee(self, tile):
         """Moves the player randomly to an adjacent tile"""
         available_moves = tile.adjacent_moves()
         r = random.randint(0, len(available_moves) - 1)
         self.do_action(available_moves[r])


# In[ ]:


    def heal(self):
        consumables = [item for item in self.inventory 
                      if isinstance(item, items.consumable)]
        if not consumables:
            print("Don't try to heal when you ain't got no items to heal, fool!")
            return

        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}. {}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 1]
                self.hp = min(100, self.hp + to_eat.heal_value)
                self.inventory.remove(to_eat)
                print("Delicious. current HP: {}".format(self.hp))
                valid = True
            except (ValueError, IndexError):
                print("Wrong choice, pal. Try again.")

