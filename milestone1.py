import numpy as np
import matplotlib.pyplot as plt

class FileIO:
    filePath = 'PROJECTS\Term Project\CalgaryWeather.csv'
    dataTable = np.genfromtxt(filePath, delimiter=',', dtype = 'float', skip_header= 1)


class Date:
    month = FileIO.dataTable[:,1]

    year = FileIO.dataTable[:,0]


class TemperatureData:
    Dateobj = Date.month
    Dateobj2 = Date.year
    minTemperature = FileIO.dataTable[:,3]
    maxTemparature = FileIO.dataTable[:,2]
    snowFall = FileIO.dataTable[:,4]

class WeatherAnalyzer:
    def getMinTemp(W):
        smallest = np.amin(W)
        return smallest

    def getMaxTemp(Y):
        greatest = np.amax(Y)
        return greatest

    def getMinTempAnnually(B):
        B = TemperatureData.minTemperature
        xarray = []
        xc = 0
        yc = 12
        for i in range (xc, yc):
            b1 = B[i]
            xarray.append(b1)
            xc += 12
            yc += 12

        b2 = WeatherAnalyzer.getMinTemp(xarray)
        print(b2)


    def getMaxTempAnnually(D):
        D = TemperatureData.maxTemperature
        xarray = []
        xc = 0
        yc = 12
        i = 0
        for i in range (xc, yc):
            b1 = D[i]
            xarray.append(b1)
            xc += 12
            yc += 12

        b2 = xarray
        print(b2)

    

        




def main():
    d0 = FileIO.dataTable

    d2 = Date.month

    d3 = Date.year
   
    d4 = TemperatureData.minTemperature

    d5 = TemperatureData.maxTemparature

    d6 = TemperatureData.snowFall

    ans = True

    while ans:
        print("""
        1- Get minimum temperature of 1990-2019
        2- get maximum temperature of 1990-2019
        3- get minimum temperature of 1990-2019 Annually
        4- get maximum temperature of 1990-2019 Annually
        5- Get average snowfall between 1990-2019 Annually""")

        ans = input("Please Choose and option: ")

        if ans =="1":
            print("\n 1-Get minimum temperature of 1990-2019.")
            print ("--------------")
            print("the minimum temperature of 1990-2019 is: ", WeatherAnalyzer.getMinTemp(d4))
        elif ans == "2":
            print("\n 1-Get maximumtemperature of 1990-2019.")
            print ("--------------")
            print("the maximum temperature of 1990-2019 is: ", WeatherAnalyzer.getMaxTemp(d5))
        elif ans == "3":
            print("\n 1-Get minimum temperature of 1990-2019 Annually.")
            print ("--------------")
            print("the minimum temperature of 1990-2019 Annually is: ", WeatherAnalyzer.getMinTempAnnually(d4))
        elif ans =="4":
            print("\n 1-Get maximum temperature of 1990-2019 Annually.")
            print ("--------------")
            print("the maximum temperature of 1990-2019 Annually is: ", WeatherAnalyzer.getMaxTempAnnually(d5))
        else:
            print("Invalid choice. Try again.")
            




    print(WeatherAnalyzer.getMaxTempAnnually(d5))



if __name__ == "__main__":
    main ()