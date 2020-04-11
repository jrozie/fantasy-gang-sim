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

class Member:

    """
    Master class for generic gang member 'Thug'
    """

    id = 0
    member_dict = {}

    def __init__(self, gang):
        dwarf = Namebase()
        self.name = dwarf.name()
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

