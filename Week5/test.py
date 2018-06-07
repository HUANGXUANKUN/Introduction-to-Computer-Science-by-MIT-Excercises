import time
def c(c):
    return c*9/5 +32

t0 = time.clock()
c(1000000)
t1 = time.clock() - t0
print(t0)
print()
print(t1)
print('t =',t0//60,':',t1,'s,')