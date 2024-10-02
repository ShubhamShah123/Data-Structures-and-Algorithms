from ExpressionEvaluationClass import ExpressionEvaluation
exprEval = ExpressionEvaluation()

stringA = input("Enter the input string: ")
dp = [[[-1 for _ in range(2)] for _ in range(205)] for _ in range(205)]

i = 0
j = len(stringA) - 1

num_ways = exprEval.RecursionSolve(stringA, i, j, True)
print(f"[Recursion]Number of ways to be True: {num_ways}")

num_ways = exprEval.MemoizationSolve(stringA, i, j, True, dp)
print(f"[Memoization]Number of ways to be True: {num_ways}")