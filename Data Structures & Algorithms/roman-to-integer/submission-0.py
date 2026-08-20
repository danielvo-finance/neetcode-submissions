class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 
                        'V': 5,
                        'X': 10, 
                        'L': 50, 
                        'C': 100, 
                        'D': 500, 
                        'M': 1000}
        total = 0

        for n in range(len(s)):

            if n + 1 < len(s) and roman_values[s[n]] < roman_values[s[n+1]]:
                total -= roman_values[s[n]]
            
            else:
                total += roman_values[s[n]]
            
        return total