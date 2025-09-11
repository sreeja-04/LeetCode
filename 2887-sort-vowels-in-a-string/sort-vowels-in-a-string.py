class Solution:
    def sortVowels(self, s: str) -> str:
        newstr = ""
        A, E, I, O, U = 65, 69, 73, 79, 85
        a, e, i, o, u = 97, 101, 105, 111, 117

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        arr = []
        for i in range(len(s)):
            if s[i] in vowels:
                arr.append(s[i])
    
        arr.sort()
        count = 0
        for i in range(len(s)):
            if s[i] not in vowels:
                newstr += s[i]
            else:
                newstr += arr[count]
                count += 1

        return newstr
                

