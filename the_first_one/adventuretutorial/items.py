
# coding: utf-8

# In[ ]:


class item():
# The base class for all items
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, 
                                                   self.description, 
                                                   self.value)


# In[ ]:


class gold(item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                        description="You have {} gold. \nNot that it matters or anything.".format(str(self.amt)),
                        value=self.amt)


# In[ ]:


class weapon(item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
        
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, 
                                                             self.description, 
                                                             self.value, 
                                                             self.damage)

class consumable(item):
    def __init__(self, name, description, heal_value):
        self.heal_value = heal_value
        super().__init__(name, description, heal_value)
        
    def __str__(self):
        return "{} (+{} HP)".format(self.name, self.heal_value)


# In[ ]:


class rock(weapon):
    def __init__(self):
        super().__init__(name="Rock",
                        description="A fist-sized rock, suitable for bludgeoning.",
                        value=0,
                        damage=5)

class knife(weapon):
    def __init__(self):
        super().__init__(name="Knife",
                        description="A small knife with a rusty blade. \nSomewhat more dangerous than a rock.",
                        value=10,
                        damage=10)

class sword(weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="Hacky and slashy. Much more so than that old knife.",
                         value=30,
                         damage=20)
        
# In[ ]:


class moldy_bread(consumable):
    def __init__(self):
        super().__init__(name = "Moldy Bread",
                         description="Half a loaf of bread. It smells nasty. \nLooks like it tastes nasty too. \nIt can heal you, though.",
                         heal_value=10)

