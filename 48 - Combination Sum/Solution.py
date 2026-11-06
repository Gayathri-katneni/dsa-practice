class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        candidates.sort()
        
        def backtrack(remain, combo, start_idx):
            if remain == 0:
                res.append(list(combo))
                return
            
            for i in range(start_idx, len(candidates)):
                if candidates[i] > remain:
                    break
                
                combo.append(candidates[i])
                
                backtrack(remain - candidates[i], combo, i)
                
                combo.pop()

        backtrack(target, [], 0)
        return res
