
# coding: utf-8

# In[1]:


import items, enemies, actions, world


# In[ ]:


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self):
        raise NotImplementedError()

    def modify_player(self, player):
        raise NotImplementedError()
    
    def adjacent_moves(self):
        '''Returns all move actions for adjacent tiles'''
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
    
    def available_actions(self):
        '''Returns all of the available actions in this room.'''
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        
        return moves
    


# In[ ]:


class StartingRoom(MapTile):
    def intro_text(self):
        return '''
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        '''
    
    def modify_player(self, player):
        #Room has no action on the player
        pass


# In[ ]:


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def add_loot(self, player):
        player.inventory.append(self.item)
        
    def modify_player(self, player):
        self.add_loot(player)
        
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
        
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, the_player.hp))
            
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return '''
        You see a bright light in the distance. 
        It grows as you get closer.
        It's sunlight!
        
        Victory is yours!
        '''
    
    def modify_player(self, player):
        player.victory = True


# In[ ]:


class EmptyCavePath(MapTile):
    def intro_text(self):
        return '''
        Another unremarkable part of the cave. Moving on...
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x,y,enemies.GiantSpider())
    
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            A giant flippin spider jumps down from hiding! It attacks!
            '''
        else:
            return '''
            The nasty corpse of a dead spider rots on the floor. So nasty.
            '''

class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.Ogre())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            An angry Ogre sees you. It attacks!
            '''
        else:
            return '''
            A nasty Ogre corpse lies neatly placed on the ground. Very nasty.
            '''

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x,y,items.Dagger())
        
    def intro_text(self):
        return '''
        You notice something shiny on the floor...
        It's a dagger! You pick it up. 
        '''
    
class FindGoldRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Gold(5))
        
    def intro_text(self):
        return '''
        You notice something shiny on the floor...
        Gold! You pick it up.
        '''

