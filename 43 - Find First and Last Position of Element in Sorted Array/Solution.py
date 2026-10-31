class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def find_bound(is_first):
            left, right = 0, len(nums) - 1
            bound_index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    bound_index = mid
                    if is_first:
                        right = mid - 1  
                    else:
                        left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return bound_index

        start = find_bound(True)
        if start == -1:
            return [-1, -1]

        end = find_bound(False)
        return [start, end]
