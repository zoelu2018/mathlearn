import sys ,os
sys.path.append(os.path.dirname(__file__))  
print(sys.path)
from Stack import Stack
def dividepy2(decNumber):
    remstack = Stack()
    while decNumber>0:
        rem = decNumber%2
        remstack.push(rem)
        decNumber = decNumber//2
    binString = ''
    while not remstack.isEmpty():
        binString = binString+str(remstack.pop())
    return binString


print(dividepy2(109))