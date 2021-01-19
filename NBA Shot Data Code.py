import csv
import matplotlib.pyplot as plt 
import numpy as np

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

#94 is the maximum number because length of the floor
    n = 95
#Creates two lists for the shots and how much they are worth (make or miss)
    shots = [[] for i in range(n)]
    value = [[] for i in range(n)]
    totalAverageValue = []
#pasres through CSV file
    for row in csv_reader:
        #skips first line
        if line_count == 0: 
            pass
            line_count += 1
        else:
            made = 0 
            worth = 0
            #row 18 has the shot distance data
            i = int(row[18])
            #row 22 has the shot outcome(made or missed)
            if str(row[22]) == "made": 
                #assigns the value of made to 1 is the shot was made
                made = 1
                #row 27 has the value of the shot (2 or 3)
                worth = made * int(row[27])
            #adds values to the lists at the corresponding shot distance
            shots[i].append(made)
            value[i].append(worth)
            totalAverageValue.append(worth)
            #starts again wth the next line in CSV
            line_count += 1 
    
    #prints the values found above        
    for i in range(n):
        #for each value, finds the average for shooting % and value
        shotAverage = Avg(shots[i])
        shotValue = Avg(value[i])
        
        print("Shot percentage from " +str(i)+" feet: "+str(shotAverage)+"%")
        print("Value of a shot from "+str(i)+" feet: "+str(shotValue)+" points")
        print()
    #finds the average value of all the shots 
    totalAverage = Avg(totalAverageValue)    
    print("The value of an average NBA shot is: "+str(totalAverage)+" points")
    #relevant shot locations
    m = 35
    # x and y axis values 
    a = []
    b = []
    c = []
    for i in range(m):
        a.append(i)
        b.append(Avg(value[i]))
        c.append(totalAverage)
    x = np.array(a) 
    y = np.array(b) 
    #next x and y values
    nextY = np.array(c)
    # plotting the points
    plt.plot(x, y, label='Shot value by distance') 
    plt.plot(x, nextY, '--', label='Average Shot Value')
    # naming the x axis
    plt.xlabel('Shot Distance (feet)') 
    # naming the y axis 
    plt.ylabel('Points per Shot')
    # giving a title to my graph 
    plt.title('Points per Shot vs. Shot Distance')
    # function to show the plot
    plt.legend()
    plt.show()
        
        
            
    
