class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
             if(n==2)or(n==3)or(n==1):
               return n
             elif(n>3):
                 return self.climbStairs(n-1)+self.climbStairs(n-2)