import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.k = k
        self.nums = nums
        
        

    def add(self, val: int) -> int:
        self.nums.append(val)
        print(self.nums)
        heap = []
        for item in self.nums:
            heapq.heappush(heap, item)
            if len(heap) > self.k:
                heapq.heappop(heap)
        print("LSIT")
        print(list(heap))
        return list(heap)[0]
            

        
