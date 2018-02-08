number = 655453535340

while True:
    foundFactor = False
    for i in xrange(2, number):
        if number % i == 0:
            number /= i
            foundFactor = True
            break
        if not foundFactor:
            print 'This number is not prime'
            break

print number
