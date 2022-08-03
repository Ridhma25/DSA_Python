def removeDuplicates(self, nums: List[int]) -> int:
        l = []
        for i in range(len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
        
        nums.clear()
        
        for j in l:
            nums.append(j)
        
        return len(nums)
   
