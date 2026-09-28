class Solution:
    def climbStairs(self, n: int) -> int:
        current, previous = 1, 1
        for _ in range(1,n):
            temp = current
            current += previous
            previous = temp

        return current
        