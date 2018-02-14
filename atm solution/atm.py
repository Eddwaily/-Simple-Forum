
def withdraw(request):
    money= 500
    paperValues= [ 100, 50, 10, 5, 1]
    assert request>0, "Invalid input"
    assert request<=money, "Balance Not Enough !"
    print "*************"
    print "Delivering "+ str(request)+ "$ to client:"
    for x in paperValues :
        while request>=x :
            print "give"+ str(x)
            request-= x
    print "**** Done ! ****"
    
#test any value here
withdraw(250)
