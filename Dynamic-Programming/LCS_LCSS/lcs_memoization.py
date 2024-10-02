import lcs_functions as lcs

X, Y = input("Enter String X: "), input("Enter String Y: ")

T = [[-1 for _ in range(len(Y) + 1)] for _ in range(len(X) + 1)]
lcs_output = lcs.LCSMemoization(X, Y, len(X), len(Y), T)
print(f"Length of longest common subsequence: {lcs_output}")