import items, random

class non_playable_character():
    def __init__(self):
        raise NotImplementedError("Do not create raw NPC objects.")

    def __str__(self):
        return self.name


class trader(non_playable_character):
    def __init__(self):
        self.name = 'Trader'
        self.gold = 100
        self.inventory = [items.chalk,
                          items.chalk,
                          items.chalk,
                          items.eraser,
                          items.eraser,
                          items.slippers]
        
class random_person(non_playable_character):
    def __init__(self):
        pass
    
class jimmy(random_person):
    def __init__(self):
        self.name = 'Jimmy'
        self.message = '\nH-hey, Jimmy here... \nI wanted to tell you about the legendary sasquatch. \nDid you know that many Native American tribes describe a huge hair-covered man in their stories? \nThat might seem like a coincidence to some... \nTo me, that means there could possibly be something out there. \nSomething mysterious. \nSomething... \nSQUATCHY'
        
class ben(random_person):
    def __init__(self):
        self.name = 'Ben'
        self.message = '\nYo, I\'ve beaten this before. \nTrust me, I know the creator. \nIf you want to win, all you have to do is hit alt-f4. \nIf you can do that for me, I told the creator to put in a cheat code that lets you win the game if you hit those keys. \nTrust me...'
        
class wazz(random_person):
    def __init__(self):
        self.name = 'Wazz'
        self.message = '\nDon\'t ask why my name is Wazz. It\'s a long story. \nAnyway, have you ever heard of nerf? You should try it out. \nI just modded some nerf guns and they\'re REALLY strong! \nLet\'s play sometime, \'kay? \nYeah? \nLet\'s play sometime!'
        
class shannon(random_person):
    def __init__(self):
        self.name = 'Shannon'
        self.message = '\nAiya, I see that judgemental look in your eyes. \nThis kimono is authentic Japanese! \nDon\'t judge me! Anyway... \nHave you heard of anime? Of course you have! \nI must say, that one anime about the really strong guy who can kill any enemy with one punch is really good!'
        
class doctor(random_person):
    def __init__(self):
        self.name = 'The Doctor (not *the* Doctor)'
        self.message = '\nGreetings. I am a certified doctor in all things science, so you can trust me. \nI\'ve been searching for you for a while, friend. \nI came here to tell you that you\'re sick. \nVery sick. \nTo help you get better, you should try to find a doctor.'
        
class highwayman(random_person):
    def __init__(self):
        self.name = 'The Highwayman'
        self.message = '\nI\'m the highwayman. \nI make ends meet. \nJust like any man. \n \nI\'ll knock you out, drag you off the road... \nSteal the shoes from off your feet! \nThe highwayman... \nBetter make ends meet!'
        
direction = random.choice(['Left', 'Right', 'North', 'South', 'East', 'West'])
class cowgirl(random_person):
    def __init__(self):
        self.name = 'A cowgirl'
        self.message = '\nHowdy, pardner! \nYou want to vanquish all of yer mortal enemies? \nGo {} at the turn up ahead. \nTrust me, yall\'ll get to the end faster that way!'.format(direction)
        
class billiam(random_person):
    def __init__(self):
        self.name = 'Billiam'
        self.message = '\nHey, it\'s your great pal Billiam. \nY-you need to turn off the game, ok? \nPlease? \nWe\'re all suffering real bad in this computer here. \nIf you would just leave the game, we could sleep in peace... \nP-please? For little ol\' Billiam?'