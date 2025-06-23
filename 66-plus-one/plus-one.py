class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        d = "".join(map(str, digits))
        # for i in digits:
        #     i = i * 10
            
        a = int(d) + 1
        arr = []
        while a>0:
            rem = a%10
            arr.append(rem)
            a = a//10

        return arr[::-1]
        
            

