def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0]*2*len(nums)
        j = 0
        for i in range(len(ans)):
            if i<len(nums):
                ans[i] = nums[i]
            else:
                ans[i] = nums[j]
                j = j + 1
        return ans
