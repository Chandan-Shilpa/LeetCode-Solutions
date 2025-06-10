class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        dictionary = {}
        rem = 0
        for h,w in rectangles:
            val = h/w
            if val not in dictionary:
                dictionary[val] = 0
            dictionary[val] += 1
        for val in dictionary.values():
            rem += (val*(val-1)//2)
        return rem