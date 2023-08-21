class date:
    def __init__(self, x, Table):
        self.month = Table[x, 1]
        self.year = int(Table[x, 0])