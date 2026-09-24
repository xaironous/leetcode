class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            total = 0
            number = nums[i]
            output = 0 

            while number > 0:
                total += number % 10
                number  = number // 10

            if total == i:
                print(total)
                print(i)
                output = i
                return output
            elif i == len(nums)-1 and output == 0:
                return -1


        