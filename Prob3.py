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
runs=0
while runs <= N:
    S = nSidedDie(np.array ([p0,1-p0])) - 1 #this function is designed for die, so subtracting 1 will give 0 or 1.
    if S == 1:
        R = nSidedDie(np.array ([e1,1-e1])) - 1
    elif S == 0:
        R = nSidedDie(np.array ([1-e0, e0])) - 1
    if R==1:
        runs+=1
        if S==1:
            successes+=1
pote = successes/N 
print('conditional probability P(S=1|R=1). p=',pote)
