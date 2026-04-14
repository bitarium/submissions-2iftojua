class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for i in range(len(nums)):
            length = 1
            if (nums[i]-1) not in numSet:
                length = 1
                while nums[i]+length in numSet:
                    length +=1
                res = max(res, length)
        return res