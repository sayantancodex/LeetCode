class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        newtarget = ord(target)
        a= []
        for i in range(len(letters)):
            a.insert(i, ord(letters[i]))
        for j in range(len(letters)):
            if a[j] > newtarget:
                return letters[j]
            
            

        if target == 'z':
            return letters[0]

        elif newtarget > a[len(a)-1]:
            return letters[0]

        elif newtarget == a[len(a)-1]:
            return letters[0]    
