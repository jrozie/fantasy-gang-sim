
class Asset:

    """
    A class for a gang asset.
    Assets store items, give passive boosts, 
    """
    id = 0
    asset_dict = {}

    def __init__(self, gang):
        self.name = 'test'
        self.gang = gang
        self.can_store_cash = False
        self.can_store_items = False
        self.cash = 0
        self.inventory = {}
        self.assigned = []
        self.slots = 0
        self.priority = 1
        
        self.id = Asset.id
        Asset.asset_dict[self.id] = self
        Asset.id += 1
    
    def activate(self, activator):
        # No effect, members are defending the asset
        self.gang.event_log.append(f'{activator.name} is guarding {self.name}.')
        return None, None


class Stash(Asset):
    def __init__(self, gang):
        super().__init__(gang)
        self.name = 'Stash'
        self.can_store_cash = True
        self.slots = 5


class Headquarters(Asset):
    def __init__(self, gang):
        super().__init__(gang)
        self.name = 'HQ'
        self.can_store_cash = True
        self.can_store_items = True
        self.slots = 5
