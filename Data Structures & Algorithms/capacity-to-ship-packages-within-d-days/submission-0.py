class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r

        def can_ship(cap):
            ships, capacity = 1, cap
            for w in weights:
                if capacity - w < 0:
                    ships += 1
                    capacity = cap
                capacity -= w
            return ships <= days

        while l <= r:
            m = l + (r - l) // 2
            if can_ship(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res

