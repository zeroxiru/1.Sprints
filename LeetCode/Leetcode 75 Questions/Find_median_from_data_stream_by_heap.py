import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialze the data structure here.
        """
        # two heaps, small = maxheap and large = minheap
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:

        heapq.heappush(self.small, -1 * num)
        # make sure every num small is <= every num in large
        if (self.small and self.large and
                (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)

        if len(self.large) > len(self.small) +1:
            val = heapq.heappop(self.large)
            heapq.heappush((self.small, -1 * val))


    def find_median(self) -> float:
        if len (self.small) > len(self.large):
            return  self.small[0]
        if len(self.large) > len(self.small):
            return  self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2

if __name__ == "__main__":
    md_order = MedianFinder()
    md_order.add_num(2)
    md_order.add_num(7)
    md_order.add_num(4)
    md_order.add_num(12)
    md_order.add_num(1)
    md_order.add_num(4)
    print(md_order.find_median())
