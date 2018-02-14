
def withDraw( money, request):
    paperValues= [ 100, 50, 10, 5, 1]
    assert request>0, "Invalid input"
    assert request<=money, "Balance Not Enough !"
    remaining=money-request

    print "Current Balance: "+ str(money)
    print "Delivering "+ str(request)+ "$ to client:"
    for x in paperValues:
        while request >= x:
            print "give"+ str(x)
            request-=x
    return remaining
    print "**** Done ! ****"

#test any value here
balance= 1000
balance= withDraw(balance,250)
