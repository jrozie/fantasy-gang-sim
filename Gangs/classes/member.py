#%%
import random


class Namebase:
    def __init__(self):
        self.male_names = [
        'Adrik', 'Alberich', 'Baern', 'Barendd', 'Brottor', 'Bruenor', 'Dain', 'Darrak', 'Delg', 
        'Eberk', 'Einkil', 'Fargrim', 'Flint', 'Gardain', 'Harbek', 'Kildrak', 'Morgran', 'Orsik', 
        'Oskar', 'Rangrim', 'Rurik', 'Taklinn', 'Thoradin', 'Thorin', 'Tordek', 'Traubon', 'Travok', 
        'Ulfgar', 'Veit', 'Vondal', 'Adrik', 'Alberich', 'Baern', 'Barendd', 'Beloril', 'Brottor', 
        'Dain', 'Dalgal', 'Darrak', 'Delg', 'Duergath', 'Dworic', 'Eberk', 'Einkil', 'Elaim', 'Erias', 
        'Fallond', 'Fargrim', 'Gardain', 'Ccur', 'Gimgen', 'Gimurt', 'Harbek', 'Kildrak', 'Kilvar', 
        'Morgran', 'Morkral', 'Nalral', 'Nordak', 'Nuraval', 'Oloric', 'Olunt', 'Skar', 'Rangfin1', 
        'Rehak', 'Rufik', 'Taan', 'Thoradhw', 'Thofln', 'Thradal', 'Tordek', 'Taubon', 'Tavok', 'Uhgar', 
        'Urahn', 'Vefi', 'Vonbm', 'Vondd', 'Vtrbin', 
        ]

        self.female_names = [
        'Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 
        'Gunnloda', 'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde', 'Liftrasa', 'Mardred', 
        'Riswynn', 'Sannl', 'Torbera', 'Torgga', 'Vistra', 'Bolhild', 'Dagnal', 'Dafifi', 'Delre', 
        'Diesa', 'Hdeth', 'Eridred', 'Falkrunn', 'Fallthra', 'Finelien', 'Gillydd', 'Gunnloda', 
        'Gurdis', 'Helgret', 'Helja', 'HHn', 'llde', 'Jarana', 'Kathra', 'Kilia', 'Kristryd', 
        'Liftrasa', 'Marastyr', 'Mardred', 'Morana', 'Nalaed', 'Nora', 'Nurkara', 'Orifi', 'Ovina', 
        'Riswynn', 'Sannl', 'Therlin', 'Thodris', 'Torbera', 'Tordrid', 'Torgga', 'Urshar', 'Valida', 
        'Vistra', 'Vonana', 'Werydd', 'Whurd red', 'Yurgunn',
        ]

        self.surnames = [
        'Balderk', 'Battlehammer', 'Brawnanvil', 'Dankil', 'Fireforge', 'Frostbeard', 'Gorunn', 
        'Holderhek', 'Ironfist', 'Loderr', 'Lutgehr', 'Rumnaheim', 'Strakeln', 'Torunn', 'Ungart',
        'Aranore', 'Balderk', 'Battlehammer', 'Bigtoe', 'Bloodkith', 'Bofdarm', 'Brawnanvil', 'Brazzik', 
        'Broodfist', 'Burrowfound', 'Caebrek', 'Daerdahk', 'Dankil', 'Daraln', 'Deepdelver', 'Durthane', 
        'Eversharp', 'Fahack', 'Fire-forge', 'Foamtankard', 'Frostbeard', 'Glanhig', 'Goblinbane', 
        'Goldfinder', 'Gorunn', 'Graybeard', 'Hammerstone', 'Helcral', 'Holderhek', 'Ironfist', 'Loderr', 
        'Lutgehr', 'Morigak', 'Orcfoe', 'Rakankrak', 'Ruby-Eye', 'Rumnaheim', 'Silveraxe', 'Silverstone', 
        'Steelfist', 'Stoutale', 'Strakeln', 'Strongheart', 'Thrahak', 'Torevir', 'Torunn', 'Trollbleeder', 
        'Trueanvil', 'Trueblood', 'Ungart',
        ]

    def name(self):
        return random.choice(self.male_names + self.female_names) + ' ' + random.choice(self.surnames)
    
    def male_name(self):
        return random.choice(self.male_names) + ' ' + random.choice(self.surnames)
    
    def female_name(self):
        return random.choice(self.female_names) + ' ' + random.choice(self.surnames)

class Member:

    """
    Master class for generic gang member 'Thug'
    """

    id = 0
    member_dict = {}

    def __init__(self, gang='Test'):
        namebase = Namebase()
        self.gender = random.choices(['male', 'female', '?'], [1, 1, 0.1])
        if self.gender == 'male':
            self.name = namebase.male_name()
        elif self.gender == 'female':
            self.name = namebase.female_name()
        else:
            self.name = namebase.male_name()
        self.archetype = 'Test'
        self.upkeep = 0
        self.gang = gang
        self.level = 1
        self.xp_requirement = (self.level)**2
        self.xp = 0
        self.gear = 0
        self.assigned_to = None
        
        self.id = Member.id
        Member.member_dict[self.id] = self
        Member.id += 1

    # Give the gang member 1 xp if they aren't at the cap
    def get_xp(self):
        if self.level < 10:
            self.xp += 1
            if self.xp >= self.xp_requirement:
                self.xp = 0
                self.level += 1
                self.xp_requirement = (self.level)**2
                self.gang.event_log.append(f'{self.name} is now level {self.level}.')
            # print(f'{self.name} is level {self.level}. ({self.xp}/{self.xp_requirement})\n')

    # Makes gang member the boss
    # def make_boss(self):
    #     self.archetype = 'Boss'
    #     # self.loyalty = 100

class Thug(Member):
    # Basic Gang Member
    def __init__(self, gang):
        super().__init__(gang)
        self.archetype = 'Thug'
        self.upkeep = 1

    def activate(self):
        if self.assigned_to is None:
            # If the thug doesn't have a job, will mug people for some cash and might gain xp
            output = random.randint(0, self.level)
            if random.randint(1, 10) >= 8:
                self.get_xp()
            self.gang.event_log.append(f'{self.name} mugs people earning {output}.')
            return 'cash', output
        else:
            return self.assigned_to.activate(self)

# class Thief(Member):
#     # Thief
#     def __init__(self, gang):
#         super().__init__(gang)
#         self.archetype = 'Thief'
#         self.upkeep = 1

class Boss(Member):
    # Leads gang
    def __init__(self, gang):
        super().__init__(gang)
        self.archetype = 'Boss'
        self.upkeep = 10

    def activate(self):
        # The Boss doesn't work Rackets, he makes them.
        # Or recruits new members
        available_cash = self.gang.count_cash()
        actions = ['recruit', 'add racket']
        recruit_worth = 2.71828 ** ((sum(self.gang.assets[n].slots for n in self.gang.assets) + sum(self.gang.rackets[n].slots for n in self.gang.rackets) - len(self.gang.members))/10)
        if available_cash > 100:
            racket_worth = available_cash / 100
        else:
            racket_worth = 0
        action = random.choices(actions, [recruit_worth, racket_worth])[0]
        if action == 'recruit':
            output = min(random.randint(0, self.level) + self.level, available_cash)
            self.gang.event_log.append(f'{self.name} tries to recruit {output} people.')
        elif action == 'add racket':
            output = 1
            self.gang.event_log.append(f'{self.name} sets up a new racket.')
        else: 
            output = None
        return action, output
        



# %%
