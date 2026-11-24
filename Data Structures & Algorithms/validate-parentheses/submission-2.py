class Solution:
    def isValid(self, s: str) -> bool:
        possibilities={")":"(","}":"{","]":"["}
        openers=set(possibilities.values())
        stack=[]

        for c in s:
            if c in openers:
                stack.append(c)
            elif c in possibilities.keys():
                if not stack or stack.pop()!=possibilities[c]:
                    return False
        return not stack
        