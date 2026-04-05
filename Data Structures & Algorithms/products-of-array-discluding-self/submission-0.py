class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pfx, sfx = [1], [1]
        
        for i in range(1,len(nums)):
            pfx.append(nums[i-1]*pfx[i-1])

        for i in range(len(nums)-2, -1, -1):
            sfx.insert(0, nums[i+1]*sfx[0])
        
        res = []
        for i in range(len(nums)):
            res.append(pfx[i] * sfx[i])
        
        return res