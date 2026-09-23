class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        buffer = ""
        count = 0


        for i in range(len(s)):
            if s[i] in buffer:
                buffer = buffer.split(s[i], 1)[1]
                
            buffer += (s[i])
            if count < len(buffer):
                count = len(buffer)
        
        return count