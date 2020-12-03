# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:34:51 2020

@author: esdeb
"""
data3 = open('data3.txt','r').read().split('\n')
def numbers_of_trees(data,rows,collums):
    tree=0
    for i in range(len(data)):
        x = collums*i
        while x > len(data[0])-1:
            x+=-len(data[0])  
        if rows*i > len(data):
            break
        if data[i*rows][x] == '#':
            tree = tree+1;
    return tree
def main():
    trees1 = numbers_of_trees(data3,1,1)
    trees2 = numbers_of_trees(data3,1,3)
    trees3 = numbers_of_trees(data3,1,5)
    trees4 = numbers_of_trees(data3,1,7)
    trees5 = numbers_of_trees(data3,2,1)
    total = trees1*trees2*trees3*trees4*trees5
    print(f'totaal = {total}')    
main()