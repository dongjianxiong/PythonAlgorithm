# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

def insertSort(array):
    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        while(j > 0 and array[j] > temp):#为什么temp不能直接用成array[i]，因为此时的array[i]已经变成array[j+1]了
            array[j+1] = array[j]
            j = j - 1
        if j != i - 1:
            array[j+1] = temp


# array = [1,3,4,1,84,2,42,2,33,45,46,5,56,64,56,464,64,6,1,2,4]
# print(array)
# insertSort(array)
# print(array)
