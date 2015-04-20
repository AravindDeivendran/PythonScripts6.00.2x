# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    
    # TODO
    dic = []
    numViruses = 100 
    maxPop = 1000 
    maxBirthProb = 0.1 
    clearProb = 0.05 
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005 
    
    nStepsBefore = 150
    nStepsMiddle = 150
    nStepsAfter = 150
    
    #for i in range(0,nStepsBefore +nStepsAfter ):
    #    dic[i] = []

    pylab.figure()
    
    for j in range(0, numTrials):
        viruses = []
        for ctr in range(0,numViruses):
            viruses.append(ResistantVirus(maxBirthProb,clearProb,resistances,mutProb))
    
        patient = TreatedPatient(viruses,maxPop)
        
        for i in range(0,nStepsBefore):
            patient.update()
        #    dic[i].append(patient.getTotalPop())

            
        patient.addPrescription('guttagonol')
        
        for i in range(0,nStepsMiddle):
            patient.update()
        #    dic[i].append(patient.getTotalPop())

            
        patient.addPrescription('grimpex')
        
        for i in range(0,nStepsAfter):
            patient.update()
        
        dic.append(patient.getTotalPop())
        
    ctr = 0
    for value in dic:
        if value >= 0 and value <= 50:
            ctr += 1
    
    print ctr
    print ctr/float(len(dic))

    pylab.hist(dic)
    pylab.show()
            
                                            



simulationDelayedTreatment(500)
#simulationDelayedTreatment(1000)






#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # TODO
