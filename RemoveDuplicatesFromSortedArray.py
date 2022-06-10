class Solution(object):
    def removeDuplicates(self, nums):
        seen = {}
        a = set(nums)

        while len(nums) > len(a):
            i = 0
            while i < len(nums):
                l = len(nums)
                if nums[i] in seen:
                    idx = nums.index(nums[i])
                    nums[idx:] = nums[-(l - idx - 1):]
                    seen.clear()
                    i = len(nums) + 1
                else:
                    seen[nums[i]] = 1
                    i += 1
        return len(nums)
        """
        :type nums: List[int]
        :rtype: int
        """
s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])