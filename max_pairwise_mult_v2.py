#Uses python3
'''
MaximumPairwiseProductProblem: Find the maximum product of two distinct numbers
in a sequence of non-negative integers.
'''

n = int(input())
a = [int(x) for x in input().split()]

a.sort()
print(a[-1]*a[-2])
