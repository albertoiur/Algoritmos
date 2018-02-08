# Uses python3

n = int(input())


if n==0:
    print(n)
    exit()
if n==1:
    print(n)
    exit()


lista = []
lista.append(0)
lista.append(1)

for i in range(2, n+1):
    lista.append(lista[i-1] + lista[i-2])

print(lista[-1])    

