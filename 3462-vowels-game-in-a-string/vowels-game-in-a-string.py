class Solution:
    def doesAliceWin(self, s: str) -> bool:
        n = len(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        c = 0
        for i in s:
            if i in vowels:
                c+=1

        if c==0:
            return False

        # odd vowels
        if c%2!=0:
            return True

        # even vowels
        if c%2==0: 
            return True
        # remstr = ""
        # # newstr = ""
        # lvc = 0
        # for i in range(n):
        #     if s[i] in vowels:
        #         lvc += 1
        #         if lvc == c:
        #             remstr = s[i:]
        #             break
        #     # newstr += i

        # if remstr
                


            


