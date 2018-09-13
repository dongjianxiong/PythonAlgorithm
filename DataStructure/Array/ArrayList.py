# coding:utf-8
# _*_coding:utf-8_*_
__author__ = 'Lenny'

# X is a good number if after rotating each digit individually by 180 degrees, we get a valid
# number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
# A number is valid if each digit remains a digit after rotation. 0, 1,
# and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to
#  each other, and the rest of the numbers do not rotate to any other number and become invalid.
# Now given a positive number N, how many numbers X from 1 to N are good?

class Solution:

    def invalidNumber(self,N):
        array = [3, 4, 7]
        ret = 1
        for n in array:
             if N == n:
                 ret = 0
        return ret

    def norotateNumber(self,N):
        array = [0, 1, 8]
        ret = 0
        for n in array:
             if N == n:
                 ret = 1
                 break
        return ret


    def rotatedDigits(self, N):
        # print(N%10)
        array = []
        count = 0
        for i in range(1,N+1):
            valueNumbers = []
            num = i
            isValue = 1
            noRotated = 1
            while (num > 0):
                n = num % 10
                num = num // 10
                if  self.invalidNumber(n) == 0:
                    isValue = 0
                    break
                else:
                    if noRotated == 1:
                        noRotated = self.norotateNumber(n)
                    valueNumbers.append(n)
            if isValue == 1 and noRotated == 0:
                count = count + 1
                array.append(i)
        print(array)
        return count


solution = Solution()
solution.rotatedDigits(2)
