class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        t=ord(target)
        for ley in letters:
            if ord(ley)>t:
                return ley
        return letters[0]
        
