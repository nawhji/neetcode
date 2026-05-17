class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        import heapq
        from collections import defaultdict

        heap = []
        freq = defaultdict(int)

        for n in nums:
            freq[n] += 1

        for n in freq:
            heapq.heappush(heap, (-freq[n], n))

        output = []
        for i in range(k):
            output.append(heapq.heappop(heap)[1])

        return output