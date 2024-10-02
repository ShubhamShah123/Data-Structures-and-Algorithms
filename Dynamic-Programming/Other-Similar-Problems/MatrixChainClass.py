############# MATRIX CHAIN MULTIPLICATION #############
class MatrixChain:
    def RecursionSolve(self,array, i, j):
        """
        Recursion method to solve the matrix chain multiplication
        """
        # Base Condition
        if i >= j : return 0 
        min_num = 99999
        # Calculating the temp ans
        for k in range(i, j):
            temp_ans = self.RecursionSolve(array, i, k) + \
                        self.RecursionSolve(array, k+1, j) + \
                        array[i-1] * array[k] * array[j]
            if temp_ans < min_num:
                min_num = temp_ans
        
        # Return Final ans
        return min_num
    
    def print_matrix(self, matrix):
        """
        Prints the matrix or the table.
        """
        print("### [Table] ###")
        for row in matrix:
            print(row)
        print("-"*len(matrix[0]))

    def MemoizedSolve(self,array, i, j, t, flag=None):
        """
        Memoization method to solve the matrix chain multiplication
        """
        if i >= j : return 0 
        if t[i][j] != -1: return t[i][j]
        min_num = 99999
        # Calculating the temp ans
        for k in range(i, j):
            temp_ans = self.MemoizedSolve(array, i, k, t) + \
                        self.MemoizedSolve(array, k+1, j, t) + \
                        array[i-1] * array[k] * array[j]
            if temp_ans < min_num:
                min_num = temp_ans
        
        t[i][j] = min_num            
        # Return Final ans
        if flag:
            return t, min_num
        else:
            return min_num
        
