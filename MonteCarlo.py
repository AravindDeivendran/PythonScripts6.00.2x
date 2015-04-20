import random

def DrawBalls():
    choice = [0,0,0,1,1,1]
    res = []
    for i in range(0,3):
        c = random.choice(choice)
        choice.remove(c)
        res.append(c)
    if sum(res) == 0 or sum(res) == 3:
        return True
    else:
        return False
       

            

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    ctr = 0
    for n in range(0,numTrials):
        bRes = DrawBalls()
        if bRes:
            ctr += 1
    
    return ctr/float(numTrials)
        

print noReplacementSimulation(100000)