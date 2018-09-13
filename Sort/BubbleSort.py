# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp



array = [1,3,4,1,84,2,42,2,33,45,46,5,56,64,56,464,64,6,1,2,4]
print(array)
bubbleSort(array)
print(array)