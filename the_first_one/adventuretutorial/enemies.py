
# coding: utf-8

# In[ ]:


class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        
    def is_alive(self):
        return self.hp > 0


# In[ ]:


class sketchy_guy(Enemy):
    def __init__(self):
        super().__init__(name="Sketchy guy",
                        hp=10,
                        damage=2)


# In[ ]:


class ogre(Enemy):
    def __init__(self):
        super().__init__(name="Ogre",
                        hp=30,
                        damage=20)


# In[ ]:


class zombie(Enemy):
    def __init__(self):
        super().__init__(name="Zombie",
                        hp=20,
                        damage=10)

