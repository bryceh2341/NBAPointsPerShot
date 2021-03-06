import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import colors 
import statistics

player3 = []

for i in range(38):
    player3.append('make')
for i in range(62):
    player3.append('miss')

playertotal = []
for i in range(1000000):

        
    player3result = np.random.choice(player3, 350)
    player3perc = 100*(sum(player3result == 'make')/(sum(player3result == 'make')+sum(player3result == 'miss')))
    playertotal.append(round(player3perc,1))
    
playertotal = np.sort(playertotal)
highestperc = max(playertotal)
lowestperc = min(playertotal)
windeviation = round(statistics.pstdev(playertotal),3)
avgtotal = round(np.average(playertotal),3)

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
N, bins, patches = axs.hist(playertotal, bins = 30) 
  
# Setting color 
fracs = ((N**(1 / 5)) / N.max()) 
norm = colors.Normalize(fracs.min(), fracs.max()) 
  
for thisfrac, thispatch in zip(fracs, patches): 
    color = plt.cm.viridis(norm(thisfrac)) 
    thispatch.set_facecolor(color) 
  
# Adding extra features     
plt.xlabel("3-Point %"+'\nMax: '+str(highestperc)+' | Min: '+str(lowestperc)+
         ' | SD: '+str(windeviation)+' | Avg: '+str(avgtotal), fontsize = 15) 
plt.ylabel("Count", fontsize = 15)  
plt.title('Distribution of 3-Point %', fontsize = 18, fontweight = 'bold') 
  
# Show plot 
plt.show() 
