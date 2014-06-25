def getInput():
    while True:
        try:
            limit = input('Please input your Term limit:')
            return (limit)
        except:
            'Please enter integers'

def fibSeq(limit):
    sequence = [1,2]
    while len(sequence) < limit:
        sequence.append(sequence[-2] + sequence[-1])
    return sequence

def fibFind(sequence):
    fibNumber = raw_input('Which Fib Num would you like to find? ')
    if fibNumber.endswith(('st', 'nd', 'th', 'rd',)):
        print 'The %s Fib Num is %d' %(
                fibNumber, sequence[int(fibNumber[:-2]) - 1])
    else:
        print 'Please put a suffix (like 5th)'
    print

if __name__ == '__main__':
    limit = getInput()
    sequence = eval('fibSeq(%d)' % (limit))
    print sequence
    print
    while True: # Also testing, make it a condional if implemented
        fibFind(sequence)