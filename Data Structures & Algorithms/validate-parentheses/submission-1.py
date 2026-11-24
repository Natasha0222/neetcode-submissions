class Solution:
    def isValid(self, s: str) -> bool:
        possibilities={")":"(","}":"{","]":"["}
        openers=set(possibilities.values())

        letters=list(s)
        stack=[]
        for c in letters:
            if c in openers:
                stack.append(c)
            elif c in possibilities.keys():
                if len(stack)==0 or stack.pop()!=possibilities[c]:
                    return False
        return not stack
        