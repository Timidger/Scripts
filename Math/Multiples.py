from time import clock
def multiples2():
    sum = 0
    print 'please enter a number'
    first = input(int)
    print 'please enter a different number'
    second = input(int)
    print 'please enter a maximum limit for the function'
    limit = input(int)
    clock()
    for i in range(1, limit + 1):
        if i % first == 0 or i % second == 0:
            print i
            sum += i
    print
    return (sum)
print 'The sum of the multiples of your chosen numbers is: %d' %multiples2()
print
print 'Time Taken: %f seconds' %clock()
print
raw_input('Function finished, press enter to finish')