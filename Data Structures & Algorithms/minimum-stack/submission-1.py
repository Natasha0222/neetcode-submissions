class MinStack:

    def __init__(self):
        self.all=[]
        self.min=[]
        
    def push(self, val: int) -> None:
        if not self.min:
            self.min.append(val)
        elif val<= self.min[-1]:
            self.min.append(val)
        self.all.append(val)

    def pop(self) -> None:
        if self.all[-1]==self.min[-1]:
            self.min.pop()
        self.all.pop()

    def top(self) -> int:
        return self.all[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
        
