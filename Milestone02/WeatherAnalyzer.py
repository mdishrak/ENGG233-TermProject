import TemperatureData
import FileIO
import numpy as np

class WeatherAnalyzer:
    def __init__(self):
        self.Table = FileIO.FileIO().Table
        self.tempData = []
        for i in range(len(self.Table)):
            self.tempData.append(TemperatureData.TemperatureData(i, self.Table))

    def getMinTemp(self):
        mintemp = self.tempData[0].minTemp
        for i in range(len(self.tempData)):
            temp = self.tempData[i].minTemp
            if (mintemp > temp):
                mintemp = temp
        
        return mintemp

    def getMaxTemp(self):
        maxtemp = self.tempData[0].maxTemp
        for i in range(len(self.tempData)):
            temp = self.tempData[i].maxTemp
            if (maxtemp < temp):
                maxtemp = temp
        
        return maxtemp


    def getMinTempAnnually(self):
        annuallMin = []
        for i in range(0, len(self.tempData), 12):
            localYearMin = []
            localYearMin.append(self.tempData[i].date.year)
            localMin = 50
            for month in range(12):
                try:
                    if self.tempData[i + month].minTemp < localMin:
                        localMin = self.tempData[i + month].minTemp
                except:
                    if self.tempData[i - month].minTemp < localMin:
                        localMin = self.tempData[i -month].minTemp
            localYearMin.append(localMin)
            annuallMin.append(localYearMin)
        return annuallMin


    def getMaxTempAnnually(self):
        annuallMax = []
        for i in range(0, len(self.tempData), 12):
            localYearMax = []
            localYearMax.append(self.tempData[i].date.year)
            localMax = -50
            for month in range(12):
                try:
                    if self.tempData[i+month].maxTemp > localMax:
                        localMax = self.tempData[i+month-1].maxTemp
                except IndexError:
                    
                    if self.tempData[i-month-1].maxTemp > localMax:
                        localMax = self.tempData[i-month].maxTemp
            localYearMax.append(localMax)
            annuallMax.append(localYearMax)
        return annuallMax
        
    def getAvgSnowfallAnnually(self):
        annualAvg = []
        for i in range(0, len(self.tempData), 12):
            yearAvg = []
            yearSum = 0
            try:
                for month in range(12):
                    yearSum += self.tempData[i + month].snowfall
                yearAvg.append(self.tempData[i].date.year)
                yearAvg.append(yearSum/12)
            except IndexError:
                yearSum = 0
                for month in range(11):
                    yearSum += self.tempData[i - month].snowfall
                yearAvg.append(self.tempData[i].date.year)
                yearAvg.append(yearSum/11)
            annualAvg.append(yearAvg)
        return annualAvg

    def getAvgTempAnnually(self):
        annuallMax = []
        for i in range(0, len(self.tempData), 12):
            avg = []
            avg.append(self.tempData[i].date.year)
            localMax = -50
            localMin = 50
            x = []
            
            for month in range(12):
                try:
                    if self.tempData[i+month].maxTemp > localMax:
                        x.append(self.tempData[i+month].maxTemp)
                    if self.tempData[i+month].minTemp < localMin:
                        x.append(self.tempData[i+month].minTemp)
                except IndexError:
                    break
            
            avg.append(np.average(x))
            annuallMax.append(avg)
            
        return annuallMax

        

        

    


