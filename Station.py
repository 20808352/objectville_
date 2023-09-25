class Station(object):
    """The Station class represents a single named station on a subway line."""

    def __init__(self, name):
        """Every Station object has a name attribute."""
        self.name = name

    def __eq__(self, obj):
        """Equality of Station objects depends on the lowercase version of
           their names."""
        if not isinstance(obj, Station):
            return False
        return self.name.lower() == obj.get_name().lower()

    def __hash__(self):
        """A Station object's hash code depends on the hash code of
           the lowercase version of its name."""
        return self.name.lower().__hash__()

    def __str__(self):
        return '%s' % (self.name)

    __repr__ = __str__

    def get_name(self):
        """Retrieves the Station object's name."""
        return self.name
