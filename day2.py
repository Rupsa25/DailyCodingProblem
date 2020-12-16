# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 09:27:12 2020

@author: Rupsa
"""

"Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i."
"Time Complexity:O(n^2)"
def newArray(arr):
    l=[]
    for i in range(len(arr)):
        prod=1
        for j in range(len(arr)):
            if i==j:
                continue
            prod=prod*arr[j]
        l.append(prod)
    return l
"Time complexity:O(n)"
def prodArray(arr):
    i=1
    prod=[1 for i in range(len(arr))]
    temp=1
    #left prdoduct
    for i in range(len(arr)):
        prod[i]=temp
        temp*=arr[i]
    #right product
    temp=1
    for j in range(len(arr)-1,-1,-1):
        prod[j]*=temp
        temp*=arr[j]
    return prod
    