import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import FileIO

class chart:
    def __init__(self):
        self.data = FileIO.FileIO()
        self.dataTable = self.data.Table

    def drawLineChart(self, x, y, title, xlabel, ylabel):
        plt.title(title)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)

        plt.plot(x, y, marker='o')
        plt.show()

    def drawBarChart(self, x, y, title, xlabel, ylabel):
       plt.title(title)
       plt.ylabel(ylabel)
       plt.xlabel(xlabel)
       z = np.arange(1990,2020)
       plt.bar(z,y, align='center', alpha=0.5)
       plt.show()

