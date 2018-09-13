# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
#
# Given "abcabcbb", the answer is "abc", which the length is 3.
#
# Given "bbbbb", the answer is "b", with the length of 1.
#
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
# "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        if s == None or len(s) == 0:
            return 0
        letterDict = {}
        maxSubstring = s[:1]
        curSubstring = ""
        for letter in s:
            if letter in letterDict:
                if len(curSubstring) > len(maxSubstring):
                    maxSubstring = curSubstring
                print("前" + curSubstring + "  -len-",len(curSubstring))
                i = 1
                for c in curSubstring:
                    if c == letter:
                        curSubstring = curSubstring[i:len(curSubstring)]
                        break
                    else:
                        i = i + 1
                curSubstring = curSubstring + letter

            else:
                letterDict[letter] = 1
                curSubstring = curSubstring + letter
        if len(curSubstring) > len(maxSubstring):
            maxSubstring = curSubstring
        print(maxSubstring)
        return len(maxSubstring)
        """
        :type s: str
        :rtype: int
        """

    def lengthOfLongestSubstring1(self, s):
        if s == None or len(s) == 0:
            return 0
        letterDict = {}
        ptr0 = 0
        ptr1 = 0
        max = 1
        for letter in s:
            if letter in letterDict:
                if ptr1 - ptr0 > max:
                    max = ptr1 - ptr0
                for i in range(ptr0,len(s)):
                    if s[i] == letter:
                        break
                    else:
                        ptr0 = ptr0 + 1
            else:
                ptr1 = ptr1 + 1
            letterDict[letter] = 1

        if ptr1 - ptr0 > max:
            max = ptr1 - ptr0
        return max
        """
        :type s: str
        :rtype: int
        """

    def lengthOfLongestSubstring2(self, s):
        if s == None or len(s) == 0:
            return 0
        letterDict = {}
        ptr0 = 0
        ptr1 = 0
        max = 1
        for letter in s:
            if letter in letterDict:
                if ptr1 - ptr0 > max:
                    max = ptr1 - ptr0
                ptr0 = letterDict[letter] + 1
            letterDict[letter] = ptr1
            ptr1 = ptr1 + 1
        if ptr1 - ptr0 > max:
            max = ptr1 - ptr0
        return max


solution = Solution()
print(solution.lengthOfLongestSubstring("abab"))