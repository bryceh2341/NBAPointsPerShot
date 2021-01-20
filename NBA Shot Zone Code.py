import csv
import numpy as np
import matplotlib.pyplot as plt

#finds the average of input l
def Avg(l):
    if len(l) < 1:
        return 0
    else:
        avg = sum(l) / len(l) 
        return avg 

#opens CSV file
with open('2015-2020 NBA Shot Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
#amount of shot zones
    n = 7
#Creates a list for percent and worth each shot zone
    shotZonePercent = [[] for i in range(n)]
    AvgShotZonePercent = [[] for i in range(n)]
    shotZoneWorth = [[] for i in range(n)]
    AvgShotZoneWorth = [[] for i in range(n)]
#different possible shot zones
    shotType = ["Restricted Area", "In The Paint (Non-RA)", "Mid-Range", 
                 "Left Corner 3", "Right Corner 3", "Above the Break 3",
                 "Backcourt"]
#creates a list for the total average
    totalAverageValue = []
#pasres through CSV file
    for row in csv_reader:
        #skips first line
        if line_count == 0: 
            pass
            line_count += 1
        else:
            #row 26 gives a made shot 1 and a missed shot 0
            made = int(row[26]) 
            worth = 0
            #if the shot was made
            if made > 0: 
                #row 27 has the value of the shot (2 or 3)
                worth = made * int(row[27])
            #adds values to the lists at the corresponding shot distance
            totalAverageValue.append(worth)
            #row 15 has the shot zone data
            i = shotType.index(str(row[15]))
            #adds whether the shot was made and how much it is worth for each zone
            shotZonePercent[i].append(made)
            shotZoneWorth[i].append(worth)
            #starts again wth the next line in CSV
            line_count += 1 
#creates two lists with the values for worth and percent            
for i in range(n):            
    AvgShotZonePercent[i] = Avg(shotZonePercent[i])
    AvgShotZoneWorth[i] = Avg(shotZoneWorth[i])
#for each value, print the average for shooting % and value
for i in range(n):
    print("Shot percentage from " +str(shotType[i])+": "+str(AvgShotZonePercent[i])+"%")
    print("Value of a shot from "+str(shotType[i])+": "+str(AvgShotZoneWorth[i])+" points\n")
#finds and prints the average value of all the shots 
totalAverage = Avg(totalAverageValue)    
print("The value of an average NBA shot is: "+str(totalAverage)+" points")

# data to plot
barWidth = 0.25
 
# Set position of bar on X axis
r1 = np.arange(n)
r2 = [x + barWidth for x in r1]
#create a list to plot a line for the average of all shots
totalAverageGraph = []
for i in range(n):
    totalAverageGraph.append(totalAverage)

# Make the plot
plt.plot(r1, totalAverageGraph, '--', color='#666666', label='Average')
plt.plot(AvgShotZonePercent, color='#e60000', label='Shot %')
plt.bar(r2, AvgShotZoneWorth, color='#0052cc', width=barWidth, edgecolor='white', label='Value')

 
# Add xticks on the middle of the group bars
plt.xlabel('Shot Zone vs. Shot Value and %', fontweight='bold')
shotTypes = ["Restricted\nArea", "In The\nPaint\n(Non-RA)", "Mid-\nRange", 
                 "Left\nCorner 3", "Right\nCorner 3", "Above\nthe\nBreak 3",
                 "Backcourt"]
plt.xticks([r + barWidth for r in range(n)], shotTypes)
#add gridlines
plt.grid(color='#95a5a6', linestyle='-', linewidth=.5, axis='y', alpha=0.7)

# Create legend & Show graphic
plt.legend()
plt.show()
