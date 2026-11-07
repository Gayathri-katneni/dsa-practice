class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        results = []
        
        candidates.sort()
        
        def backtrack(start_index, current_combination, remaining_target):
            if remaining_target == 0:
                results.append(list(current_combination))
                return
            
            for i in range(start_index, len(candidates)):
                if candidates[i] > remaining_target:
                    break
                
                if i > start_index and candidates[i] == candidates[i - 1]:
                    continue
                
                current_combination.append(candidates[i])
                
                backtrack(i + 1, current_combination, remaining_target - candidates[i])
                
                current_combination.pop()

        backtrack(0, [], target)
        return results
