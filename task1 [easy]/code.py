class Solution(object):
    def twoSum(self, nums, target):
        n = len(nums)
        for a in range(0,n):
            for i in range(0,n):
                if a == i:
                    pass
                else:
                    if nums[a]+nums[i] == target:
                        cavab = [a,i]
                        return cavab