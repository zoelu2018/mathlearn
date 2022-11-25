import sys ,os
sys.path.append(os.path.dirname(__file__))  
print(sys.path)
from Stack import Stack
def parCheacher(sym):
    s = Stack()
    balanced = True
    index = 0
    while index < len(sym) and balanced:
        symbol = sym[index]
        if symbol == '{[(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top = s.pop()

                if not matcher(top,symbol):
                    balanced= False
        index = index+1
    if balanced and s.isEmpty():
        return  True
    else:
        return False
def matchers(open,close):
    opens = "([{"
    closes = (")]}")
    return opens.index(open) == closes.index(close)

parCheacher('()()()))(')
print(parCheacher('()(}()))('))