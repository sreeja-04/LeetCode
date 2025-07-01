class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        def make_digit(arr):
            temp = 0
            for i in arr:
                temp = temp * 10 + i
            return temp

        def even_subsequence(digits):
            if not digits:
                return 0

            digits.sort()
            count = 0
            used = [False] * len(digits)
            unique = set()

            def helper(curr, idx):
                nonlocal count

                if len(curr) == 3:
                    if curr[0] == 0:
                        return
                    num = make_digit(curr)
                    if num % 2 == 0 and num not in unique:
                        unique.add(num)
                        count += 1
                    return

                if idx == len(digits):
                    return

                if not used[idx]:
                    if idx == 0 or digits[idx] != digits[idx - 1] or used[idx - 1]:
                        used[idx] = True
                        curr.append(digits[idx])
                        helper(curr, 0)  
                        curr.pop()
                        used[idx] = False

                helper(curr, idx + 1)

            helper([], 0)
            return count

        return even_subsequence(digits)