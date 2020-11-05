def fizbuz(checkNumber):
    if checkNumber % 3 == 0 and checkNumber % 5 == 0:
        print("fizzBuzz: " +str(checkNumber))
    elif checkNumber % 3 == 0:
        print("fizz: " + str(checkNumber))
    elif checkNumber % 5 == 0:
        print("buzz: " +str(checkNumber))
    else:
        print("wrong number!")
        

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,18,21,90] 
for number in numbers:
    check = fizbuz(number)