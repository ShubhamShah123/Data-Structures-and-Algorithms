import lcs_functions as lcs

X = input("Enter the input string:")
lrs_matrix, lrs_length = lcs.LongestRepeatingSubsequence(X)

lcs.print_matrix(lrs_matrix)
print(f"Length of longest repeqting subsequence: {lrs_length}")
