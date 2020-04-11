import random


class Namebase:
    def __init__(self, male_names, female_names, surnames):
        self.male_names = male_names
        self.female_names = female_names
        self.surnames = surnames

    def name(self):
        return random.choice(self.male_names + self.female_names) + ' ' + random.choice(self.surnames)


male_names = [
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

female_names = [
    'Amber', 'Artin', 'Audhild', 'Bardryn', 'Dagnal', 'Diesa', 'Eldeth', 'Falkrunn', 'Finellen', 
    'Gunnloda', 'Gurdis', 'Helja', 'Hlin', 'Kathra', 'Kristryd', 'Ilde', 'Liftrasa', 'Mardred', 
    'Riswynn', 'Sannl', 'Torbera', 'Torgga', 'Vistra', 'Bolhild', 'Dagnal', 'Dafifi', 'Delre', 
    'Diesa', 'Hdeth', 'Eridred', 'Falkrunn', 'Fallthra', 'Finelien', 'Gillydd', 'Gunnloda', 
    'Gurdis', 'Helgret', 'Helja', 'HHn', 'llde', 'Jarana', 'Kathra', 'Kilia', 'Kristryd', 
    'Liftrasa', 'Marastyr', 'Mardred', 'Morana', 'Nalaed', 'Nora', 'Nurkara', 'Orifi', 'Ovina', 
    'Riswynn', 'Sannl', 'Therlin', 'Thodris', 'Torbera', 'Tordrid', 'Torgga', 'Urshar', 'Valida', 
    'Vistra', 'Vonana', 'Werydd', 'Whurd red', 'Yurgunn',
]

surnames = [
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


dwarf = Namebase(male_names, female_names, surnames)