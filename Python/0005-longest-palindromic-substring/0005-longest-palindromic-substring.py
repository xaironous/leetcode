class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        palindrome = s[0]
        count = 1

        for i in range(len(s)):
            left = i
            right = i

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > count:
                        palindrome = s[left:right + 1]
                        count = right - left + 1

                    left -= 1
                    right += 1
                else:
                    break

            left = i
            right = i + 1

            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left + 1 > count:
                        palindrome = s[left:right + 1]
                        count = right - left + 1

                    left -= 1
                    right += 1
                else:
                    break

        return palindrome