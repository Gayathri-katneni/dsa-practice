class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        phone_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, path):
            # If the path length equals digits length, we have a complete combination
            if index == len(digits):
                result.append(path)
                return
            
            # Get the letters corresponding to the current digit
            current_digit = digits[index]
            for letter in phone_map[current_digit]:
                backtrack(index + 1, path + letter)
        
        backtrack(0, "")
        return result
