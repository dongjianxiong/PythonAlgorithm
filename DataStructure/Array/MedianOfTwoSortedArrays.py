# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
#
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = None
        if (nums1 == None or len(nums1) == 0) and (nums2 == None or len(nums2) == 0):
            return -1
        elif (nums1 == None or len(nums1) == 0):
            nums = nums2
        elif (nums2 == None or len(nums2) == 0):
            nums = nums1
        elif nums2[0] > nums1[len(nums1) - 1]:
            nums1.extend(nums2)
            nums = nums1
        elif nums1[0] > nums2[len(nums2) - 1]:
            nums2.extend(nums1)
            nums = nums2
        media = 0
        if nums != None:
            media = self.findMedian(nums)
        else:
            nums = nums1
            start = len(nums1)-1
            # print(start,nums)
            nums.extend(nums2)
            index = 0
            for i in range(start,len(nums)):
                temp = nums[i]
                j = i - 1
                if temp < nums[j]:
                    index = self.findInsertIndex(index, j, temp, nums)
                    while (j >= index):
                        nums[j + 1] = nums[j]
                        j = j - 1
                        nums[j + 1] = temp
                if index > len(nums)//2:
                    break
            media = self.findMedian(nums)
            print(nums)
        return media

        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
    def findMedian(self,nums):
        median = 0
        m = len(nums) % 2
        index = len(nums) // 2
        if m > 0:
            median = nums[index] * 2 / 2
        else:
            median = (nums[index] + nums[index - 1]) / 2

        return median

    def findInsertIndex(self,low, high, target, nums):
        mid = 0
        while low <= high:
            print(1)
            if low == high:
                if nums[low] > target:
                    return low
                else:
                    return low + 1
            mid = (high + low) // 2
            if nums[mid] == target:
                return mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return mid


solution = Solution()
nums1 = [1,3,4,20,24,56,76,78,89]
nums2 = [2,5,6,9,20,24,56,79,98]
print(solution.findMedianSortedArrays(nums1,nums2))