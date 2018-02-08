#Uses python3
'''
Maior Divisor Comum
'''

a = int(input())
b = int(input())

def mdc(a,b):
    if b==0:
        return a
    aa = a % b
    return mdc(b,aa)

print(mdc(a,b))
