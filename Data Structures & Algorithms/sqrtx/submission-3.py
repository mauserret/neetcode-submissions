class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        l, r = 1, x
        while l <= r:
            mid = l + (r - l) // 2
            mid_squared = mid * mid
            if mid_squared == x:
                return mid
            elif mid_squared > x:
                r = mid - 1
            else:
                l = mid + 1
        return r
        