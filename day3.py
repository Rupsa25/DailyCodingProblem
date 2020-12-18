# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 09:09:33 2020

@author: Rupsa
"""

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def inputTree():
    rootData=input()
    if rootData=='-1':
        return None
    root=Node(rootData)
    left=inputTree()
    right=inputTree()
    root.left=left
    root.right=right
    return root


def serialize(root):
    return serializeHelper(root)
def serializeHelper(root,l=[]):
    if root!=None:
        l.append(root.val)
    else:
        l.append('-1')
        return
    serializeHelper(root.left,l)
    serializeHelper(root.right,l)
    return l


#input should be reversed output of serialize
def deserialize(s):
    rootdata=s.pop()
    if rootdata=='-1':
        return None
    root=Node(rootdata)
    root.left=deserialize(s)
    root.right=deserialize(s)
    return root


    
    
    

def printTree(root):
    if root==None:
        return 
    print(root.val,end=":")
    if root.left!=None:
        print(root.left.val,end=",")
    if root.right!=None:
        print(root.right.val,end="")
    print()
    printTree(root.left)
    printTree(root.right)
    
        
    
        