import csv
import numpy as np
import matplotlib.pyplot as plt
import re

#finds the average of input l
def Avg(l):
    if len(l) < 1:
        return 0
    else:
        avg = sum(l) / len(l) 
        return avg 

#there are 53 different shot types    
n = 53 
#creates a list for the different shot types and one for the total average
shotType = []
totalAverageValue = []

#opens CSV file
with open('2015-2020 NBA Shot Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
            #skips first line
        if line_count == 0: 
            pass
            line_count += 1
        else:
            #row 13 has the shot types
            shot = str(row[13]).replace(' ','')
            #checks to see if there is a new shot type, adds if a new type
            if shot not in shotType:
                shotType.append(shot)
        #creates different dictionaries of lists for the different values needed
        shotsMade = {i:[] for i in shotType}
        shotsWorth = {i:[] for i in shotType}
        shotsDistance = {i:[] for i in shotType}
        allShotsSorted = {i:[] for i in shotType}
        
#goes back through the csv with the bins set up     
with open('2015-2020 NBA Shot Data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')       
    line_count = 0
    for row in csv_reader: 
        #skips the first line
        if line_count == 0: 
            pass
            line_count += 1
        else:
            #row 26 has binary data on if the shot is made (0 or 1)
            made = int(row[26]) 
            worth = 0
            #row 18 has the data on shot distance
            distance = int(row[18])
            shot = str(row[13]).replace(' ','')
            #if the shot was made
            if made > 0: 
                #row 27 has the value of the shot (2 or 3)
                worth = made * int(row[27])
            #adds values to the list for the total value
            totalAverageValue.append(worth)
            #adds whether the shot was made and how much it is worth/how far it was for each type
            shotsMade[shot].append(made)
            shotsWorth[shot].append(worth)
            shotsDistance[shot].append(distance)
            #starts again wth the next line in CSV
            line_count += 1 
#creates a list to be used for graphing the average value of a shot
averageValue = [] 
currAverageValue = Avg(totalAverageValue)  
#adds the average value for n times into the list 
for i in range(n):    
    averageValue.append(currAverageValue)
#creats a new list of all the data
for shot in shotType:
    allShotsSorted[shot].append(Avg(shotsMade[shot]))
    allShotsSorted[shot].append(Avg(shotsWorth[shot]))
    allShotsSorted[shot].append(Avg(shotsDistance[shot]))   
#sorts the data by distance for easier comprehension
allShotsSorted = sorted(allShotsSorted.items(), key=lambda e:e[1][2])  
#creates new lists of sorted data to be used for graphing
shotTypeName = []
shotMadeSort = []
shotWorthSort = []  
shotDistanceSort = []
#prints the data and adds data for creating a chart  
for i in range(n):
    print("Shot percentage of a " +str(allShotsSorted[i][0])+": "+str(allShotsSorted[i][1][0])+"%")
    print("Value of a shot from "+str(allShotsSorted[i][0])+": "+str(allShotsSorted[i][1][1])+" points")
    print("Average distance of a "+str(allShotsSorted[i][0])+": "+str(allShotsSorted[i][1][2])+" feet\n")
    shotDistanceSort.append(allShotsSorted[i][1][2])
    shotTypeName.append(str(re.sub(r"(\w)([A-Z])", r"\1 \2", str(allShotsSorted[i][0]))))    
    shotMadeSort.append(allShotsSorted[i][1][0]) 
    shotWorthSort.append(allShotsSorted[i][1][1]) 
#creates a list for relative shotdistance for each shot
for i in range(n):
    shotDistanceSort[i] = (shotDistanceSort[i]/shotDistanceSort[n-1])
#resizes the figure 
plt.figure(num=None, figsize=(15, 10), dpi=80, facecolor='w', edgecolor='k')
#plots the different bars and lines
plt.bar(shotTypeName, shotWorthSort, color='red', label = 'Value')
plt.plot(shotMadeSort, color='blue', label = 'Shot %')
plt.plot(shotDistanceSort, color='green', label = 'Relative Distance')
plt.plot(shotTypeName, averageValue, '--', color='#666666', label='Average')
#creates gridlines
plt.grid(color='#95a5a6', linestyle='-', linewidth=.5, axis='y', alpha=0.7)
#rotates the x-axis labels
plt.xticks(rotation=90)
# naming the x axis
plt.xlabel('Shot Type') 
# naming the y axis 
plt.ylabel('Points per Shot')
# giving a title to my graph 
plt.title('Points per Shot vs. Shot Type', fontweight = 'bold')
# function to show the plot
plt.legend()
plt.show()