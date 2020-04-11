class Racket:
    """
    Class for rackets, a place or operation that provides a benefit to the gang
    Rackets have active effects that provide a resource to the gang
    """
    id = 0
    racket_dict = {}

    def __init__(self, gang):
        self.name = 'Racket'
        self.gang = gang
        self.income = 10
        
        self.id = Racket.id
        Racket.racket_dict[self.id] = self
        Racket.id += 1

    def activate(self):
        gang.earn(income)