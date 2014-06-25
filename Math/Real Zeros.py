def RealZeros(equation):
    numerator,denominator, answer = [],[],[]
    firstcoe,lastcoe = equation[0],int(equation[-1])
    for i in range(1,lastcoe/2 + 1):
        if lastcoe % i == 0:
            numerator.append(i)
    numerator.append(lastcoe)
    if firstcoe.isdigit() is False:
        denominator = [1, -1]
    else:
        firstcoe = int(firstcoe)
        for i in range(1,firstcoe +1):
            if firstcoe % i == 0:
                denominator.append(i)
                denominator.append(-i)
    options = Join(numerator, denominator)
    print 'The options are {}'.format(options)
    print
    for x in options:
        if eval(equation) == 0:
            answer.append(x)
    return answer

def Join(list1,list2):
    list3 = []
    for i in list1:
        for z in list2:
            list3.append(float(i)/float(z))
    for item in list3:
        if list3.count(item) > 1:
            list3.remove(item)
    return list3
while True:
    question = raw_input('Enter Equation ')
    print RealZeros(question)