# Uses python3
a, b = [int(x) for x in input().split()]

def mdc(a,b):
    if b==0:
        return a
    aa = a % b
    return mdc(b,aa)

def lcm(a,b):
    mdc_new = mdc(a,b)
    return ((a*b)//mdc_new)


print(lcm(a,b))
