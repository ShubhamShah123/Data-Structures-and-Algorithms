from collections import Counter

def getAnagramOccurence(string, pattern):
    i, j = 0, 0
    ans = 0
    K = len(pattern)
    mapCtr = Counter(pattern)
    count = len(mapCtr)

    while j < len(string):
        # Perform Calculations
        if string[j] in mapCtr:
            mapCtr[string[j]] -= 1
            if mapCtr[string[j]] == 0:
                count -= 1

        # Less than window size
        if (j - i + 1) < K:
            j += 1
        
        # Hitting the window size
        elif (j - i + 1) == K:
            # Get the ans
            if count == 0:
                ans += 1

            # Sliding the window
            if string[i] in mapCtr:
                if mapCtr[string[i]] == 0:
                    count += 1
                mapCtr[string[i]] += 1
            i += 1
            j += 1
    
    return ans

str = input("Enter the first string: ")
pattern = input("Enter the pattern string: ")

total = getAnagramOccurence(str, pattern)
print(f"Total number of anagram occurrences: {total}")
