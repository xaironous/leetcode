class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(len(nums)):
            total = 0
            number = nums[i]

            while number > 0:
                total += number % 10
                number  = number // 10

            if total == i:
                print(total)
                print(i)
                return i
        return -1


        