def febonacci(end):
    mylist = [1,2]
    temp = 3
    i = 0
    while temp < end :
        mylist.append( temp )
        i += 1
        temp = mylist[i] + mylist[i+1]
    return mylist

def getEvenSum(anylist):
    mysum = 0
    for number in anylist :
        if number % 2 == 0:
            mysum += number
    return mysum

four_mil = 4000000
result = febonacci(four_mil)

print getEvenSum(result)
