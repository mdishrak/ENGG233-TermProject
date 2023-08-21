import numpy as np

class FileIO:
    def __init__(self):
        self.filePath = 'PROJECTS\Term Project\Milestone02_Ishrak\Milestone02\CalgaryWeather.csv'
        self.Table = self.read_weather()
        self.y = self.Table[:, 3]
        self.x = self.Table[:, 1]
    def read_weather(self):
        data = np.loadtxt(self.filePath, delimiter=',', skiprows=1, usecols=(0, 1, 2, 3, 4), dtype=np.float)
        return data