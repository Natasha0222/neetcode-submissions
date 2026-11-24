class Solution:
    def isValid(self, s: str) -> bool:
        possibilities={")":"(","}":"{","]":"["}
        openers=set(possibilities.values())
        stack=[]
        letters=list(s)
        for c in letters:
            if c in openers:
                stack.append(c)
            elif c in possibilities.keys():
                if not stack or stack.pop()!=possibilities[c]:
                    return False
        return not stack
        