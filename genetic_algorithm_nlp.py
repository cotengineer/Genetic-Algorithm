# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 09:49:05 2019

@author: cotengineer
"""

#MAXIMIZE NLP with Genetic Algorithm

import random
import time
import math
import matplotlib.pyplot as plt

start = time.time()
###########################################################################

x = [1,1,1]
G = 0
fit = []
GENES = 0
gen = 1
def getKey(item):
    return item[0]


#Initiate random first generation
while GENES < 16:
    x[0] = random.uniform(0,10)
    x[1] = random.uniform(0,10)
    x[2] = random.uniform(0,10)
    
    cond = (((x[0]+x[1]+x[2]) < 15) and ((x[0]*x[1]*x[2]) > 0.75) and (x[0] < 10) and (x[1] < 10) and (x[2] < 10) and (x[0] > 0) and (x[1] > 0) and (x[2] > 0))
    
    if cond == True:
        G = abs((math.cos(x[0]))**4 + (math.cos(x[1])**4) + (math.cos(x[2])**4) - 2 * ((math.cos(x[0])**2) * (math.cos(x[1])**2) * (math.cos(x[2])**2))/(math.sqrt((1*x[0]**2) + (2*x[1]**2) + (3*x[2]))))
        roll = G,x[0],x[1],x[2]
        fit.append(roll)
        GENES += 1
       
        
    elif cond == False:
        pass
    
fit.sort(reverse = True,key = getKey)
top4 = [fit[0],fit[1],fit[2],fit[3]]
best_of_gen = [top4[0][0]]
best_score = G
best_x = x

#Next Generations
while gen < 50:
    fit = []
    GENES = 0
    while GENES < 16:
        
        #the crossover of best parents of each generation
        rc = [0,1,3]        
                
        x[0] = (top4[0][1] + top4[random.randint(1,3)][random.randint(1,3)])/2
        x[1] = (top4[0][2] + top4[random.choice(rc)][random.choice(rc)])/2
        x[2] = (top4[0][3] + top4[random.randint(0,2)][random.randint(0,2)])/2
               
        cond = (((x[0]+x[1]+x[2]) < 15) and ((x[0]*x[1]*x[2]) > 0.75) and (x[0] < 10) and (x[1] < 10) and (x[2] < 10) and (x[0] > 0) and (x[1] > 0) and (x[2] > 0))
        
        if cond == True:
            G = abs((math.cos(x[0]))**4 + (math.cos(x[1])**4) + (math.cos(x[2])**4) - 2 * ((math.cos(x[0])**2) * (math.cos(x[1])**2) * (math.cos(x[2])**2))/(math.sqrt((1*x[0]**2) + (2*x[1]**2) + (3*x[2]))))
            roll = G,x[0],x[1],x[2]
            fit.append(roll)
            GENES += 1
            if G > best_score:
                best_score = G
                best_x = x
           
            
        elif cond == False:
            pass
        
    fit.sort(reverse = True,key = getKey)
    top4 = [fit[0],fit[1],fit[2],fit[3]]
    best_of_gen.append(top4[0][0])
    gen += 1

###########################################################################
end = time.time()

print("")
print("Finished in:", end-start)


plt.plot(best_of_gen)
plt.title('Genetic Algorithm for NLP',fontsize=18,color='r')
plt.xlabel('Generation',fontsize=14,color='b')
plt.ylabel('Generation Best Score',fontsize=14,color='b')
plt.grid()
plt.show()

print("Maximum Value:",best_score)
print("")
print("When x =",best_x)
