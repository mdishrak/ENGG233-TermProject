import date
class TemperatureData:
    def __init__(self, x, Table):
        self.date = date.date(x, Table)
        self.minTemp = Table[x, 3]
        self.maxTemp = Table[x, 2]
        self.snowfall = Table[x, 4]