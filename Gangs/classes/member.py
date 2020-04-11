import random
from classes.namebase import dwarf

class Member:

    """
    Master class for generic gang member 'Thug'
    """

    id = 0
    member_dict = {}

    def __init__(self, gang):
        self.name = self.namer(dwarf)
        self.archetype = 'Thug'
        self.gang = gang
        self.level = 0
        self.xp = 0
        self.gear = 0
        
        self.id = Member.id
        Member.member_dict[self.id] = self
        Member.id += 1

    # Give the gang member 1 xp if they aren't at the cap
    def get_xp(self):
        if self.level < 10:
            xp_requirement = (self.level+1)**2
            self.xp += 1
            if self.xp >= xp_requirement:
                self.xp = 0
                self.level += 1
            print(f'{self.name} is level {self.level}. ({self.xp}/{xp_requirement})\n')

    # Makes gang member the boss
    def make_boss(self):
        self.archetype = 'Boss'
        # self.loyalty = 100

    def namer(self, race):
        return random.choice(race.male_names+race.female_names) + ' ' + random.choice(race.surnames)

