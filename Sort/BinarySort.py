# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

def binarySearch(low, high, target, nums):
    mid = 0
    while low < high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid
        else:
            low = mid

    return mid



def binarySort(array):

    for i in range(len(array)):
        temp = array[i]
        j = i - 1
        if temp < array[j]:
            index = binarySearch(0,i,temp,array)
            print(i, index)
            while(j >= index):
                array[j + 1] = array[j]
                j = j - 1
            array[j + 1] = temp





array = [2,1,3]
binarySort(array)
print(array)
