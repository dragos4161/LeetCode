class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []
        for n1 in nums1:
            if n1 in nums2:
                j = nums2.index(n1) + 1
                maxi = n1
                while j < len(nums2):
                    if nums2[j] > n1:
                        ans.append(nums2[j])
                        maxi = nums2[j]
                        j = len(nums2) + 2
                    j += 1
                if maxi == n1:
                    ans.append(-1)
            else:
                ans.append(-1)
        return ans

s = Solution()
print(s.nextGreaterElement([4,1,2],[1,3,4,2]))