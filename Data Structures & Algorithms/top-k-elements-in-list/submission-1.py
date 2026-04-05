class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}

        for i in nums:
            dict1[i] = dict1.get(i,0) + 1
        
        dict1 = dict(sorted(dict1.items(),key=lambda x: x[1], reverse=True))

        mk = 0
        lst = []

        for key, value in dict1.items():
            if mk < k:
                lst.append(key)
            mk += 1
        return lst
