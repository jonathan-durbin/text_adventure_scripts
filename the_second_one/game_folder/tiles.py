import items, enemies, actions, world, npc, random
from player_file import player

class map_tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def intro_text(self):
        raise NotImplementedError('do this in the sub-class!')

    def modify_player(self, player):
        raise NotImplementedError('do this in the sub-class!')
    
    def adjacent_moves(self):
        '''Returns all move actions for adjacent tiles'''
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.move_east())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.move_west())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.move_north())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.move_south())
        return moves
    
    def available_actions(self):
        '''Returns all of the available actions in this room.'''
        moves = self.adjacent_moves()
        moves.append(actions.view_inventory())
        print(player().hp)
        if player().hp < 100:
            moves.append(player.heal())
        if world.tile_exists(self.x, self.y) == 'trader_room':
            moves.append(actions.Trade())
            
        moves.append(actions.Quit())
        
        return moves
    
''' Start room defined here. '''

class start_room(map_tile):
    def intro_text(self):
        return '''
        
        I am in a room. It looks like my bedroom.
        It's not my bedroom. Time to exact justice.
        
        '''
    
    def modify_player(self, player):
        #Room has no action on the player
        pass

class victory_room(map_tile):
    def intro_text(self):
        return '''
        
        I thought I would never leave this weird place. 
        Nay! I see light up ahead! Real, unfiltered light!
        I made it to the end! 
        
        Victory is mine!
        
        '''
    
    def modify_player(self, player):
        player.victory = True
        
''' Here, rooms that inform the player of things are defined. '''

class creepy_chamber_room(map_tile):
    def intro_text(self):
        return '''
        
        I felt a chill when I walked into this room. I don't see anything currently.
        This chill reminds me that there is always a greater evil that needs to be vanquished.
        My heart starts to pound, ready for the next battle.
        
        '''
    
    def modify_player(self, player):
        pass
    
class long_hallway(map_tile):
    def intro_text(self):
        return '''
        
        A long hallway stretches before me. 
        Sunlight streams in from stained glass windows on both sides of me.
        For a moment, I can rest.
        
        '''
    
    def modify_player(self, player):
        pass
    
class split_2_room(map_tile):
    def intro_text(self):
        return '''
        
        I step into a room that splits into two. 
        I look down both corridors, but only see darkness.
        
        '''
    
    def modify_player(self, player):
        pass
    
class split_3_room(map_tile):
    def intro_text(self):
        return '''
        
        I step into a room that splits into three.
        I look down the three corridors, but only see darkness.
        
        '''
    
    def modify_player(self, player):
        pass
    
''' Trader room goes here '''

