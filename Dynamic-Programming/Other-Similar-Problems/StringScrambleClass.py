class StringScramble:
    def getSubString(self, string: str, pos: int, length: int) -> str:
        return string[pos:pos+length]
    
    def solveRecursion(self, stringA: str, stringB: str) -> bool:
        # Base conditions
        if stringA == stringB: return True        
        if len(stringA) <= 1: return False
        
        N = len(stringA)
        flag = False
        
        for i in range(1, N):
            # Case 1: No swap
            cond1 = self.solveRecursion(self.getSubString(stringA, 0, i), self.getSubString(stringB, 0, i)) and \
               self.solveRecursion(self.getSubString(stringA, i, N-i), self.getSubString(stringB, i, N-i))
            
            # Case 2: Swap the partitions
            cond2 = self.solveRecursion(self.getSubString(stringA, 0, i), self.getSubString(stringB, N-i, i)) and \
               self.solveRecursion(self.getSubString(stringA, i, N-i), self.getSubString(stringB, 0, N-i))
            
            if cond1 or cond2:
                flag = True
                break            
        return flag

    def solveMemoized(self, stringA: str, stringB: str, HASHMAP: dict) -> bool:
        # Base conditions
        if stringA == stringB: return True        
        if len(stringA) <= 1: return False
        hash_key = stringA + "_" + stringB
        if hash_key in HASHMAP.keys(): return HASHMAP[hash_key]
        N = len(stringA)
        flag = False
        
        for i in range(1, N):
            # Case 1: No swap
            cond1 = self.solveMemoized(self.getSubString(stringA, 0, i), self.getSubString(stringB, 0, i), HASHMAP) and \
               self.solveMemoized(self.getSubString(stringA, i, N-i), self.getSubString(stringB, i, N-i), HASHMAP)
            
            # Case 2: Swap the partitions
            cond2 = self.solveMemoized(self.getSubString(stringA, 0, i), self.getSubString(stringB, N-i, i), HASHMAP) and \
               self.solveMemoized(self.getSubString(stringA, i, N-i), self.getSubString(stringB, 0, N-i), HASHMAP)
            
            if cond1 or cond2:
                flag = True
                break    
        HASHMAP[hash_key] = flag
        return flag
