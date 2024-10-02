import cProfile
import lcs_functions as lcs

def find_scs(X, Y):
    print("[Find SCS]")
    scs_matrix, scs_length = lcs.ShortestCommonSuperstring(X, Y)
    lcs.print_matrix(scs_matrix)

    superstring_list = []  # Use a list to accumulate characters
    i, j = len(X), len(Y)

    # Traceback from the bottom-right of the matrix
    while i > 0 and j > 0:
        # If characters match, it's part of the LCS
        if X[i-1] == Y[j-1]:
            superstring_list.append(X[i-1])
            i -= 1
            j -= 1
        # If they don't match, move towards the direction of the larger value
        elif scs_matrix[i-1][j] > scs_matrix[i][j-1]:
            superstring_list.append(X[i-1])
            i -= 1
        else:
            superstring_list.append(Y[j-1])
            j -= 1

    # Add remaining characters from X or Y
    while i > 0:
        superstring_list.append(X[i-1])
        i -= 1

    while j > 0:
        superstring_list.append(Y[j-1])
        j -= 1

    # The superstring is built in reverse, so reverse it at the end
    SUPERSTRING = ''.join(reversed(superstring_list))
    
    print(f"Length of shortest common supersequence: {scs_length}")
    print(f"Shortest Common Superstring: {SUPERSTRING}")

def main():
    print("[Main Function]")
    X, Y = "acbcf", "abcdaf"
    find_scs(X, Y)

# Profiling the main function
if __name__ == '__main__':
    cProfile.run('main()')

# X, Y = input("Enter String X: "), input("Enter String Y: ")

# scs_matrix, scs_length = lcs.ShortestCommonSuperstring(X, Y)

# lcs.print_matrix(scs_matrix)

# superstring_list = []


# i = len(X)
# j = len(Y)

# while i > 0 and j > 0:
#     # If the characters match, it is part of the LCS
#     if X[i-1] == Y[j-1]:
#         superstring_list.append(X[i-1])  # Add this character to the result
#         i -= 1
#         j -= 1
#     # If they don't match, move in the direction of the larger value
#     elif scs_matrix[i-1][j] > scs_matrix[i][j]:
#         superstring_list.append(X[i-1])
#         i -= 1
#     elif scs_matrix[i][j-1] > scs_matrix[i][j]:
#         superstring_list.append(Y[j-1])
#         j -= 1

# while i > 0:
#     superstring_list.append(X[i-1])
#     i -= 1

# while j > 0:
#     superstring_list.append(Y[j-1])
#     j -= 1
# # The SUBSTRING is built backwards, so reverse it
# SUPERSTRING = ''.join(reversed(superstring_list))
# print(f"Length of shortest common supersequence: {scs_length}\nShortest Common Superstring: {SUPERSTRING}")