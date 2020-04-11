class Racket:
    """
    Class for rackets, a place or operation that provides a benefit to the gang
    """
    id = 0
    racket_dict = {}

    def __init__(self, gang):
        self.name = 'Racket'
        self.gang = gang
        self.income = 10
        self.cash = 50
        self.inventory = {}
        
        self.id = Racket.id
        Racket.racket_dict[self.id] = self
        Racket.id += 1