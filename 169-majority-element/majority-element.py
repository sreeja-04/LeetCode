class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = len(nums)//2 + 1
        maj_count = 0
        maj_ele = nums[0]
        counting_table = {}
        
        for i in nums:
            counting_table[i] = counting_table.get(i, 0) + 1
            if counting_table[i] > maj_count:
                maj_count = counting_table[i]
                maj_ele = i

        return maj_ele
        



            


