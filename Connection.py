from Station import Station

class Connection(object):
    """The Connection class represents a connection between two subway
       stations along a particular subway line. Note: this class
       is an information holder. It does nothing but store data."""

    def __init__(self, station1, station2, line):
        """Every Connection object has two stations and the name of its line."""
        self.station1 = station1
        self.station2 = station2
        self.line     = line

    def __eq__(self, obj):
        """Equality of Connection objects depends on the equality
           of their attributes: station1, station2, line."""
        if not isinstance(obj, Connection):
            return False
        result1 = self.station1 == obj.get_station1()
        result2 = self.station2 == obj.get_station2()
        result3 = self.line == obj.get_line()
        return result1 and result2 and result3

    def __str__(self):
        return '(%s,%s,%s)' % (self.station1,self.station2,self.line)

    __repr__ = __str__

    def get_station1(self):
        """Retrieves a Connection object's first station."""
        return self.station1

    def get_station2(self):
        """Retrieves a Connection object's second station."""
        return self.station2

    def get_line(self):
        """Retrieves the name of a Connection object's subway line."""
        return self.line
