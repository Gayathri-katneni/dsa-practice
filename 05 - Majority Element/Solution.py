class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1
        for num in count:
            if count[num] > len(nums) / 2:
                return num
