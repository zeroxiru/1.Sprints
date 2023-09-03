import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize the data structure here.
        """
        # Two heaps: small as a max-heap and large as a min-heap
        self.small = []
        self.large = []

    def add_num(self, num: int) -> None:
        # Push the negated number to small, effectively creating a max-heap
        heapq.heappush(self.small, -1 * num)  # Push negated number

        # Make sure every number in small is <= every number in large
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)  # Pop negated number
            heapq.heappush(self.large, val)  # Push negated number

        # If the size difference between small and large is more than 1, balance them
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)  # Pop negated number
            heapq.heappush(self.large, val)  # Push negated number

        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * val)  # Push negated number

        # Print the state of the heaps after adding the number
        print("After adding {}: ".format(num))
        print("small:", [-x for x in self.small])  # Display in positive form
        print("large:", self.large)  # No need to negate here

    def find_median(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]  # Return negated number
        if len(self.large) > len(self.small):
            return self.large[0]

        return (-1 * self.small[0] + self.large[0]) / 2


if __name__ == "__main__":
    md_order = MedianFinder()
    md_order.add_num(2)
    md_order.add_num(3)
    md_order.add_num(4)
    md_order.add_num(12)
    # md_order.add_num(1)
    # md_order.add_num(4)
    #
    # print("After adding 2:")
    # print("small:", [-2])
    # print("large:", [])
    #
    # print("After adding 7:")
    # print("small:", [-2])
    # print("large:", [7])
    #
    # print("After adding 4:")
    # print("small:", [-4, -2])
    # print("large:", [7])
    #
    # print("After adding 12:")
    # print("small:", [-4, -2])
    # print("large:", [7, 12])
    #
    # print("After adding 1:")
    # print("small:", [-4, -2, -1])
    # print("large:", [7, 12])
    #
    # print("After adding 4:")
    # print("small:", [-4, -2, -1])
    # print("large:", [4, 7, 12])

    print("Median:", md_order.find_median())
