class EggDropping:
    def SolveRecursion(self, e, f):
        if f == 0 or f == 1: return f
        if e == 1: return f
        mn = float('inf')
        for k in range(1, f+1):
            temp = 1 + max(self.SolveRecursion(e-1, k-1), self.SolveRecursion(e, f-k))
            mn = min(mn, temp)
        return mn