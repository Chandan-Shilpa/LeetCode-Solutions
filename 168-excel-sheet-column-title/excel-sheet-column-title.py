class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
       result = []
       while columnNumber > 0:
        columnNumber -= 1  # Shift for 1-indexed to 0-indexed
        result.append(chr(ord('A') + columnNumber % 26))
        columnNumber //= 26
       return ''.join(reversed(result))