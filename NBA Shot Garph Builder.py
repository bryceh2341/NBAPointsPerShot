import csv
import matplotlib.pyplot as plt

#finds the average of input l
def Avg(l):
    if len(l) < 1:
        return 0
    else:
        avg = sum(l) / len(l) 
        return avg 
#creates a loop to create as many shot charts as the user wants
toContinue=True
while toContinue == True:
    #amount of relevant shot locations
    n = 35
    #amount of shot types
    m = 7
    #creates lists for the different values needed
    allPlayerNames = []
    avgLocValue = [[] for i in range(n)]
    avgLocZoneWorth = [[] for i in range(m)]
    #list of the different shot types
    shotType = ["Restricted Area", "In The Paint (Non-RA)", "Mid-Range", 
         "Left Corner 3", "Right Corner 3", "Above the Break 3",
         "Backcourt"]
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
                #row 18 has distance data
                distance = int(row[18])
                #row 15 has shot type data
                typeOfShot = shotType.index(str(row[15]))
                #row6 has player name
                currPlayerName = str(row[6])
                #row 26 has made or miss, row 27 has shot value
                worth = int(row[26]) * int(row[27])
                #adds values of a shot from a certain distance to average later
                if distance < n:
                    avgLocValue[distance].append(worth)
                    avgLocZoneWorth[typeOfShot].append(worth)
                #checks to see if there is a new player, adds if a new player
                if currPlayerName not in allPlayerNames:
                    allPlayerNames.append(currPlayerName)
                
    #gets valid user inputs for player name and shot chart type  
    while True:                
        playerName = input("Enter player name: ")
        shotGraphType = int(input("Enter graph type (1 = Distance, 2 = Zone): "))
        
        if (playerName in allPlayerNames):
            break    
        elif (playerName not in allPlayerNames):
            print("Invalid Name")

    #calculates average location value
    avgLocValue = [Avg(i) for i in avgLocValue]
    #calculates average location value for each zone
    avgLocZoneWorth = [Avg(i) for i in avgLocZoneWorth]
    #creates dictionaries for all of the needed values
    playerShotWorth = [[] for i in range(n)]   
    playerShotDistance = [[] for i in range(n)]
    playerShotType = [[] for i in range(m)]
    playereFG = []
    playerLoceFG = []
    shotZoneWorth = [[] for i in range(m)]
    totalShots = 0
    #opens csv to go back through
      
    with open('2015-2020 NBA Shot Data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')       
    
        for row in csv_reader: 
            #skips the first line
            if (str(row[6]) == playerName):
                #creates different objects for loater storage and calculation
                made = int(row[26]) 
                worth = 0
                eFG = 0
                typeOfShot = shotType.index(str(row[15]))
                #row 18 has the data on shot distance
                distance = int(row[18])
                if distance < n: 
                    #adds value for the average eFG at each location
                    shotLoceFG = avgLocValue[distance]/2
                    #adds shot distance
                    playerShotDistance[distance].append(1)
                    #dds to the total shots counter
                    totalShots += 1
                    if made > 0: 
                        #row 27 has the value of the shot (2 or 3)
                        worth = made * int(row[27])
                        eFG = worth/2
                    #add the values which were just found to the correct lists    
                    playerShotWorth[distance].append(worth)
                    playerLoceFG.append(shotLoceFG)
                    playereFG.append(eFG)
                #adds whether the shot was made and how much it is worth for each zone
                shotZoneWorth[typeOfShot].append(worth)
                playerShotType[typeOfShot].append(1)
    #creates lists to be graphed
    x = []
    nextX = []
    playerShotValuePerDistance = []
    playerAverageDistance = []
    avgShotZoneWorth = []
    playerAverageZone = []
    #adds values to lists for values of shots at each distance and average distance
    for i in range(n):
        x.append(i)
        playerShotValuePerDistance.append(Avg(playerShotWorth[i]))
        playerAverageDistance.append((len(playerShotDistance[i]))*3/totalShots)
    #adds values for shots at each zone and how many shots at each zone  
    for i in range(m):
        avgShotZoneWorth.append(Avg(shotZoneWorth[i]))
        nextX.append(i)
        playerAverageZone.append((len(playerShotType[i])/totalShots))
    #prints distance chart
    if shotGraphType == 1:
        plt.plot(x, playerShotValuePerDistance, label='Average Player Shot Value') 
        plt.plot(x, avgLocValue, '--', label='Average NBA Shot Value')
        plt.bar(x, playerAverageDistance, color='#e60000', label='Distribution of Shots per Distance')
        # naming the x axis
        plt.xlabel('Shot Distance (feet)\n'+'PPS: '+str(round(Avg(playereFG)*2, 3))+' | eFG%: '+
                       str(round(Avg(playereFG),3))+' | Location eFG%: '+str(round(Avg(playerLoceFG),3))
                       , fontsize=14) 
        # naming the y axis 
        plt.ylabel('Points per Shot', fontsize=14)
        # giving a title to my graph 
        plt.title(playerName, fontweight='bold', fontsize=16)
        #add gridlines
        plt.grid(color='#95a5a6', linestyle='-', linewidth=.5, axis='y', alpha=0.7)
        # function to show the plot
        plt.legend()
        plt.show()  
    #prints shot type chart 
    if shotGraphType == 2:
        # data to plot
        barWidth = 0.25
        
        plt.plot(avgShotZoneWorth, label='Average Player Shot Value') 
        plt.plot(avgLocZoneWorth, '--', label='Average NBA Shot Value')
        plt.bar(nextX, playerAverageZone, color='#e60000', label='Distribution of Shots per Type')
         
        # Add xticks on the middle of the group bars
        plt.title(playerName, fontweight='bold', fontsize=16)
        shotTypes = ["Restricted\nArea", "In The\nPaint\n(Non-RA)", "Mid-\nRange", 
                         "Left\nCorner 3", "Right\nCorner 3", "Above\nthe\nBreak 3",
                         "Backcourt"]
        plt.xticks([r for r in range(m)], shotTypes)
        
        plt.xlabel('Shot Type\n'+'PPS: '+str(round(Avg(playereFG)*2, 3))+' | eFG%: '+
               str(round(Avg(playereFG),3))+' | Location eFG%: '+str(round(Avg(playerLoceFG),3))
               , fontsize=14) 
        #add gridlines
        plt.grid(color='#95a5a6', linestyle='-', linewidth=.5, axis='y', alpha=0.7)
        
        # Create legend & Show graphic
        plt.legend()
        plt.show()
    #asks the user is they would like to continue 
    userContinue = input("Continue? (Y/N): ")
    if userContinue == 'N':
        toContinue = False
    else:
        toContinue=True