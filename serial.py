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

    def __init__(self, start):
        "Create unique incrementing serial numbers from 'start' number."
        self.start = start
        self.start_fix = start

    def __repr__(self):
        "String representation to provide a nicer appearance in debugging messages or in the console"
        return f"<SerialGenerator start={self.start_fix} next={self.start}>"

    def generate(self):
        "Get new unique incrementing serial number."
        current_serial_number = self.start
        self.start += 1
        return current_serial_number

    def reset(self):
        "Reset the serial number to the 'start' number."
        self.start = self.start_fix