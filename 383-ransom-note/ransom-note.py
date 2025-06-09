class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
         count_ransom = Counter(ransomNote)
         count_magazine = Counter(magazine)
    
         for ch in count_ransom:
             if count_ransom[ch] > count_magazine.get(ch, 0):
                 return False
         return True