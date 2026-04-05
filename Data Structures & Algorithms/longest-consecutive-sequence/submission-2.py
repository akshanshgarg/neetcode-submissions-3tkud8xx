class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()        
        sub_len =  1
        res = 1
        if len(nums) == 0:
            return 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 0:
                continue
            if nums[i+1] - nums[i] == 1:
                sub_len+=1
                res = max(sub_len, res)
            else:
                sub_len = 1
            # print("res:", res)
            # print("sub_len:", sub_len)
        return res