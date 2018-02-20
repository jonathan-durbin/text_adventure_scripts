''' Parent class for items with following basic attributes: name, description, value'''

class item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        
''' Parent classes for three main types of items, each with added descriptions'''

class heal_item(item):
    def __init__(self, name, description, value, healing_points):
        self.healing_points = healing_points
        super().__init__(name, description, value)
        
    def __str__(self):
        return '{} \n ========== \n{} \n ========== \nValue: {} \nHealing Points: {} \n ========== '.format(self.name, self.description, self.value, self.healing_points)

class weapon_item(item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
        
    def __str__(self):
        return '{} \n ========== \n{} \n ========== \nValue: {} \nDamage: {} \n ========== '.format(self.name, self.description, self.value, self.damage)

class note_item(item):
    def __init__(self, name, description, value, writing):
        self.writing = writing
        super().__init__(name, description, value)
        
    def __str__(self):
        return '{} \n ========== \n{} \n ========== \nValue: {} \nWriting: {} \n ========== '.format(self.name, self.description, self.value, self.writing)

#''' Currency is important! '''
#class gold_item(item):
#    def __init__(self, worth):
#        self.worth = worth
#        super().__init__(name="Gold",
#                         description="Looks like about {} worth of gold. Beautiful, pure, #gold.".format(str(self.worth)),
#                         value=self.worth)
#        
''' Healing items put in this section '''

class chalk(heal_item):
    def __init__(self):
        super().__init__(name = 'Chalk',
                         description = 'A piece of brand-new white chalk. Unfortunately it\'s bite-sized, so it won\'t heal you much.',
                         value = 5,
                         healing_points = 10)

class eraser(heal_item):
    def __init__(self):
        super().__init__(name = 'Eraser', 
                         description = 'An eraser! Lightly dusted. It has the faint smell of chalk on it.',
                         value = 10,
                         healing_points = 25)
        
class slippers(heal_item):
    def __init__(self):
        super().__init__(name = 'Slippers', 
                         description = 'Two identical slippers. Soft to the touch. Very valuable. An important commodity for any scientist.', 
                         value = 30,
                         healing_points = 50)

''' Weapons put in this section '''

first_law = weapon_item(name = 'The First Law', 
                        description = 'Damage dealt to me hurts, but damage dealt to an enemy hurts more.',
                        value = 15,
                        damage = 13)

second_law = weapon_item(name = 'The Second Law',
                         description = 'Enemies won\'t be able to tell where I\'m coming from. Conservation of Energy is violated',
                         value = 17.6,
                         damage = 19)

third_law = weapon_item(name = 'The Third Law',
                        description = 'Blinded by my fast attacks! Face the justice of the universe, enemies!',
                        value = 21.9,
                        damage = 29)

zeroth_law = weapon_item(name = 'The Zeroth Law',
                         description = 'Decrease the total entropy of the universe! My attacks will vaporize my enemies.',
                         value = 29.4,
                         damage = 37)

''' Put notes here '''

class atbash_note(note_item):
    def __init__(self):
        super().__init__(name = 'A mysterious note',
                         description = 'This note has hastily drawn scribbles all over it, most of them unintelligible. You can only read a small section. \nIn the corner of this paper, you see small writing that says \"@BASH\".',
                         value = 4,
                         writing = 'Vevib grnv R orxp z hgznk, R xlmhfnv z gvmgs lu z xzolirv.')

class base64_note(note_item):
    def __init__(self):
        super().__init__(name = 'A mysterious note',
                         description = 'This note glows faintly. On it are recognizable runes and symbols, but in no discernable order. \nIn the corner you see written \"64\".',
                         value = 5,
                         writing = 'U3R1ZGllcyBzaG93IHRoYXQgaWYgYSBjYXQgZmFsbHMgb2ZmIHRoZSBzZXZlbnRoIGZsb29yIG9mIGEgYnVpbGRpbmcgaXQgaGFzIGFib3V0IHRoaXJ0eSBwZXJjZW50IGxlc3MgY2hhbmNlIG9mIHN1cnZpdmluZyB0aGFuIGEgY2F0IHRoYXQgZmFsbHMgb2ZmIHRoZSB0d2VudGlldGggZmxvb3IuIEl0IHN1cHBvc2VkbHkgdGFrZXMgYWJvdXQgZWlnaHQgZmxvb3JzIGZvciB0aGUgY2F0IHRvIHJlYWxpemUgd2hhdCBpcyBvY2N1cnJpbmcsIHJlbGF4IGFuZCBjb3JyZWN0IGl0c2VsZi4=')

class caesarian_6_note(note_item):
    def __init__(self):
        super().__init__(name = 'A mysterious note',
                         description = 'This note smells like someone\'s smelly aunt. Not your own, of course. In the corner you see written \"Hail Caesar\".',
                         value = 3,
                         writing = 'Nby upyluay jylmih mjyhxm 6 gihnbm iz nbycl fczy mcnncha un lyx fcabnm.')
        

class morse_note(note_item):
    def __init__(self):
        super().__init__(name = 'A mysterious note',
                        description = 'This note is soft. It reminds you of a nice peach. In the corner, you see written \"Morose\".',
                        value = 6,
                        writing = '--- -. . / --.- ..- .- .-. - . .-. / --- ..-. / - .... . / -... --- -. . ... / .. -. / -.-- --- ..- .-. / -... --- -.. -.-- / .- .-. . / .. -. / -.-- --- ..- .-. / ..-. . . - .-.-.-')