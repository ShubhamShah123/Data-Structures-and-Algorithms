####### LONGEST COMMON SUBSEQUENCE: LCS #######

# LCS : RECURSION
def LCSRecursion(X, Y, lenX, lenY):
    # Base condition
    if lenX == 0 or lenY == 0:
        return 0
    # Choice diagram
    if X[lenX - 1] == Y[lenY - 1]:
        return 1 + LCSRecursion(X, Y, lenX-1, lenY-1)
    else:
        return max(LCSRecursion(X, Y, lenX, lenY-1), \
                   LCSRecursion(X, Y, lenX-1, lenY))

# LCS: Memoization
def LCSMemoization(X, Y, lenX, lenY, T):
    # Base condition
    if lenX == 0 or lenY == 0:
        return 0
    
    if T[lenX][lenY] != -1:
        return T[lenX][lenY]
    
    # Choice diagram
    if X[lenX - 1] == Y[lenY - 1]:
        T[lenX][lenY] = 1 + LCSMemoization(X, Y, lenX-1, lenY-1, T)
    else:
        T[lenX][lenY] = max(LCSMemoization(X, Y, lenX, lenY-1, T), \
                            LCSMemoization(X, Y, lenX-1, lenY, T))
    return T[lenX][lenY]

# LCS: TopDown
def print_matrix(matrix):
    print("### [DP-Table] ###")
    for row in matrix:
        print(row)
    print("-"*len(matrix[0]))

def LCSTopDown(X, Y,flag=None):
    lenX = len(X) if X else 0
    lenY = len(Y) if Y else 0
    t = [[0 if i == 0 or j == 0 else 0 for j in range(lenY+1)] for i in range(lenX+1)]
    if flag:
        print("### INIT ###")
        print_matrix(t)
    for i in range(1, lenX+1):
        for j in range(1, lenY+1):
            if X[i-1] == Y[j-1]: t[i][j] = t[i-1][j-1] + 1
            else: t[i][j] = max(t[i-1][j], t[i][j-1])
    if flag:
        print("### AFTER ###")
        print_matrix(t)
    return t[lenX][lenY]

####### PRINTING THE SUBSTRING #######
def return_lcs_matrix(X, Y):
    lenX = len(X) if X else 0
    lenY = len(Y) if Y else 0
    t = [[0 if i == 0 or j == 0 else 0 for j in range(lenY+1)] for i in range(lenX+1)]
    
    for i in range(1, lenX+1):
        for j in range(1, lenY+1):
            if X[i-1] == Y[j-1]: 
                t[i][j] = t[i-1][j-1] + 1
            else: t[i][j] = max(t[i-1][j], t[i][j-1])
    
    return t, t[lenX][lenY]

def print_lcs(X, Y):
    substring_list = []

    # Get the LCS matrix
    lcs_matrix, lcs_length = return_lcs_matrix(X, Y)
    # lcs.print_matrix(lcs_matrix)

    # Start from the bottom-right corner of the matrix
    i = len(X)
    j = len(Y)

    while i > 0 and j > 0:
        # If the characters match, it is part of the LCS
        if X[i-1] == Y[j-1]:
            substring_list.append(X[i-1])  # Add this character to the result
            i -= 1
            j -= 1
        # If they don't match, move in the direction of the larger value
        elif lcs_matrix[i-1][j] > lcs_matrix[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(substring_list)[::-1]

####### LONGEST COMMON SUBSTRING: LCSS #######
def LCSS(X, Y,flag=None):
    lenX = len(X) if X else 0
    lenY = len(Y) if Y else 0
    t = [[0 if i == 0 or j == 0 else 0 for j in range(lenY+1)] for i in range(lenX+1)]
    if flag:
        print("### INIT ###")
        print_matrix(t)
    for i in range(1, lenX+1):
        for j in range(1, lenY+1):
            if X[i-1] == Y[j-1]: t[i][j] = t[i-1][j-1] + 1
            else: t[i][j] = 0
    if flag:
        print("### AFTER ###")
        print_matrix(t)
    return max(max(row) for row in t)


###### SHORTES COMMON SUPERSEQUENCE #####
def ShortestCommonSuperstring(X, Y):
    lenX = len(X) if X else 0
    lenY = len(Y) if Y else 0
    lcs_matrix, lcs_length = return_lcs_matrix(X, Y)
    return lcs_matrix, lenX + lenY - lcs_length


###### MINUMUM NUMBER OF OPERATIONS #####
### INSERTION AND DELETION ###
def MinimumInsertionDeletion(X, Y):
    lenX = len(X) if X else 0
    lenY = len(Y) if Y else 0
    _, lcs_len = return_lcs_matrix(X, Y)
    
    num_deletion = abs(lenX - lcs_len)
    num_insertion = abs(lenY - lcs_len)

    return num_insertion, num_deletion

###### LONGEST PALINDORMIC SUBSEQUENCE (LPS) #####
def getLPS(stringA):
    return "" if not stringA else print_lcs(stringA, stringA[::-1])

####### LONGEST REPEATING SUBSEQUENCE (LRS) ######
def LongestRepeatingSubsequence(X):
    lenX = len(X) if X else 0
    t = [[0 if i == 0 or j == 0 else 0 for j in range(lenX+1)] for i in range(lenX+1)]
    for i in range(1, lenX+1):
        for j in range(1, lenX+1):
            if X[i-1] == X[j-1] and i != j:
                t[i][j] = t[i-1][j-1] + 1
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    return t, t[lenX][lenX]

########### SEQUENCE PATTERN MATCHING ########
def SequencePatternMatching(stringA, stringB):
    _, lcs_length = return_lcs_matrix(stringA, stringB)
    return True if lcs_length == len(stringA) else False


#####################################
"""
MINIMUM NUMBER OF INSERTION AND DELETION REQUIRED TO MAKE PALINDROME.
"""
def MinInsertionDeletionPalindrom(X):
    lps_string = getLPS(X)
    num_deletions = abs(len(lps_string) - len(X))
    num_insertions = abs(len(lps_string) - len(X))
    return num_insertions, num_deletions
