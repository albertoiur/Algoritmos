# Uses python3

n = int(input())

if n==0:
    print(n)
    exit()

if n==1:
    print(n)
    exit()

a,b = 0,1

for i in range(1,n):
    a,b = b, (a+b) % 10
    #print(i,a,b)

print(b)    
    
