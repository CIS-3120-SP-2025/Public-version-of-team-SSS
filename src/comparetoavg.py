def comparetoavg(a, b, c, avg):
    '''
    This function compares each number to the average and prints if it is
    greater,less or equal to it.
    It also adds up everytime it is equal to the average and prints how many at the end.
    '''
    x=0                                                           #Variable created to hold how many were equal to the average

    for i in [a,b,c]:                                             #For loop to compare the different numbers to the average
        if i == avg:                                              #if it is equal, we add 1 to the count and we print that it is equal
            x+=1
            print(f"{i} is equal to the average")
        elif i > avg:                                             #if it is greater, we just print it
            print (f"{i} is greater than the average")
        else:                                                     #if it is less, we just print it
            print (f"{i} is less than the average")
    print (f"Number of values equal to the average: {x}")         #We print total numbers count that were equal to the average.
