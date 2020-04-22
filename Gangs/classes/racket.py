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
        self.provides = 'cash'
        self.income = 10
        self.assigned = []
        self.slots = 5
        
        self.id = Racket.id
        Racket.racket_dict[self.id] = self
        Racket.id += 1

    def activate(self, activator):
        # Gang members work the racket to earn a resource
        # Update to provide items or materials etc
        if self.provides == 'cash':
            output = self.income
        self.gang.event_log.append(f'{activator.name} works at {self.name} earning {self.income}.')
        return self.provides, output