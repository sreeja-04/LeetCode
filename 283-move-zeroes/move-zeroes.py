class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        if n==1 or n==0:
            return nums
        j = 0
        i=0
        # while n>0:
        #     if nums[i] == 0:
        #         nums.remove(nums[i])
        #         nums.append(0)
            
        #     i+=1
        #     n-=1

        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j+=1
        
        for i in range(j, n):
            nums[i] = 0
        
        return nums

                
