### LONGEST PALINDROMIC SUBSEQUENCE ###
import lcs_functions as lcs

X = input("Enter the String X: ")

insertions, deletions = lcs.MinInsertionDeletionPalindrom(X)
print(f"# of insertions: {insertions}\n# of deletions: {deletions}")