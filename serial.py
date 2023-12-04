"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


    def __init__(self, start=0):
        """Make a new generator and define starting number. Establish count"""
        self.start = start
        self.count = 0
    
    def __repr__(self):
        """Show representation"""
        return f"<SerialGenerator start={self.start} count={self.count}"

    def generate(self):
        """If count is 0, return starting number, else, return next serial. Increase count"""
        if self.count == 0:
            self.count += 1
            return self.start
        self.count += 1
        return self.start + self.count-1
    
    def reset(self):
        """Reset count to 0"""
        self.count = 0
        


