import pylab

# You may have to change this path
WORDLIST_FILENAME = "C:/Aravind/Learning/EdX/6.00.2x/Scripts/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=15):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    lst = []
    for word in wordList:
        word = word.lower()
        cnt = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
        prop = cnt/float(len(word))
        lst.append(prop)
        
    pylab.hist(lst, numBins)
    pylab.show()

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
