import lcs_functions as lcs

X, Y = input("Enter String X: "), input("Enter String Y: ")
isSure = input('Want the dp table? (y/n): ').lower().strip() == 'y'

lcs_output = lcs.LCSTopDown(X, Y, isSure)
print(f"Length of longest common subsequence: {lcs_output}")