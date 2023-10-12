from Connection import Connection
from Station    import Station

class Subway(object):
    """The Subway class represents a subway line with stations and
       connections between those stations."""

    def __init__(self):
        """Every Subway object has a collection of stations and a list
           of connections."""
        self.stations = []
        self.connections = []
        self.network = {}

    def add_station(self, name):
        """If we have never seen the specified station name before, then
           we add it to our collection of station objects."""
        if not self.has_station(name):
            self.stations.append(Station(name))
            return True
        return False

    def has_station(self, name):
        """Returns True if we have a station with the specified name."""
        station = Station(name)
        return station in self.stations

    def has_connection(self, name1, name2, line):
        """Returns True if we have a connection with the specified atts."""
        connection = Connection(Station(name1), Station(name2), line)
        return connection in self.connections

    def add_connection(self, name1, name2, line):
        """Adds a connection going in both directions to the subway
           as long as specified names reference existing stations."""
        if self.has_station(name1) and self.has_station(name2):
            connection1 = Connection(Station(name1), Station(name2), line)
            connection2 = Connection(Station(name2), Station(name1), line)
            self.connections.append(connection1)
            self.connections.append(connection2)
            self.add_to_network(Station(name1), Station(name2))
            self.add_to_network(Station(name2), Station(name1))
            return True
        return False

    def add_to_network(self, station1, station2):
        if self.network.__contains__(station1):
            stations = self.network[station1]
            if not station2 in stations:
                stations.append(station2)
        else:
            self.network[station1] = [station2]

    def get_directions(self, name1, name2):
        if not self.has_station(name1) or not self.has_station(name2):
            return False
        station1  = Station(name1)
        station2  = Station(name2)
        route     = []
        reachable = []
        previous  = {}

        # check to see if stations are one station apart
        neighbors = self.network[station1]
        for station in neighbors:
            if station == station2:
                route.append(self.get_connection(station1, station2))
                return route
            else:
                reachable.append(station)
                previous[station] = station1

        # start searching the graph looking for shortest path to destination
        next_stations = []
        next_stations.extend(neighbors)
        current_station = station1

        # need to use found_it flag as I've done below
        # because python does not support labelled loops
        found_it = False

        for i in range(1, len(self.stations)):
            if found_it:
                break
            tmp_next_stations = []
            for station in next_stations:
                if found_it:
                    break
                reachable.append(station)
                current_station   = station
                current_neighbors = self.network[current_station]
                for neighbor in current_neighbors:
                    if found_it:
                        break
                    if neighbor == station2:
                        reachable.append(neighbor)
                        previous[neighbor] = current_station
                        found_it = True
                    elif not neighbor in reachable:
                        reachable.append(neighbor)
                        tmp_next_stations.append(neighbor)
                        previous[neighbor] = current_station
            next_stations     = tmp_next_stations

        # path has been found
        keepLooping = True
        key_station = station2
        station     = None

        while keepLooping:
            station = previous[key_station]
            route.insert(0, self.get_connection(station, key_station))
            if station1 == station:
                keepLooping = False
            key_station = station

        return route

    def get_connection(self, station1, station2):
        for connection in self.connections:
            if station1 == connection.get_station1() and \
               station2 == connection.get_station2():
                return connection
        return None
