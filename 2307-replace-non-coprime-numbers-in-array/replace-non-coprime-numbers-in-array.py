class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def is_coprime(a, b):
            return True if gcd(a, b) == 1 else False
        
        def lcm(a, b):
            return abs(a*b) // gcd(a, b)

        n = len(nums)
        i=0
        
        stack = []

        while nums:
                x = nums.pop(0)
                stack.append(x)
                while len(stack) > 1 and not is_coprime(stack[-1], stack[-2]):
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(lcm(a, b))

        return stack





        return nums


