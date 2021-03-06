import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import colors 
import statistics

atbthree = []
cornerthree = []
shortmid = []
longmid = []
attherim = []
ft = []

for i in range(355):
    atbthree.append('make')
for i in range(645):
    atbthree.append('miss')
    
for i in range(39):
    cornerthree.append('make')
for i in range(61):
    cornerthree.append('miss')
    
for i in range(401):
    shortmid.append('make')
for i in range(599):
    shortmid.append('miss')
    
for i in range(408):
    longmid.append('make')
for i in range(592):
    longmid.append('miss')
    
for i in range(635):
    attherim.append('make')
for i in range(365):
    attherim.append('miss')

for i in range(773):
    ft.append('make')
for i in range(227):
    ft.append('miss')

standings = []
for i in range(1000):
    gameswon = 0
    for i in range(4):
        homepoints = 0
        roadpoints = 0
        
        homeatb3 = np.random.choice(atbthree, 27)
        homeatb3perc = sum(homeatb3 == 'make')/(sum(homeatb3 == 'make')+sum(homeatb3 == 'miss'))
        homepoints += homeatb3perc*1.5*27
        
        homecorn3 = np.random.choice(cornerthree, 8)
        homecorn3perc = sum(homecorn3 == 'make')/(sum(homecorn3 == 'make')+sum(homecorn3 == 'miss'))
        homepoints += homecorn3perc*1.5*8
        
        homesm = np.random.choice(shortmid, 19)
        homesmperc = sum(homesm == 'make')/(sum(homesm == 'make')+sum(homesm == 'miss'))
        homepoints += homesmperc*19
        
        homelm = np.random.choice(longmid, 11)
        homelmperc = sum(homelm == 'make')/(sum(homelm == 'make')+sum(homelm == 'miss'))
        homepoints += homelmperc*11
        
        homeatr = np.random.choice(attherim, 35)
        homeatrperc = sum(homeatr == 'make')/(sum(homeatr == 'make')+sum(homeatr == 'miss'))
        homepoints += homeatrperc*35
        
        homeft = np.random.choice(ft, 19)
        homeftperc = sum(homeft == 'make')/(sum(homeft == 'make')+sum(homeft == 'miss'))
        homepoints += homeftperc*19
        
        roadatb3 = np.random.choice(atbthree, 27)
        roadatb3perc = sum(roadatb3 == 'make')/(sum(roadatb3 == 'make')+sum(roadatb3 == 'miss'))
        roadpoints += roadatb3perc*1.5*27
        
        roadcorn3 = np.random.choice(cornerthree, 8)
        roadcorn3perc = sum(roadcorn3 == 'make')/(sum(roadcorn3 == 'make')+sum(roadcorn3 == 'miss'))
        roadpoints += roadcorn3perc*1.5*8
        
        roadsm = np.random.choice(shortmid, 19)
        roadsmperc = sum(roadsm == 'make')/(sum(roadsm == 'make')+sum(roadsm == 'miss'))
        roadpoints += roadsmperc*19
        
        roadlm = np.random.choice(longmid, 11)
        roadlmperc = sum(roadlm == 'make')/(sum(roadlm == 'make')+sum(roadlm == 'miss'))
        roadpoints += roadlmperc*11
        
        roadatr = np.random.choice(attherim, 35)
        roadatrperc = sum(roadatr == 'make')/(sum(roadatr == 'make')+sum(roadatr == 'miss'))
        roadpoints += roadatrperc*35
        
        roadft = np.random.choice(ft, 19)
        roadftperc = sum(roadft == 'make')/(sum(roadft == 'make')+sum(roadft == 'miss'))
        roadpoints += roadftperc*19
        
        if (homepoints>roadpoints):
            gameswon+=1
    standings.append(gameswon)
standings = np.sort(standings)
highestwins = max(standings)
lowestwins = min(standings)
windeviation = round(statistics.pstdev(standings),3)
avgwins = round(np.average(standings),3)

# Creating histogram 
fig, axs = plt.subplots(1, 1, 
                        figsize =(10, 7),  
                        tight_layout = True) 
  
  
# Remove axes splines  
for s in ['top', 'bottom', 'left', 'right']:  
    axs.spines[s].set_visible(False)  
  
# Remove x, y ticks 
axs.xaxis.set_ticks_position('none')  
axs.yaxis.set_ticks_position('none')  
    
# Add padding between axes and labels  
axs.xaxis.set_tick_params(pad = 5)  
axs.yaxis.set_tick_params(pad = 10) 
  
# Add x, y gridlines  
axs.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.5,  
        alpha = 0.6)   
  
# Creating histogram 
N, bins, patches = axs.hist(standings, bins = 30) 
  
# Setting color 
fracs = ((N**(1 / 5)) / N.max()) 
norm = colors.Normalize(fracs.min(), fracs.max()) 
  
for thisfrac, thispatch in zip(fracs, patches): 
    color = plt.cm.viridis(norm(thisfrac)) 
    thispatch.set_facecolor(color) 
  
# Adding extra features     
plt.xlabel("Wins"+'\nMax: '+str(highestwins)+' | Min: '+str(lowestwins)+
         ' | SD: '+str(windeviation)+' | Avg: '+str(avgwins), fontsize = 15) 
plt.ylabel("Count", fontsize = 15)  
plt.title('Distribution of Wins', fontsize = 18, fontweight = 'bold') 
  
# Show plot 
plt.show() 
