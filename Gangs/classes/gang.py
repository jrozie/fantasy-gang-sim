from classes.racket import Racket
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

    # sources money from rackets to pay for things
    def spend(self, amount):
        if self.count_cash() >= amount:
            #can spend
            while amount > 0:
                spend_from = self.rackets[max(self.rackets, key=lambda  x: self.rackets[x].cash)]
                if spend_from.cash >= amount:
                    spend_from.cash -= amount
                    amount = 0
                else:
                    amount -= spend_from.cash
                    spend_from.cash = 0
            return True
        else:
            return False

    # get total cash reserves
    def count_cash(self):
        cash = 0
        for n in self.rackets:
            cash += self.rackets[n].cash
        return cash

    # Add [n] new members to self.members
    # Costs 1 cash
    def recruit(self, n):
        for i in range(n):
            member = Member(self)
            self.members[member.id] = member

    # List the members and their stats
    def get_status(self):
        print(f'{self.name}\nRoster:')
        for n in self.members:
            member = self.members[n]
            print(f'{member.name} ({member.archetype}):\n    Level: {member.level} ({member.xp}/{(member.level+1)**2}) Gear: {member.gear}')
        print('Rackets:')
        for n in self.rackets:
            racket = self.rackets[n]
            print(f'{racket.name}:\n    Stored Cash: {racket.cash} Income: {racket.income}')
        print('\n')
    
    # Checks if given id is in gang or gets random member
    # if id is not in gang returns False
    # filter for min gear tier
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
