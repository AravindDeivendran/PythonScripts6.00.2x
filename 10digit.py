'''
i = 6210001000
ctr = 9
bFound = True
no = i
while ctr > 0:
    n = no % 10
    print 'doing ' + str(n)
    print 'ctr ' + str(ctr)
    if not (n == str(i).count(str(ctr))):
        print str(i).count(str(ctr))
        bFound = False
        break
    no = no / 10 
    ctr -= 1
if bFound:
    print i
else:
    print 'failed'

'''
i = 1000000000
while i < 10000000000:
    print 'doing ' + str(i)
    ctr = 9
    bFound = True
    no = i
    while ctr > 0:
        n = no % 10
        if not (n == str(i).count(str(ctr))):
            bFound = False
            break
        no = no / 10 
        ctr -= 1
    if bFound:
        print i
        break
    i += 1

