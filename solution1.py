def Reverse():
    while( not Q.Empty()):
        S.push(Q.deQueue())
    while( not S.Empty()):
        Q.enQueue(S.pop())