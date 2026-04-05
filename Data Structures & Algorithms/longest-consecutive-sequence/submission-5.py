class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest, length = 0, 0

        for n in nums:
            if n-1 not in nums_set:
                length = 1
                while (n+length) in nums_set:
                    length += 1
                longest = max(longest, length)
        
        return longest

        # Using sorting nlogn
        # nums.sort()        
        # sub_len =  1
        # res = 1
        # if len(nums) == 0:
        #     return 0
        # for i in range(len(nums)-1):
        #     if nums[i+1] - nums[i] == 0:
        #         continue
        #     if nums[i+1] - nums[i] == 1:
        #         sub_len+=1
        #         res = max(sub_len, res)
        #     else:
        #         sub_len = 1
            
        # return res