# Uses python3
'''
Maior Divisor Comum
'''

def mdc(a,b):
    if b==0:
        return a
    aa = a % b
    return mdc(b,aa)

a, b = [int(x) for x in input().split()]
print(mdc(a,b))
