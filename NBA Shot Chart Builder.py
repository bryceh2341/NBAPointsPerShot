import csv
from matplotlib.patches import Circle, Rectangle, Arc
import matplotlib.pyplot as plt
import itertools 
import seaborn as sns

#finds the average of input l
def Avg(l):
    if len(l) < 1:
        return 0
    else:
        avg = sum(l) / len(l) 
        return avg 
def draw_court(ax=None, color='black', lw=2, outer_lines=False):
    # If an axes object isn't provided to plot onto, just get current one
    if ax is None:
        ax = plt.gca()
    # Create the basketball hoop
    hoop = Circle((0, 0), radius=7.5, linewidth=lw, color=color, fill=False)
    # Create backboard
    backboard = Rectangle((-30, -7.5), 60, -1, linewidth=lw, color=color)
    # The paint
    outer_box = Rectangle((-80, -47.5), 160, 190, linewidth=lw, color=color,
                          fill=False)
    # Create the inner box of the paint, widt=12ft, height=19ft
    inner_box = Rectangle((-60, -47.5), 120, 190, linewidth=lw, color=color,
                          fill=False)
    # Create free throw top arc
    top_free_throw = Arc((0, 142.5), 120, 120, theta1=0, theta2=180,
                         linewidth=lw, color=color, fill=False)
    # Create free throw bottom arc
    bottom_free_throw = Arc((0, 142.5), 120, 120, theta1=180, theta2=0,
                            linewidth=lw, color=color, linestyle='dashed')
    # Restricted Zone, it is an arc with 4ft radius from center of the hoop
    restricted = Arc((0, 0), 80, 80, theta1=0, theta2=180, linewidth=lw,
                     color=color)
    # Three point line
    corner_three_a = Rectangle((-220, -47.5), 0, 140, linewidth=lw,
                               color=color)
    corner_three_b = Rectangle((220, -47.5), 0, 140, linewidth=lw, color=color)
    # 3pt arc - center of arc will be the hoop, arc is 23'9" away from hoop
    three_arc = Arc((0, 0), 475, 475, theta1=22, theta2=158, linewidth=lw,
                    color=color)
    # Center Court
    center_outer_arc = Arc((0, 422.5), 120, 120, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    center_inner_arc = Arc((0, 422.5), 40, 40, theta1=180, theta2=0,
                           linewidth=lw, color=color)
    # List of the court elements to be plotted onto the axes
    court_elements = [hoop, backboard, outer_box, inner_box, top_free_throw,
                      bottom_free_throw, restricted, corner_three_a,
                      corner_three_b, three_arc, center_outer_arc,
                      center_inner_arc]
    if outer_lines:
        # Draw the half court line, baseline and side out bound lines
        outer_lines = Rectangle((-250, -47.5), 500, 470, linewidth=lw,
                                color=color, fill=False)
        court_elements.append(outer_lines)
    # Add the court elements onto the axes
    for element in court_elements:
        ax.add_patch(element)
    #return the court
    return ax
toContinue=True
while toContinue == True:
    #amount of players in the database
    n = 43
    #creates lists for the different values needed
    allPlayerNames = []
    totalAverageValue = []
    avgLocValue = [[] for i in range(n)]
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
                #row 18 has distance data
                distance = int(row[18])
                #row6 has player name
                currPlayerName = str(row[6])
                #row 26 has made or miss, row 27 has shot value
                worth = int(row[26]) * int(row[27])
                #adds values of a shot from a certain distance to average later
                if distance < n:
                    avgLocValue[distance].append(worth)
                    totalAverageValue.append(worth)
                #checks to see if there is a new player, adds if a new player
                if currPlayerName not in allPlayerNames:
                    allPlayerNames.append(currPlayerName)
                
    #gets valid user inputs for player name and shot chart type  
    while True:                
        playerName = input("Enter player name: ")
        shotChartType = int(input("Enter desired shot chart type (1 = dot, 2 = hexagonal, 3 = gradient): "))       
        
        if (playerName in allPlayerNames) and (shotChartType == 1 or 2 or 3):
            break    
        elif (playerName not in allPlayerNames) and (shotChartType == 1 or 2 or 3):
            print("Invalid Name")
        elif (playerName in allPlayerNames) and (shotChartType != 1 or 2 or 3):
            print("Invalid Type")
        else:
            print("Invalid Name and Type")
     
    avgLocValue = [Avg(i) for i in avgLocValue]
    #creates dictionaries for all of the needed values
    playerShotDistance = []
    playerShotWorth = []
    playerShotMade = []
    playerShotXValueMade = []
    playerShotYValueMade = []
    playerShotXValueMiss = []
    playerShotYValueMiss = []
    playerLoceFG = []
    allPlayerShotsX = []
    allPlayerShotsY = []
    #opens csv to go back through
      
    with open('2015-2020 NBA Shot Data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')       
    
        for row in csv_reader: 
            #skips the first line
            if (str(row[6]) == playerName):
                made = int(row[26]) 
                worth = 0
                #row 18 has the data on shot distance
                distance = int(row[18])
                if distance < n: 
                    #adds value for the average eFG at each location
                    shotLoceFG = avgLocValue[distance]/2
                    if made > 0: 
                        #row 27 has the value of the shot (2 or 3)
                        worth = made * int(row[27])
                        #add the shot location data to the made lists
                        playerShotXValueMade.append(float(row[19]))
                        playerShotYValueMade.append(float(row[20]))
                    else:
                        #add the shot location data to the missed lists
                         playerShotXValueMiss.append(float(row[19]))
                         playerShotYValueMiss.append(float(row[20]))
                    #add the values which were just found to the correct lists    
                    playerShotDistance.append(distance)
                    playerShotWorth.append(worth)
                    playerShotMade.append(made)
                    playerLoceFG.append(shotLoceFG)
                                   
    #gets the correct x and y values for plotting
    playerShotXValueMade = [i * 10 for i in playerShotXValueMade]
    playerShotYValueMade = [(i * 10)-50 for i in playerShotYValueMade]
    playerShotXValueMiss = [i * 10 for i in playerShotXValueMiss]
    playerShotYValueMiss = [(i * 10)-50 for i in playerShotYValueMiss]
    allPlayerShotsX = list(itertools.chain(playerShotXValueMade, playerShotXValueMiss))  
    allPlayerShotsY = list(itertools.chain(playerShotYValueMade, playerShotYValueMiss))
    #gets eFG from shot worth
    eFG = [i/2 for i in playerShotWorth] 
    
    #dot plot shot chart
    if shotChartType == 1:
        #size the figure
        plt.figure(figsize=(12,11))
        #plot the makes and misses
        plt.scatter(playerShotXValueMiss, playerShotYValueMiss, color='red', alpha = .5)
        plt.scatter(playerShotXValueMade, playerShotYValueMade, color='green', alpha = .5)
        #title and x axis label with data
        plt.title(playerName, fontsize=18, fontweight = 'bold')
        plt.xlabel('PPS: '+str(round(Avg(playerShotWorth), 3))+' | eFG%: '+
                   str(round(Avg(eFG),3))+' | Location eFG%: '+str(round(Avg(playerLoceFG),3))
                   , fontsize=18)
        #draw court to correct size
        draw_court(outer_lines=True)
        plt.xlim(-250,250)
        plt.ylim(422.5, -47.5)
        #show chart
        plt.show()
        
    if shotChartType == 2:
        plt.figure(figsize=(12,11))
    
        plt.hexbin(allPlayerShotsX, allPlayerShotsY, bins='log', cmap='afmhot', 
                   gridsize=(40), extent=(-300, 300, -100, 500))
        
        
        plt.title(playerName, fontsize=18, fontweight = 'bold')
        plt.xlabel('PPS: '+str(round(Avg(playerShotWorth), 3))+' | eFG%: '+
                   str(round(Avg(eFG),3))+' | Location eFG%: '+str(round(Avg(playerLoceFG),3))
                   , fontsize=18)
        #draw court to correct size
        draw_court(outer_lines=True, color='white')
        plt.xlim(-250,250)
        plt.ylim(422.5, -47.5)
        
        plt.show()
        
    if shotChartType == 3:  
           
        cmap = plt.cm.gist_heat_r
    
        # n_levels sets the number of contour lines for the main kde plot
        joint_shot_chart = sns.jointplot(x=allPlayerShotsX, y=allPlayerShotsY,
                                         kind='kde', space=0, shade=True, cmap=cmap, 
                                         color='orange', fill=True, n_levels=50)
        
        joint_shot_chart.fig.set_size_inches(12,11)
        
        # A joint plot has 3 Axes, the first one called ax_joint 
        # is the one we want to draw our court onto and adjust some other settings
        ax = joint_shot_chart.ax_joint
        draw_court(ax)
        ax.set_title(playerName, y=1.2, fontsize=18, fontweight='bold')
        # Adjust the axis limits and orientation of the plot in order
        # to plot half court, with the hoop by the top of the plot
        ax.set_xlim(-250,250)
        ax.set_ylim(422.5, -47.5)
        
        # Get rid of axis labels and tick marks
        ax.set_xlabel('PPS: '+str(round(Avg(playerShotWorth), 3))+' | eFG%: '+
                   str(round(Avg(eFG),3))+' | Location eFG%: '+str(round(Avg(playerLoceFG),3))
                   , fontsize=18)
        
        ax.set_ylabel('')
        ax.tick_params(labelbottom='off', labelleft='off') 
        
        plt.show()
        
    userContinue = input("Continue? (Y/N): ")
    if userContinue == 'N':
        toContinue = False
    else:
        toContinue=True