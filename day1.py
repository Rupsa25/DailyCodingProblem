# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:44:07 2020

@author: Rupsa
"""
"""Time complexity O(logn)"""
"""Given a list of numbers and a number k, return whether any two numbers from the list add up to k."""
def sumExists(arr,k):
    arr.sort()
    i=0
    j=len(arr)-1
    while i<j:
        if arr[i]+arr[j]==k:
            return True
        elif arr[i]+arr[j]>k:
            j-=1
        elif arr[i]+arr[j]<k:
            i+=1
    return False