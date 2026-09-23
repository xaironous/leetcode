class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = nums1 + nums2 
        merge.sort()

        if len(merge) % 2 == 0:
            median = ((merge[len(merge)/2]) + (merge[(len(merge)/2)-1])) / 2.0
        else:
            median = merge[len(merge)/2]
        return median
        