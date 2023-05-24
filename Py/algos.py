#imports
import math
import os
import random
import re
import sys



#solveMeFirst
# def solveMeFirst(a,b):
# 	return a+b 
# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)


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
# def diagonalDifference(arr):
#     matrix = 0
#     res = 0 
#     for i in range(0, len(arr)): matrix = matrix + arr[i][i]
#     for j in range(0, len(arr)): res = res + arr[j][len(arr)-1-j]
#     return abs(matrix-res)


#time conversion
# def timeConversion(s):
#     #check if last 2 elements of time is AM and first 2 are 12 
#     if s[-2:] == 'AM' and s[:2] == '12': return '00' + s[2:-2]
#     #remove AM 
#     elif s[-2:] == 'AM': return s[:-2]
#     #check if last 2 elements of time is PM and first 2 are 12 
#     elif s[-2:] == 'PM' and s[:2] == '12': return s[:-2]
#     #add 12 to hours and remove PM 
#     else: return str(int(s[:2]) + 12) + s[2:8]
# print(timeConversion('07:05:45PM'))


#super reduced string
# def superReducedString(s):
#     res = []
#     for i in range(len(s)):
#         if len(res)==0 or s[i] != res[-1]: res.append(s[i])
#         else: res.pop()
#     return 'Empty String' if len(res)==0 else ''.join(res)
# print(superReducedString('aaabccddd'))


#find digits (divisible)
# def findDigits(n):
#     count = 0
#     for i in list(str(n)):
#         if int(i) != 0 and n % int(i)==0: count += 1
#     return count 
# print(findDigits(124)) 
# print(findDigits(10)) 


#pangram
# def pangrams(s):
#     letters = 'abcdefghijklmnopqrstuvwxyz'
#     for i in letters: 
#         if i not in s.lower(): return 'not pangram'
#     return 'pangram'
# print(pangrams('The quick brown fox jumps over the lazy dog'))


#staircase 
# def staircase(n):
#     for i in range(1, n+1): print(' ' * (n-i) + '#' * i)
# print(staircase(6))


#grading students
# adds = [0,0,0,2,1]
# def gradingStudents(grades):
#     return [i if i<38 else i + adds[i%5] for i in grades]

