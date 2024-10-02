import lcs_functions as lcs

X, Y = input("Enter String X: "), input("Enter String Y: ")

lcs_output = lcs.LCSRecursion(X, Y, len(X), len(Y))
print(f"Length of longest common subsequence: {lcs_output}")