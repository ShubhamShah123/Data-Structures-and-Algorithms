import lcs_functions as lcs

X, Y = input("Enter String X: "), input("Enter String Y: ")

_, scs_length = lcs.ShortestCommonSuperstring(X, Y)
print(f"Length of shortest common supersequence: ", scs_length)