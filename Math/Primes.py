def primegenerator(limit, primes = [3]):
    'From a given limit, generates that many prime numbers'
    numOfPrimes = 3
    while len(primes) < limit - 1: # one cause something
        for prime in primes:
            if numOfPrimes % prime == 0:
                numOfPrimes += 2
                break
            elif prime != primes[-1]:
                continue #Keeps the loop if haven't reached end
            else:
                primes.append(numOfPrimes)
                numOfPrimes += 2
                break
    if 2 not in primes:
        primes.insert(0,2)
    return primes

def primefind(primes):
    'List of primes'
    query = raw_input('What number? ')
    if query.endswith(('st', 'nd', 'th', 'rd',)):
        return 'The %s prime is %d' %(
        query, primes[int(query[0:-2]) - 1])
    elif int(query) in primes:
        return '%d is the %dth prime' %(
        int(query), primes.index(int(query) - 1))
    elif not int(query):
        return 'Stopping'
    else:
        return '%d is not a prime' % int(query)
    
if __name__ == '__main__':
    limit = input('Enter a limit please: ')
    primes = primegenerator(limit)
    print '-------------------------' * 2
    print 'Just to check: %d' %len(primes)
    print 'The answer is: %d' %primes[-1]
    print 'The sum of the primes is: %d' %sum(primes)
    print 'Search for a specific number'
    print '-------------------------' * 2
    while True:
        try:
            temp = primefind(primes)
            if temp is 'Stopping':
                break
            else:
                print temp
        except:
            print 'Follow syntax rules, & stay within %d'%(int(primes[-1]))
