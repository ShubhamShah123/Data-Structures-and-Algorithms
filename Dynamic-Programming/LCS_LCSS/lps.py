### LONGEST PALINDROMIC SUBSEQUENCE ###
import lcs_functions as lcs

X = input("Enter the String X: ")
lps_string = lcs.getLPS(X)

print(f"Length of LPS: {len(lps_string)}\nLongest palindromic subsequence: {lps_string}")
