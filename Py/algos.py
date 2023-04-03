#imports
import math
import os
import random
import re
import sys


#simple array sum 
# def simpleArraySum(ar):
#     n = 0 
#     for i in ar:
#         n = n + i 
#     return n 
# print(simpleArraySum([1,2,3]))


#mini max sum 
# def miniMaxSum(arr):
#     maxx = max(arr)
#     minn = min(arr)
#     i = 0 
#     for i in arr: 
#         a = sum(arr) - maxx 
#         b = sum(arr) - minn 
#     print(a,b)
# print(miniMaxSum([1,3,5,7,9]))


#plus-minus
# def plusMinus(arr):
#     pos = 0 
#     neg = 0 
#     zero = 0 
#     for i in arr:
#         if i>0: pos += 1
#         elif i<0: neg += 1
#         else: zero += 1 
#     print(pos/len(arr))
#     print(neg/len(arr))
#     print(zero/len(arr))
# print(plusMinus([-4, 3, -9, 0, 4, 1]))


#very big sum
# def aVeryBigSum(ar):
#     sum = 0 
#     for i in range(len(ar)): sum += ar[i]
#     return sum 


#diagonal difference
def diagonalDifference(arr):
    matrix = 0
    res = 0 
    for i in range(0, len(arr)): matrix = matrix + arr[i][i]
    for j in range(0, len(arr)): res = res + arr[j][len(arr)-1-j]
    return abs(matrix-res)