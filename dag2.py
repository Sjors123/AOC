# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 19:56:26 2020

@author: Sjors
"""
text_file = open("dataset2.txt", "r")
data = text_file.readlines()
res = list(map(lambda st: str.replace(st, ": ", "-"), data)) 
used_data = list(map(lambda st: str.replace(st, " ", "-"), res))
final_data=[0] *len(used_data)
total = 0
for i in range(len(used_data)):
   final_data[i]= used_data[i].split('-')
for i in final_data:
    number = i[3].count(i[2])
    if int(i[0])<= number <= int(i[1]):
        total=total+1
print(total)
total2=0
for i in final_data:
    string=i[3]
    if string[int(i[0])-1] == i[2]:
        if  string[int(i[1])-1] != i[2]:
            total2=total2+1
    if string[int(i[1])-1] == i[2]:
        if  string[int(i[0])-1] != i[2]:
            total2=total2+1   

print(total2)
