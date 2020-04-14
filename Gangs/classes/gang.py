#%%
import random
from classes.racket import Racket
from classes.asset import Asset
from classes.member import Thug
from classes.member import Boss

class Gang:
    """
    Master Class for gang objects to handle their stats and interactions
    """

    id = 0
    gang_dict = {}

    def __init__(self, name, initial_members=10):
        self.name = name
        self.members = {}
        self.boss = None
        self.rackets = {}
        self.assets = {}
        
        self.add_asset(cost=0)
        self.add_racket(cost=0)
        self.earn(initial_members*3)
        self.recruit_boss()
        self.recruit(initial_members, cost=0)

        # self.boss = self.members[max(self.members, key=lambda x: self.members[x].level)]
        # self.boss.make_boss()

        self.get_status()
        
        self.id = Gang.id
        Gang.gang_dict[self.id] = self
        Gang.id += 1

    # creates a new racket that provides income/gear
    def add_racket(self, cost=100):
        if self.spend(cost):
            racket = Racket(self)
            self.rackets[racket.id] = racket
            return True
        else:
            return False

    # creates a new asset that stores cash/gear
    def add_asset(self, cost=100):
        if self.spend(cost):
            asset = Asset(self)
            self.assets[asset.id] = asset
            return True
        else:
            return False

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
        return sum(self.assets[n].cash for n in self.assets)

    def count_income(self):
        return sum(self.rackets[n].income * len(self.rackets[n].assigned) for n in self.rackets)

    # Add [n] new members to self.members
    # Costs 1 cash
    def recruit(self, n, cost=1):
        for i in range(n):
            if self.spend(cost):
                member = Thug(self)
                self.members[member.id] = member
            else:
                return False
        return True

    def recruit_boss(self):
        member = Boss(self)
        self.members[member.id] = member
        self.boss = member
        return True

    # Gets Gang Strength
    def get_strength(self):
        return sum(self.members[n].level for n in self.members)

    # List the members and their stats
    def get_status(self):
        print(f'{self.name}\nRoster:')
        for n in self.members:
            member = self.members[n]
            print(f'{member.name} ({member.archetype}):\n    Level: {member.level} ({member.xp}/{member.xp_requirement}) Gear: {member.gear}')
        print(f'\nRackets:  Total Income: {self.count_income()}')
        for n in self.rackets:
            racket = self.rackets[n]
            print(f'{racket.name}:\n    Income: {racket.income}')
        print(f'\nAssets:\n  Total Cash: {self.count_cash()}')
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
            except IndexError or KeyError:  # Not a valid id
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

    # assigns a member to a racket or asset
    def assign_member(self, id=None):
        member = self.get_member(id)
        if not member:
            return False
        if member == self.boss:
            return False
        assign_to = [None]
        weights = [1]
        for n in self.assets:
            weight = self.assets[n].slots - len(self.assets[n].assigned)
            if weight > 0:
                assign_to.append(self.assets[n])
                weights.append(weight)
        for n in self.rackets:
            weight = self.rackets[n].slots - len(self.rackets[n].assigned)
            if weight > 0:
                assign_to.append(self.rackets[n])
                weights.append(weight)
        if len(assign_to) > 0:
            member.assigned_to = random.choices(assign_to, weights)[0]
            if member.assigned_to is not None:
                member.assigned_to.assigned.append(member)
            return True
        else: 
            return False

    # The gang members take their actions then pay upkeep
    def activate(self):
        # make sure members have a job then activate members

        for n in self.assets:
            self.assets[n].assigned = []
        for n in self.rackets:
            self.rackets[n].assigned = []
        
        recruitment = 0
        for n in self.members:
            member = self.members[n]
            self.assign_member(n)
            resource, output = member.activate()
            if resource == 'cash':
                self.earn(output)
            elif resource == 'recruit':
                recruitment += output
            elif resource == 'add racket':
                self.add_racket()
        loyalty_check = []
        for n in self.members:
            member = self.members[n]
            if not self.spend(member.upkeep):
                # hasn't been paid :(
                loyalty_check.append(n)
        for n in loyalty_check:
            if self.members[n] != self.boss:
                self.remove_member(n)
        self.recruit(recruitment)



# %%
