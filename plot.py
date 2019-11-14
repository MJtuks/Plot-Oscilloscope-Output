import matplotlib.pyplot as plt
import pandas as pd
import sys

inputFile1 = str(sys.argv[1])
inputFile2 = str(sys.argv[2])
outputFile = str(sys.argv[3])

pandaDataFrame = pd.read_csv(inputFile1)
seconds = list(pandaDataFrame['x-axis'])
voltages = list(pandaDataFrame['LIN'])

seconds.remove(seconds[0])
voltages.remove(voltages[0])

seconds = list(map(float, seconds))
voltages = list(map(float, voltages))

plt.plot(seconds, voltages, color='y')

df = pd.read_csv(inputFile2)
seconds = list(df['x-axis'])
voltages = list(df['2'])

seconds.remove(seconds[0])
voltages.remove(voltages[0])

seconds = list(map(float, seconds))
voltages = list(map(float, voltages))

plt.plot(seconds, voltages, color='r')
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Transmitted and Received Ultrasonic Signal")
plt.savefig(outputFile, format='pdf')