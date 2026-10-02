from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # Find the position of '#'
            j = i
            while s[j] != "#":
                j += 1
            
            # Get the length
            length = int(s[i:j])
            
            # Extract the word
            word = s[j+1 : j+1+length]
            res.append(word)
            
            # Move pointer
            i = j + 1 + length
        
        return res