# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'



def quickSort(array, left, right):

    if left >= right:
        return

    i = left
    j = right
    point = array[i]
    while i < j:

        while array[j] <= point and i < j:
            j = j - 1
        array[i] = array[j]

        while array[i] >= point and i < j:
            i = i + 1
        array[j] = array[i]

    array[i] = point
    quickSort(array,left,i-1)
    quickSort(array,j+1,right)



array = [1,3,4,1,84,2,42,2,33,45,46,5,56,64,56,464,64,6,1,2,4]
print(array)
quickSort(array,0,len(array)-1)
print(array)