class trader_room(map_tile):
    def __init__(self, x, y):
        self.trader = npc.trader()
        super().__init__(x, y)
        
    def trade(self, buyer, trader):
        for i, item in enumerate(trader.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
        
        while True:
            user_input = input("Choose an item or press \"q\" to exit: ")
            if user_input == 'q':
                return
            
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                
                except ValueError:
                    print("Invalid choice!")
                    
    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")
        
    def check_if_trade(self, player):
        while True:
            print("Would you like to (b)uy, (s)ell, or (q)uit?")
            user_input = input()
            
            if user_input in ['Q', 'q']:
                return
            
            elif user_input in ['B', 'b']:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            
            elif user_input in ['S', 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            
            else:
                print("Invalid choice!")
                
    def intro_text(self):
        return '''
        
        I see a frail man sitting in a cardboard box. 
        He has gold coins scattered all over the floor.
        He beckons to me.
        Looks like he wants to trade.
        
        '''
    
    def modify_player(self, player):
        pass

''' Here, the enemy rooms are defined. '''

class reg_enemy_room(map_tile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
        
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The enemy does {} damage. I have {} HP remaining".format(self.enemy.damage, player.hp))
            
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

class boss_room(map_tile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
        
    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("The great evil does {} damage. I have {} HP remaining".format(self.enemy.damage, player.hp))
            
        if not self.enemy.is_alive():
            player.inventory.append(self.enemy.weapon)
            print('The great evil is dead. I take the weapon they wielded against me as my own. I now use {}.'.format(self.enemy.weapon))
            
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()

''' Boss rooms go here '''

class huge_floating_skull_bossroom(boss_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.huge_floating_skull())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A floating skull the size of my aunt Bertha attacks me.
            It starts by launching fireballs from its eyes.
            
            '''
        else:
            return '''
            
            I have vanquished the huge floating skull. 
            Its remains remind me of that one time aunt Bertha fell off the swing set.
            
            '''
        
class huge_judge_bossroom(boss_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.huge_judge())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A judge sits on a large podium. The judge is also large.
            He looms over me and tries to pound me with his gavel.
            I won't have it!
            
            '''
        else:
            return '''
            
            The defeated judge lies over the podium he once owned.
            I use my Law to smite him one last time, out of spite.
            
            '''
        
class little_boy_bossroom(boss_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.little_boy())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A little boy offers me candy. I refuse. He decides to fight me.
            He's very strong. I may die.
            
            '''
        else:
            return '''
            
            The child is vanquished. I have the Law he used against me.
            Should have given me better candy!
            
            '''

''' Regular enemy rooms go here '''

class zombie_room(reg_enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.zombie())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A zombie attacks! It looks hungry. It doesn't look like anyone I know.
            
            '''
        else:
            return '''
            
            The corpse of a slain zombie lies here. I try to ignore the smell.
            I must move on.
            
            '''
        
class stitched_monster_room(reg_enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.stitched_monster())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            From the shadows of the room, a monster shambles towards me.
            It's covered in stiches - a menagerie of flesh and bone.
            It looks sad. I'll put it out of its misery.
            
            '''
        else:
            return '''
            
            A slain monster covered in stitches lies sprawled on the ground.
            A faint smile covers its face. I'm glad I removed this one.
            
            '''
        
class sketchy_guy_room(reg_enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.sketchy_guy())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            A really sketchy guy approaches me. He's wearing the whole shebang.
            Hoody, tattered pants, weird look in his eyes.
            From within his sleeve, I see a knife flash. He attacks!
            
            '''
        else:
            return '''
            
            A sketchy - looking corpse lies on the ground. 
            It's from that sketchy guy I killed earlier
            
            '''
        
class crazy_guy_room(reg_enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.crazy_guy())
        
    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            
            I hear howling as I enter the room. A guy with a wild look in his eyes approaches.
            He goes "Pew! Pew! Pew!" Like he's trying to shoot me.
            What he's actually doing is trying to slash me open.
            
            '''
        else:
            return '''
            
            As I walk past the corpse of the crazy guy, I hear a faint "...pew..."
            At least, I think I did...
            
            '''

''' Loot rooms here. '''

class find_5_gold_room(map_tile):
    def __init__(self, x, y):
        self.gold = 5
        self.gold_claimed = False
        super().__init__(x, y)
        
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return '''
            
            I think this is where I found that gold earlier.
            
            '''
        else:
            return '''
            
            I see some gold coins scattered on the floor. Sweet! It's not many, but it's still good.
            I'll take them.
            
            '''
        
class find_10_gold_room(map_tile):
    def __init__(self, x, y):
        self.gold = 10
        self.gold_claimed = False
        super().__init__(x, y)
        
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return '''
            
            I think this is where I found that gold earlier.
            
            '''
        else:
            return '''
            
            I see some gold coins scattered on the floor. Sweet!
            I'll take them.
            
            '''
        
class find_15_gold_room(map_tile):
    def __init__(self, x, y):
        self.gold = 15
        self.gold_claimed = False
        super().__init__(x, y)
        
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return '''
            
            I think this is where I found that gold earlier.
            
            '''
        else:
            return '''
            
            I see some gold coins scattered on the floor. Sweet! Looks like a lot!
            I'll take them.
            
            '''
        
class find_20_gold_room(map_tile):
    def __init__(self, x, y):
        self.gold = 20
        self.gold_claimed = False
        super().__init__(x, y)
        
    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} gold added.".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return '''
            
            I think this is where I found that gold earlier.
            
            '''
        else:
            return '''
            
            I see some gold coins scattered on the floor. Sweet! This looks like a lot!
            I'll take them.
            
            '''
        
''' Sub-class for loot rooms. '''

class loot_room(map_tile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def add_loot(self, player):
        player.inventory.append(self.item)
        
    def modify_player(self, player):
        self.add_loot(player)

        
class find_chalk_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x, y, items.chalk())
        
    def intro_text(self):
        return '''
        
        I see a lone piece of chalk on the floor. Score! This stuff is delicious.
        
        '''
    
class find_eraser_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x, y, items.eraser())
        
    def intro_text(self):
        return '''
        
        I spy an eraser attached to a string hanging from the ceiling. Awesome!
        Even better than chalk, these things are super good for me.
        
        '''
    
class find_slippers_room(loot_room):
    def __init__(self, x, y):
        super().__init__(x, y, items.slippers())
        
    def intro_text(self):
        return '''
        
        I see slippers! Nailed to the wall! I'll take them. Even better, they're made out of leather.
        These might be the most delicious things I have ever tasted.
        
        '''
    
''' Random encounter rooms go here. '''

class random_person_room(map_tile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.125:
            self.random_person = npc.jimmy()
        elif r < 0.25:
            self.random_person = npc.ben()
        elif r < 0.375:
            self.random_person = npc.wazz()
        elif r < 0.5:
            self.random_person = npc.shannon()
        elif r < 0.625:
            self.random_person = npc.doctor()
        elif r < 0.75:
            self.random_person = npc.highwayman()
        elif r < 0.875:
            self.random_person = npc.cowgirl()
        else:
            self.random_person = npc.billiam()
            
        super().__init__(x, y)
        
    def intro_text(self):
        print('\nI walk into the next room. \nA stranger greets me. \nThey say their name is {}. \nThey have something to say...'.format(self.random_person.name), '\n =========== \n', self.random_person.message)
        return ' '
    
    def modify_player(self, player):
        pass
    
''' Note rooms go here. '''

class note_room(map_tile):
    def __init__(self, x, y, note):
        self.note = note
        super().__init__(x, y)
        
    def add_note(self, player):
        player.inventory.append(self.note)
        
    def modify_player(self, player):
        self.add_note(player)
        
class atbash_room(note_room):
    def __init__(self, x, y):
        self.note_claimed = False
        super().__init__(x, y, items.atbash_note())
        
    def modify_player(self, player):
        if not self.note_claimed:
            self.note_claimed = True
            player.inventory.append(items.atbash_note())

    def intro_text(self):
        if self.note_claimed:
            return '''
            
            I see an empty room. This might have been where I found that note...
            
            '''
        else:
            return '''
            
            I see a mysterious note on the ground. I pick it up. Cool!
            
            '''
        
class base64_room(note_room):
    def __init__(self, x, y):
        self.note_claimed = False
        super().__init__(x, y, items.base64_note())
        
    def modify_player(self, player):
        if not self.note_claimed:
            self.note_claimed = True
            player.inventory.append(items.base64_note())

    def intro_text(self):
        if self.note_claimed:
            return '''
            
            I see an empty room. This might have been where I found that note...
            
            '''
        else:
            return '''
            
            I see a mysterious note on the ground. 
            It's glowing... 
            I pick it up. Cool!
            
            '''
        
class caesarian_6_room(note_room):
    def __init__(self, x, y):
        self.note_claimed = False
        super().__init__(x, y, items.caesarian_6_note())
        
    def modify_player(self, player):
        if not self.note_claimed:
            self.note_claimed = True
            player.inventory.append(items.caesarian_6_note())

    def intro_text(self):
        if self.note_claimed:
            return '''
            
            I see an empty room. This might have been where I found that note...
            
            '''
        else:
            return '''
            
            I see a mysterious note on the ground. It's stinky... 
            I pick it up. Cool!
            
            '''
        
class morse_room(note_room):
    def __init__(self, x, y):
        self.note_claimed = False
        super().__init__(x, y, items.morse_note())
        
    def modify_player(self, player):
        if not self.note_claimed:
            self.note_claimed = True
            player.inventory.append(items.morse_note())

    def intro_text(self):
        if self.note_claimed:
            return '''
            
            I see an empty room. This might have been where I found that note...
            
            '''
        else:
            return '''
            
            I see a mysterious note on the ground. 
            I pick it up. It's soft to the touch! Cool!
            
            '''