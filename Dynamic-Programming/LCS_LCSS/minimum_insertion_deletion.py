import lcs_functions as lcs

X, Y  = input("Enter String X: "), input("Enter String Y: ")

from_string = "EMPTY STRING" if not X else X
to_string = "EMPTY STRING" if not Y else Y

insertion_len, deletion_len = lcs.MinimumInsertionDeletion(X, Y)

print(f"\nFrom {from_string} to {to_string}")
print(f"\nMinimum inserts: {insertion_len}\nMinimum deletes: {deletion_len}")