class ExpressionEvaluation:
    def RecursionSolve(self, stringA: str, i: int, j: int, isTrue: bool):
        # Base condition
        if i > j: return 0
        if i == j:
            if isTrue == True:
                return stringA[i] == 'T'
            else:
                return stringA[i] == 'F'
        # Temp ans
        ans = 0
        for k in range(i+1, j, 2):
            leftTrue = self.RecursionSolve(stringA, i, k-1, True)
            leftFalse = self.RecursionSolve(stringA, i, k-1, False)
            rightTrue = self.RecursionSolve(stringA, k+1, j, True)
            rightFalse = self.RecursionSolve(stringA, k+1, j, False)
            # calculating final ans
            """
            & Truth table
            T & T -> T
            T & F -> F
            F & T -> F
            F & F -> F

            ^ Truth Table
            T ^ T -> F
            T ^ F -> T
            F ^ T -> T
            F ^ F -> F

            | Truth Table
            T | T -> T
            T | F -> T
            F | T -> T
            F | F -> F

            """
            if stringA[k] == '&':
                if isTrue:
                    ans += leftTrue*rightTrue
                else:
                    ans += leftTrue*rightFalse + leftFalse*rightTrue + leftFalse*rightFalse
            
            elif stringA[k] == '|':
                if isTrue:
                    ans += leftTrue*rightTrue + leftTrue*rightFalse + leftFalse*rightTrue
                else:
                    ans += leftFalse*rightFalse
            
            elif stringA[k] == '^':
                if isTrue:
                    ans += leftTrue*rightFalse + leftFalse*rightTrue
                else:
                    ans += leftTrue*rightTrue + leftFalse*rightFalse
        return ans
    
    def MemoizationSolve(self, stringA: str, i: int, j: int, isTrue: bool, dp: list):
        if i>j: return 0
        if dp[i][j][isTrue] != -1: return dp[i][j][isTrue]
        if i==j:
            if isTrue:
                return stringA[i] == 'T'
            else:
                return stringA[i] == 'F'
            
        ans = 0
        for k in range(i+1, j, 2):
            if dp[i][k-1][1] == -1:
                dp[i][k-1][1] = self.MemoizationSolve(stringA, i, k-1, True, dp)
            if dp[i][k-1][0] == -1:
                dp[i][k-1][0] = self.MemoizationSolve(stringA, i, k-1, False, dp)
            if dp[k+1][j][1] == -1:
                dp[k+1][j][1] = self.MemoizationSolve(stringA, k+1, j, True, dp)
            if dp[k+1][j][0] == -1:
                dp[k+1][j][0] = self.MemoizationSolve(stringA, k+1, j, False, dp)
            # calculating final ans
           
            if stringA[k] == '&':
                if isTrue:
                    ans += dp[i][k-1][1]*dp[k+1][j][1]
                else:
                    ans += dp[i][k-1][1]*dp[k+1][j][0] + dp[i][k-1][0]*dp[k+1][j][1] + dp[i][k-1][0]*dp[k+1][j][0]
            
            elif stringA[k] == '|':
                if isTrue:
                    ans += dp[i][k-1][1]*dp[k+1][j][1] + dp[i][k-1][1]*dp[k+1][j][0] + dp[i][k-1][0]*dp[k+1][j][1]
                else:
                    ans += dp[i][k-1][0]*dp[k+1][j][0]
            
            elif stringA[k] == '^':
                if isTrue:
                    ans += dp[i][k-1][1]*dp[k+1][j][0] + dp[i][k-1][0]*dp[k+1][j][1]
                else:
                    ans += dp[i][k-1][1]*dp[k+1][j][1] + dp[i][k-1][0]*dp[k+1][j][0]
        return ans

