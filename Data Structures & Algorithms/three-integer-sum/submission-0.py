class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            lst = nums.copy()
            lst.pop(i)
            target = (-nums[i])

            l , r = 0, len(lst) - 1
            while l < r:
                if lst[l] + lst[r] < target:
                    l+=1
                elif lst[l] + lst[r] > target:
                    r -=1
                elif lst[l] + lst[r] == target:
                    output = [-target, lst[l], lst[r]]
                    output.sort()
                    if output not in res:
                        res.append(output)
                    l+=1
                    r-=1
        return res
