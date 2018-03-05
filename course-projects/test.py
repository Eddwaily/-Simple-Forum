def myfunc():
    number = 1
    mylist = (1,21,1)
    while(1):
        counter = 0
        for i in mylist:
            if number % i:
                pass
            else:
                counter += 1
        if counter ==20:
            return number
        else:
            number += 1
print myfunc()
