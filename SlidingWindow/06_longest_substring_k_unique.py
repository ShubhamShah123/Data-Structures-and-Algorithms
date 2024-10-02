def LongestSubstringWithK(array, size, K):
    i, j = 0, 0
    ans = 0
    CHARMAP = {}  # contains the character and its count
    
    while j < size:
        # Do the calculations
        if array[j] in CHARMAP:
            CHARMAP[array[j]] += 1
        else:
            CHARMAP[array[j]] = 1
        
        # Condition < K
        if len(CHARMAP) < K:
            j += 1
        # Condition = K
        elif len(CHARMAP) == K:
            ans = max(ans, j - i + 1)
            j += 1
        # Condition > K
        elif len(CHARMAP) > K:
            while len(CHARMAP) > K:
                CHARMAP[array[i]] -= 1
                if CHARMAP[array[i]] == 0:
                    del CHARMAP[array[i]]
                i += 1
            j += 1
    
    # print("CHARACTER MAP: \n", CHARMAP)
    return ans

# N = int(input("Enter the number of elements: "))
input_string = input("Enter the string: ")
K = int(input("Enter the value of K: "))

output = LongestSubstringWithK(input_string, len(input_string), K)
print(f"Length of longest substring with {K} unique characters: {output}")
