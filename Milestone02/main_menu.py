import WeatherAnalyzer
import numpy as np
import chart

def main():
    chart1 = chart.chart()
    weatherAnal = WeatherAnalyzer.WeatherAnalyzer()
    prompt = True
    while prompt:
        print('1- Get Minimum Temperature of 1990-2019')
        print('2- Get Maximum Temperature of 1990-2019')
        print('3- Get Minimum Temperature of 1990-2019 Annually')
        print('4- Get Maximum Temperature of 1990-2019 Annually')
        print('5- Get Average Snowfall between 1990-2019 Annually')
        print('6- Get Average Temperature between 1990-2019 Annually')
        print('7- LineChart Minimum Temperature of 1990-2019 Annually')
        print('8- LineChart Maximum Temperature of 1990-2019 Annually')
        print('9- Barchart Average Snowfall between 1990-2019 Annually')
        print('10- Barchart Average Temperature between 1990-2019 Annually')
        Option = int(input('11- Select Option: '))
        print("-----------------------")
        if Option == 1:
            print(weatherAnal.getMinTemp())
        elif Option == 2:
            print(weatherAnal.getMaxTemp())
        elif Option == 3:
            matrix = weatherAnal.getMinTempAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
        elif Option == 4:
            matrix = weatherAnal.getMaxTempAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
        elif Option == 5:
            matrix = weatherAnal.getAvgSnowfallAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
        elif Option == 6:
            matrix = weatherAnal.getAvgTempAnnually()
            for row in matrix:
                for col in row:
                    print(col, end=' ')
                print()
        elif Option == 7:
            data = np.array(weatherAnal.getMinTempAnnually())
            chart1.drawLineChart(data[:, 0], data[:, 1],
                'Minimum Temperatures of 1990-2019 annually', 'Year', 'Min Temp (F)')
        elif Option == 8:
            data = np.array(weatherAnal.getMaxTempAnnually())
            chart1.drawLineChart(data[:, 0], data[:, 1],
                'Maximum Temperatures of 1990-2019 annually', 'Year', 'Max Temp (F)')
        elif Option == 9:
            data = np.array(weatherAnal.getAvgSnowfallAnnually())
            chart1.drawBarChart(data[:, 0], data[:, 1],
                'Average Snowfall between 1990-2019 annually', 'Year', 'Snowfall (cm)')
        elif Option == 10:
            data = np.array(weatherAnal.getAvgTempAnnually())
            chart1.drawBarChart(data[:, 0], data[:, 1],
                'Average Temperature between 1990-2019 annually', 'Year', 'Average Temperature (F)')
        elif Option == 11:
                prompt = False
        else:
            print('Invalid Option, try again')

        print("\n-----------------------------------")
            


if __name__ == '__main__':
    main()