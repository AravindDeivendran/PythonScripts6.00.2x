#producePlot(lowTemps, highTemps):
import pylab

inFile = open('C:/Aravind/Learning/EdX/6.00.2x/Scripts/julyTemps.txt')
highTemps = []
lowTemps = []
diffTemps = []
for line in inFile:
    fields = line.split('\n')[0].split(' ')
    if len(fields) == 3 and fields[0].isdigit():
        print fields
        lowTemps.append(int(fields[2]))
        highTemps.append(int(fields[1]))
        diffTemps.append(int(fields[1]) - int(fields[2]))
        
pylab.figure(1)
print len(diffTemps)
pylab.plot(range(1,32),diffTemps)
pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')
pylab.show()
