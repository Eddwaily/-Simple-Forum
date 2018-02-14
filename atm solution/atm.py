
def withdraw(request):
    money = 500
    paperValues = [ 100, 50, 10, 5, 1]
    if request <= 0 :
        print "Invalid input !" ; return 0
    elif request > money:
        print "Balance Not Enough !" ; return 0
    else:
        print "*************"
        print "Delivering "+ str(request)+ "$ to client:"
        for x in paperValues :
            while request >= x :
                print "give" + str(x)
                request -= x
        print "**** Done ! ****"
        return 1

#test any value here
withdraw(250)
