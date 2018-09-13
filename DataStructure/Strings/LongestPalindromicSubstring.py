# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        if s == None or len(s) == 0:
            return ""
        maxSubstring = s[0]
        curSubstring = ""
        index = 0
        for i in range(0,len(s)):
            for j in range(0, i):
                # print(i,j)
                if s[i] == s[j]:
                    curSubstring = s[j:i+1]
                    print("curSubstring:" + curSubstring)
                    isPalindrome = 1
                    curLen = len(curSubstring)
                    for index in range(0, curLen // 2):
                        if curSubstring[index] != curSubstring[curLen - index - 1]:
                            isPalindrome = 0
                            break
                    if len(curSubstring) >= len(maxSubstring) and isPalindrome == 1:
                        maxSubstring = curSubstring
            index = index + 1
        return maxSubstring
        """
            :type s: str
            :rtype: str
        """

    def longestPalindrome1(self, s):
        if s == None or len(s) == 0:
            return ""
        maxSubstring = s[0]
        curSubstring = ""
        index = 0
        for i in range(0,len(s)):
            for j in range(0, i):
                # print(i,j)
                if s[i] == s[j]:
                    curSubstring = s[j:i+1]
                    # print("curSubstring:" + curSubstring)
                    isPalindrome = 1
                    curLen = len(curSubstring)
                    for index in range(0, curLen // 2):
                        if curSubstring[index] != curSubstring[curLen - index - 1]:
                            isPalindrome = 0
                            break
                    if len(curSubstring) >= len(maxSubstring) and isPalindrome == 1:
                        maxSubstring = curSubstring
            index = index + 1
        return maxSubstring
        """
            :type s: str
            :rtype: str
        """

solution = Solution()
maxSubstring = solution.longestPalindrome1("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
print("result：" + maxSubstring)