# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

def selectSort(list):
    for i in range(0,len(list)-1):
        min = i
        for j in range(i+1, len(list)):
            if list[j] < list[min]:
                min = j
        if min != i:
            list[i],list[min] = list[min],list[i]


array = [1,3,4,1,84,2,42,2,33,45,46,5,56,64,56,464,64,6,1,2,4]
print(array)
selectSort(array)
print(array)