import lcs_functions as lcs

X, Y = input("Enter String X: "), input("Enter String Y: ")
SUBSTRING = lcs.print_lcs(X, Y)

print(f"LCS Length: {len(SUBSTRING)}\nLCS Substring: {SUBSTRING}")
