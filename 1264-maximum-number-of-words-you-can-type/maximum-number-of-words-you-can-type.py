class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        def sol(letters, word):
            for i in letters:
                if i in word:
                    return True
            return False

        arr = text.split(" ")
        letters  = list(brokenLetters)
        count = len(arr)
        for i in arr:
            if sol(letters, i):
                count -=1
            
                    
        
        return count