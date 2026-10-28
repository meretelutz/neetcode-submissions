class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        buckets = []
        for num, cnt in count.items():
            buckets.append([cnt, num])
        buckets.sort()

        result = []
        while k>0:
            result.append(buckets.pop()[1])
            k -= 1
        
        return result












        # buckets = []
        # for num, cnt in count.items():
        #     buckets.append([cnt, num])
        # buckets.sort()
        
        # result = []
        # while k > 0:
        #     result.append(buckets.pop()[1])
        #     k-=1
        # return result