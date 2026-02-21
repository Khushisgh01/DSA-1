import heapq

class MedianFinder:

    def __init__(self):
        # max heap (store negatives)
        self.small = []
        # min heap
        self.large = []

    def addNum(self, num: int) -> None:
        # Step 1: push to max heap
        heapq.heappush(self.small, -num)

        # Step 2: balance - move largest from small to large
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Step 3: maintain size property
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0
