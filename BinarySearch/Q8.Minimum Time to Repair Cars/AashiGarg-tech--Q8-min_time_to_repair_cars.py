class Solution(object):
    def repairCars(self, ranks, cars):
        topRank = max(ranks)
        minRank = min(ranks)
        freqRanks = [0] * (topRank + 1)

        for rnk in ranks:
            freqRanks[rnk] += 1
        
        lo = 1
        hi = minRank * cars * cars

        while lo < hi:
            mid = lo + (hi - lo) // 2
            numCars = 0
            for rnk in range(1, len(freqRanks)):
                freq = freqRanks[rnk]
                numCars += freq * int(math.sqrt(mid / rnk))
            if numCars >= cars:
                hi = mid
            elif numCars < cars:
                lo = mid + 1
        
        return lo
