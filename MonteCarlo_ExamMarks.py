import random
import pylab
def sampleQuizzes():
    totCnt = 0
    cnt = 0
    for i in range(10000):
        mid1 = 50 + random.random() * 30
        mid2 = 60 + random.random() * 30
        final = 55 + random.random() * 40
        total = 0.25 * mid1 + 0.25 * mid2 + 0.5 * final
        totCnt += 1
        if total >= 70 and total <= 75:
            cnt += 1
    return cnt/float(totCnt)

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    lstScore = []
    for i in range(numTrials):
        mid1 = 50 + random.random() * 30
        mid2 = 60 + random.random() * 30
        final = 55 + random.random() * 40
        total = 0.25 * mid1 + 0.25 * mid2 + 0.5 * final
        lstScore.append(total)
    return lstScore

def plotQuizzes():
    # Your code here
    lstScore = generateScores(10000)
    pylab.hist(lstScore,bins=7)
    pylab.title("Distribution of scores")
    pylab.xlabel("Final Score")
    pylab.ylabel("Number of Trials")
    pylab.legend()
    pylab.show()
    
plotQuizzes()

    