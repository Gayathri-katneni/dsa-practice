class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            # Prevents potential integer overflow in other languages, 
            # equivalent to (left + right) // 2
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1  # Target is in the right half
            else:
                right = mid - 1 # Target is in the left half
                
        return -1  # Target not found
