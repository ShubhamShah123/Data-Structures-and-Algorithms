############# PALINDROM PARTITIONING #############
class PalindromePartition:
    def isPalindrome(self, stringA,i ,j):
        return stringA[i:j+1] == stringA[i:j+1][::-1]
    
    def RecursionPartition(self, stringA, i, j):
        # print(f"Input string: {stringA} | (i, j): {i, j}")
        # Base Condition
        MIN_NUM = float('inf')
        if i >= j: return 0
        if self.isPalindrome(stringA, i, j): return 0
        for k in range(i, j):
            temp_ans = self.RecursionPartition(stringA, i, k) + \
                        self.RecursionPartition(stringA, k+1, j) + 1
            MIN_NUM = min(temp_ans, MIN_NUM)
        return MIN_NUM
    
    def MemoizedPartitions(self, stringA, i, j, t, flag=None):
        MIN_NUM = float('inf')
        if i >= j or self.isPalindrome(stringA, i, j): return 0
        if t[i][j] != -1: return t[i][j]
        for k in range(i, j):
            temp_ans = self.MemoizedPartitions(stringA, i, k, t) + \
                        self.MemoizedPartitions(stringA, k+1, j, t) + 1
            MIN_NUM = min(temp_ans, MIN_NUM)
        t[i][j] = MIN_NUM
        # Return Final ans
        if flag:
            return t, MIN_NUM
        else:
            return MIN_NUM
    
    def makePartitions(self, stringA, i, j, curr_partitions, all_partitions):
        if i > j: 
            all_partitions.append(curr_partitions.copy())
            return
        
        for k in range(i, j+1):
            if self.isPalindrome(stringA, i, k):
                curr_partitions.append(stringA[i:k+1])
                self.makePartitions(stringA, k + 1, j, curr_partitions, all_partitions)
                curr_partitions.pop()


    def getPartitions(self, stringA):
        curr_partitions = []
        all_partitions = []
        self.makePartitions(stringA, 0, len(stringA)-1, curr_partitions, all_partitions)
        return all_partitions