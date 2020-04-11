

class Asset:

    """
    A class for a gang asset.
    Assets store items, give passive boosts, 
    """
    id = 0
    asset_dict = {}

    def __init__(self):
        self.name = 'Stash'
        self.can_store_cash = True
        self.can_store_items = False
        self.cash = 0
        self.inventory = {}
        
        self.id = Racket.id
        Racket.racket_dict[self.id] = self
        Racket.id += 1