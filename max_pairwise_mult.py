#Uses python3
'''
Slow algorithm.
MaximumPairwiseProductProblem: Find the maximum product of two distinct
numbers in a sequence of non-negative integers.
O(n^2)
'''

n = int(input())
a = [int(x) for x in input().split()]

product=0

for i in range(n):
    for j in range(i+1 ,n):
        product = max(product, a[i]*a[j])
print(product)
