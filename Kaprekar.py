"""
Find Kaprekar numbers
"""
def isKaprekar(x):
    OK = False
    sqrt= str(x**2) #Decimal representation of the square
    for i in range(1, len(sqrt)-1):
        p1 = int(sqrt[:i])
        p2 = int(sqrt[i:])
        if p1 + p2 == x:
            OK = True
            break
    return OK

#for x in range(1001)
#    if isKaprekar(x) = True: print(x)

print([x for x in range(10001) if isKaprekar(x)])
