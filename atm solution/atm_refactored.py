
def withdraw( money, request):
    paperValues= [ 100, 50, 10, 5, 1]
    remaining= money - request
    
    if request <= 0 :
        print "Invalid input !" ; return money
    if request > money :
        print "Balance Not Enough !" ; return money

    print "Current Balance: "+ str(money)
    print "Delivering "+ str(request)+ "$ to client:"
    for x in paperValues:
        while request >= x:
            print "give"+ str(x)
            request -= x
    print "**** Done ! ****"
    return remaining

#test any value here
balance = 1000
balance = withdraw( balance, 750 )
print "Remaining balance " + str( balance )
