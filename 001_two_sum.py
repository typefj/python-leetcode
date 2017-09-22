class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp_d = {}
        for idx, n in enumerate(nums):
            if n in tmp_d:
                return [tmp_d[n], idx]
            else:
                tmp_d[target-n] = idx
