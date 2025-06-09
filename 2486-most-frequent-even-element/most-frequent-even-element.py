class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
      freq = {}
      max_freq = 0
      answer = -1

      for num in nums:
        if num % 2 == 0: 
            freq[num] = freq.get(num, 0) + 1 

           
            if freq[num] > max_freq or (freq[num] == max_freq and num < answer):
                max_freq = freq[num]
                answer = num

      return answer