import random
from classes.racket import Racket
from classes.asset import Asset
from classes.member import Member

class Gang:
    """
    Master Class for gang objects to handle their stats and interactions
    """

    id = 0
    gang_dict = {}

    def __init__(self, name, initial_members=10):
        self.name = name
        self.members = {}
        self.rackets = {}
        self.assets = {}
        
        self.add_asset()
        self.add_racket()
        self.earn(initial_members*3)
        self.recruit(initial_members)

        self.boss = self.members[max(self.members, key=lambda x: self.members[x].level)]
        self.boss.make_boss()

        self.get_status()
        
        self.id = Gang.id
        Gang.gang_dict[self.id] = self
        Gang.id += 1

    # creates a new racket that provides income/gear
    def add_racket(self):
        racket = Racket(self)
        self.rackets[racket.id] = racket

    # creates a new asset that stores cash/gear
    def add_asset(self):
        asset = Asset(self)
        self.assets[asset.id] = asset

    # sources money from assets to pay for things
    def spend(self, amount):
        if self.count_cash() >= amount:
            #can spend
            while amount > 0:
                spend_from = self.assets[max(self.assets, key=lambda  x: self.assets[x].cash)]
                if spend_from.cash >= amount:
                    spend_from.cash -= amount
                    amount = 0
                else:
                    amount -= spend_from.cash
                    spend_from.cash = 0
            return True
        else:
            return False

    # store money in an asset
    def earn(self, amount):
        stash_assets = []
        for asset_id in self.assets:
            if self.assets[asset_id].can_store_cash:
                stash_assets.append(asset_id)
        if len(stash_assets) > 0:
            self.assets[random.choice(stash_assets)].cash += amount
            return True
        else:
            return False

    # get total cash reserves
    def count_cash(self):
        cash = 0
        for n in self.assets:
            cash += self.assets[n].cash
        return cash

    # Add [n] new members to self.members
    # Costs 1 cash
    def recruit(self, n, cost=1):
        for i in range(n):
            if self.spend(cost):
                member = Member(self)
                self.members[member.id] = member
            else:
                return False
        return True

    # List the members and their stats
    def get_status(self):
        print(f'{self.name}\nRoster:')
        for n in self.members:
            member = self.members[n]
            print(f'{member.name} ({member.archetype}):\n    Level: {member.level} ({member.xp}/{(member.level+1)**2}) Gear: {member.gear}')
        print('\nRackets:')
        for n in self.rackets:
            racket = self.rackets[n]
            print(f'{racket.name}:\n    Income: {racket.income}')
        print('\nAssets:')
        for n in self.assets:
            asset = self.assets[n]
            print(f'{asset.name}:\n    Stored Cash: {asset.cash}')
        print('\n')
    
    # Checks if given id is in gang or gets random member
    # if id is not in gang returns False
    def get_member(self, id=None):
        if id is None:
            try:
                member = self.members[random.choice([i for i in self.members])]
            except IndexError:  # No valid choices
                return False
        else:
            try:
                member = self.members[id]
            except IndexError:  # Not a valid id
                return False
        return member

    # Train a gang member to give them 1xp
    # Costs their current level in cash
    def train(self, id=None):
        member = self.get_member(id)
        if not member:
            return False
        # if self.cash >= member.level:
        #     self.cash -= member.level
        member.get_xp()
        return True
        # else:
        #     return False

    # Upgrade a gang member to gear level [tier]
    # Requires 
    def equip(self, tier, id=None):  
        member = self.get_member(id)
        if not member:
            return False
        if member.gear >= tier:
            # Can't upgrade
            return False
        else:
            member.gear = tier
            return True

    # Remove a member from the gang
    def remove_member(self, id=None):
        member = self.get_member(id)
        if not member:
            return False
        member.gang = None
        del(self.members[member.id])
        return True
