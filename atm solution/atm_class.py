def line():
    print "="*30
    
class ATM:
    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name



    def withdraw(self,request):
        paperValues = [ 100, 50, 10, 5, 1]

        line()
        print "Welcome to " + self.bank_name +" !"
        print "Current Balance: "+ str(self.balance)

        if request <= 0 :
            print "Invalid input !" ;
        elif request > self.balance :
            print "Balance Not Enough !" ;
        else:
            print "Delivering " + str(request) + "$ to client:"
            for x in paperValues:
                while request >= x:
                    print "give"+ str(x)
                    request -= x
            self.balance -= request
            print "Remaining balance " + str( self.balance )
            line()
        return self.balance

#making objects of type ATM
atm1 = ATM( 500, "AMAN BANK")
atm2 = ATM( 1500, "WAHDA BANK")

#testing withdraw method for those objects
atm1.balance = atm1.withdraw(501)
