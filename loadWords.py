import string
PATH_TO_FILE = 'C:/Aravind/Learning/EdX/6.00.2x/Scripts/words.txt'

def loadWords():
	inFile = open(PATH_TO_FILE, 'r', 0)
	line = inFile.readline()
	wordlist = string.split(line)
	print "  ", len(wordlist), "words loaded."
	return wordlist

wordlist = loadWords()
#wordlist = ['harassment']
myword = 'locnslnui'
for word in wordlist:

    if (len(word) == len(myword)):
        bFind = True
        for letter in word:
            if  (not (letter in myword )):
                bFind = False
                break
        if bFind:
            print 'Found ' + word
            
# Uncomment the following function if you want to try the code template
# def loadWords2():
# 	try:
# 		inFile = open(PATH_TO_FILE, 'r', 0)
# 	#line of code to be added here#
# 		print "The wordlist doesn't exist; using some fruits for now"
# 		return ['apple', 'orange', 'pear', 'lime', 'lemon', 'grape', 'pineapple']
# 	line = inFile.readline()
# 	wordlist = string.split(line)
# 	print "  ", len(wordlist), "words loaded."
# 	return wordlist
# PATH_TO_FILE = 'words2.txt'
# loadWords2()
# PATH_TO_FILE = 'doesntExist.txt'
# loadWords2()
