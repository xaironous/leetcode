class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merge = [] 
        i = 0
        j = 0
        while i < len(nums1) or j < len(nums2):
            if i >= len(nums1):
                merge.append(nums2[j])
                j += 1

            elif j >= len(nums2):
                merge.append(nums1[i])
                i += 1

            elif nums1[i] > nums2[j]:
                merge.append(nums2[j])
                j += 1

            else:
                merge.append(nums1[i])
                i += 1

        if len(merge) % 2 == 0:
            median = ((merge[len(merge)/2]) + (merge[(len(merge)/2)-1])) / 2.0
        else:
            median = merge[len(merge)/2]
        return median
        