class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        current_str = "1"
        
        for _ in range(n - 1):
            next_parts = []
            i = 0
            
            while i < len(current_str):
                j = i
                while j < len(current_str) and current_str[j] == current_str[i]:
                    j += 1
                
                count = j - i
                digit = current_str[i]
                
                next_parts.append(str(count))
                next_parts.append(digit)
                
                i = j
                
            current_str = "".join(next_parts)
            
        return current_str
