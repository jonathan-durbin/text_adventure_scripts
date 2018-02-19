import items

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