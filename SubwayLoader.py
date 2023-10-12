from Subway        import Subway
from SubwayPrinter import SubwayPrinter

class SubwayLoader(object):

    def __init__(self):
        self.subway = Subway()

    def get_subway(self):
        return self.subway

    def loadFromFile(self, name):
        data = open(name, "U")
        self.loadStations(data)
        line = data.readline().strip()
        while line != "":
            self.loadLine(data, line)
            line = data.readline().strip()
        data.close()

    def loadStations(self, data):
        station = data.readline().strip()
        while station != "":
            self.subway.add_station(station)
            station = data.readline().strip()

    def loadLine(self, data, line):
        station1 = data.readline().strip()
        station2 = data.readline().strip()
        while station2 != "":
            self.subway.add_connection(station1,station2,line)
            station1 = station2
            station2 = data.readline().strip()

if __name__ == '__main__':
    """Takes the place of the book's LoadTester class."""
    loader = SubwayLoader()
    loader.loadFromFile("ObjectvilleSubway.txt")
    subway = loader.get_subway()
    print("Testing stations...")
    if subway.has_station("DRY Drive") and \
       subway.has_station("Servlet Springs") and \
       subway.has_station("Boards 'R' Us"):
        print("PASSED!")
    else:
        print("FAILED!")
    print("Testing connections...")
    if subway.has_connection("DRY Drive","PMP Place","Wirfs-Brock Line")   and \
       subway.has_connection("GoF Gardens","JSP Junction","Jacobson Line") and \
       subway.has_connection("LSP Lane","Head First Labs","Booch Line"):
        print("PASSED!")
    else:
        print("FAILED!")
    print
    p = SubwayPrinter()
    print("-" * 70)
    p.print_directions(subway.get_directions("AJAX Rapids", "JavaRanch"))
    print("-" * 70)
    p.print_directions(subway.get_directions("XHTML Expressway","JSP Junction"))
    print("-" * 70)
    p.print_directions(subway.get_directions("Mighty Gumball, Inc.", "Choc-O-Holic, Inc."))
    print("-" * 70)
