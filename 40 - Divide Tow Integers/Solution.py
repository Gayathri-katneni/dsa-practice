class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        is_positive = (dividend > 0) == (divisor > 0)
        dvd = abs(dividend)
        dvs = abs(divisor)
        quotient = 0
        while dvd >= dvs:
            temp_dvs = dvs
            multiple = 1

            while dvd >= (temp_dvs << 1):
                temp_dvs <<= 1
                multiple <<= 1
                
            dvd -= temp_dvs
            quotient += multiple
            
        result = quotient if is_positive else -quotient
        return min(max(INT_MIN, result), INT_MAX)

