class Solution(object):
    def jump(self, nums):
        """
        Greedy BFS-by-levels: each jump covers a window of indices.
        Time: O(n), Space: O(1)

        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        current_end = 0   # farthest index reachable with `jumps` jumps
        farthest = 0      # farthest index reachable with `jumps + 1` jumps

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    break

        return jumps
