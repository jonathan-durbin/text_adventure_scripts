
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


class start_room(MapTile):
    def intro_text(self):
        return '''
        
        You are in a dimly lit room. You see four corridors, each spooky-looking.
        In the darkness, you spot a silver piece on the ground.
        You try to pick it up, but it's been glued to the floor.
        Frustrated and embarassed, you leave.
        
        '''
    
    def modify_player(self, player):
        #Room has no action on the player
        pass


# In[ ]:


class loot_room(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def add_loot(self, player):
        player.inventory.append(self.item)
        
    def modify_player(self, player):
        self.add_loot(player)
        
class enemy_room(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
        
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining".format(self.enemy.damage, 
                                                                       the_player.hp))
            
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class victory_room(MapTile):
    def intro_text(self):
        return '''
        
        You thought this labyrinth would become your home.
        You were wrong! You finally see sunlight up ahead.
        You made it!
        
        Victory is yours!
        
        '''
    
    def modify_player(self, player):
        player.victory = True


# In[ ]:


class empty_room(MapTile):
    def intro_text(self):
        return '''
        
        Ugh, such a boring room. 
        You daydream about your favorite meals as you pass through.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass


# In[ ]:


class dead_sad_room(MapTile):
    def intro_text(self):
        return '''
        
        You feel a wave of sadness and melancholy as you enter this room.
        In the corner you see a stuffed animal. Nothing's wrong with it, it just hasn't been touched in years.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass


# In[ ]:


class find_knife_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x,y,items.knife())
        
    def intro_text(self):
        return '''
        
        You notice something shiny on the floor...
        It's a knife! You pick it up. 
        This will help deal with those beasties whose screams you hear faintly.
        
        '''
    
class find_sword_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x,y,items.sword())
        
    def intro_text(self):
        return '''
        
        You notice something shiny on the floor...
        It's a big honkin' sword! You pick it up.
        All the beasties will fear your name.
        
        '''
    
class find_5_gold_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x, y, items.gold(5))
        
    def intro_text(self):
        return '''
        
        You notice something shiny on the floor...
        5 gold pieces! You pick them up.
        You also bite them, one by one. Yep, they're real.
        
        '''
    
class find_10_gold_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x, y, items.gold(10))
        
    def intro_text(self):
        return '''
        
        You notice something shiny on the floor...
        10 gold pieces! That seems like a lot! You pick them up.
        You also bite them, one by one. Yep, they're real.
        
        '''
    
class find_20_gold_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x, y, items.gold(20))
        
    def intro_text(self):
        return '''
        
        You notice something shiny on the floor...
        20 gold pieces! You have so much imaginary currency! You pick them up.
        You also bite them, one by one. Yep, they're real.
        
        '''
    


# In[ ]:


class sketchy_guy_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x,y,enemies.sketchy_guy())
    
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A really sketchy dude shambles up to you. 
            He attacks by throwing burning cigars.
            
            '''
        else:
            return '''
            
            The nasty corpse of a sketchy guy rots on the floor. So nasty. So sketchy.
            
            '''

class ogre_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.ogre())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            An angry, gross-smelling Ogre sees you. It attacks!
            You ready your weapon, after you recover from the awful stench.
            
            '''
        else:
            return '''
            
            A nasty Ogre corpse lies neatly placed on the ground. Very nasty. Very neat.
            
            '''
class zombie_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.zombie())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A zombie sees you. It wants your brain. 
            You ready your weapon, after you recover from the shock of seeing a zombie.
            
            '''
        else:
            return '''
            
            A nasty zombie corpse is spread all over the walls, like peanut butter on bread. Very tasty.
            
            '''


# In[ ]:


class interesting_1_room(MapTile):
    def intro_text(self):
        return '''
        
        The hallway opens up into a huuuuge circular chamber. 
        The ceiling is so high, you can't see where it ends. 
        The walls are adorned with tribal paintings. 
        The paintings are so intricate, you keep seeing more details the closer you look
        There's nothing to do in this room. It's just kinda interesting.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class interesting_2_room(MapTile):
    def intro_text(self):
        return '''
        
        As you leave the hallway, it's like you're transported to a western-style cowboy bar
        You try to say something to the patrons, but they're not moving.
        Everyone here blankly stares forward, slightly hunched over.
        There's not really anything to do in this room, but it is kinda interesting.
        You're equally creeped out and interested, so you hurry on.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class interesting_3_room(MapTile):
    def intro_text(self):
        return '''
        
        You see a light up ahead. Could it possibly be the exit?
        No, it's a small square room with tons of silver coins glued to the floor, ceiling, and walls.
        The light is coming from a single torch stuck in the middle of the floor. 
        It's reflecting quite beautifully - it's dazzling to look at.
        There's not really anything to do in this room, but it is kinda interesting.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class interesting_4_room(MapTile):
    def intro_text(self):
        print("""As you walk into this room, a man in a suit adresses you.
        "Hello there, would you like my help? I can protect you from the dangers of this place."
        
        You silently stare at him, unable to talk. This is the first time someone has talked to you here.
        
        As you stare, you see one of his hands is hidden behind his back.
        
        Will you trust him?
        """)
        ans = input("Trust? yes [y] or no [n] :")
        
        if ans == 'y':
            return '''
            
            You decide to trust him. right before you say anything, however, he vanishes in a puff of smoke.
            Looks like either you took too long deciding, or this is just another strange (but interesting) room.
            
            '''
        elif ans != 'y':
            return '''
            
            You really must not trust this guy. You move on past the room.
            On the way out, you pause and contemplate how interesting this room is.
            
            '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class interesting_5_room(MapTile):
    def intro_text(self):
        return '''
        
        As you enter this room, you see nothing except a book standing up on the ground.
        The book is also upside down.
        It's title is in an unreadable language, but you can still tell it's upside-down.
        How can you tell that the book is upside-down?
        Well, that's the interesting part.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass


# In[ ]:


class note_1_room(MapTile):
    def intro_text(self):
        return '''
        
        You see a note on the ground. You pick it up. 
        It says "don't look behind you."
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class note_2_room(MapTile):
    def intro_text(self):
        return '''
        
        You see a note on the ground. You pick it up.
        It says "look behind you."
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class note_3_room(MapTile):
    def intro_text(self):
        return '''
        
        You see a note on the ground. You pick it up.
        It says "please, i just want to surv---"
        It cuts out before the sentence ends. What was this person thinking?
        Probably an uncivilized chap.
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass
    
class note_4_room(MapTile):
    def intro_text(self):
        return '''
        
        You see a note on the ground. You pick it up.
        It says "my parents abandoned me when i was young. i was raised by elk. they abandoned me too."
        Poor elk :(
        
        '''
    def modify_player(self, player):
        # Room has no action on the player
        pass

