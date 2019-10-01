import numpy as np

p0=0.35  
e0=0.04  
e1=0.07

N = 100000 #number of times to repeat the experiment

def nSidedDie(p): #flips the unfair die a single time and returns the result
    n = len(p)    
    cs = np.cumsum(p)
    cp = np.append(0,cs)
    r = np.random.rand()
    for k in range(0,n):
        if r>cp[k] and r<=cp[k+1]:
            d=k+1   
    return d


successes = 0
for num in range(N):

pote = successes/N 
print(pote)
