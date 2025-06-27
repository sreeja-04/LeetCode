class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if not nums:
            return
        
        mxp = mnp = res = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                mxp, mnp = mnp, mxp
                
            mxp = max(nums[i], nums[i] * mxp)
            mnp = min(nums[i], nums[i] * mnp)

            res = max(mxp, res)
        
        return res

