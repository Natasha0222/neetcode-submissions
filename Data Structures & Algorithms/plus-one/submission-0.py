class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=len(digits)-1
        for i in range(i,-1,-1):
            if digits[i]!=9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
        digits[0]=1
        digits.append(0)
        return digits



    

        