class SubwayPrinter(object):

    def __init__(self):
        pass

    def print_directions(self, route):
        connection    = route[0]
        station1      = connection.get_station1()
        station2      = connection.get_station2()
        current_line  = connection.get_line()
        previous_line = current_line

        print(f"Start out at {station1.get_name()}")
        print()
        print(f"Get on the %s heading towards {current_line, station2.get_name()}.")
        print()

        for index in range(1, len(route)):
            connection   = route[index]
            current_line = connection.get_line()
            station1     = connection.get_station1()
            station2     = connection.get_station2()
            if current_line == previous_line:
                print(f"Continue past {station1.get_name()}...")
                print
            else:
                print(f"When you get to {station1.get_name()}, get off the {previous_line}.")
                print()
                print(f"Switch over to the {current_line}, heading towards {station2.get_name()}.")
                print()
                previous_line = current_line

        print(f"Get off at {station2.get_name()} and enjoy yourself!")
        print()
