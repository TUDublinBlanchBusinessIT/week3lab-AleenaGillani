#AleenaGillani
#07/2/2024
#divisors.py


def divisors(num):
    myList=[]
    for i in range(1, num):
        if num % i == 0:
            myList.append(i)

    return myList

print (divisors(128))
        
