class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
      ratio_count = defaultdict(int)
      count = 0

      for width, height in rectangles:
        g = gcd(width, height)
        ratio = (width // g, height // g)
        count += ratio_count[ratio]
        ratio_count[ratio] += 1

      return count