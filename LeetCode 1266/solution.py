class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        p = points
        return sum(max(abs(p[i][0] - p[i - 1][0]), abs(p[i][1] - p[i - 1][1])) for i in range(1, len(p)))