class SubwayPrinter(object):

    def __init__(self):
        pass

    def print_directions(self, route):
        connection    = route[0]
        station1      = connection.get_station1()
        station2      = connection.get_station2()
        current_line  = connection.get_line()
        previous_line = current_line

        print "Start out at %s." % (station1.get_name())
        print
        print "Get on the %s heading towards %s." % \
              (current_line, station2.get_name())
        print

        for index in range(1, len(route)):
            connection   = route[index]
            current_line = connection.get_line()
            station1     = connection.get_station1()
            station2     = connection.get_station2()
            if current_line == previous_line:
                print "Continue past %s..." % (station1.get_name())
                print
            else:
                print "When you get to %s, get off the %s." % \
                      (station1.get_name(), previous_line)
                print
                print "Switch over to the %s, heading towards %s." % \
                      (current_line, station2.get_name())
                print
                previous_line = current_line

        print "Get off at %s and enjoy yourself!" % (station2.get_name())
        print
