from StringScrambleClass import StringScramble

ss = StringScramble()
HASHMAP = {}

stringA, stringB = input("Enter string A: "), input("Enter string B: ")

if not stringA or not stringB:
    print(f"Empty strings are not allowed! Try again.")
    exit(0)

if len(stringA) != len(stringB):
    print(f"Strings are of not equal length! Try again.")
    exit(0)

recursionAns = ss.solveRecursion(stringA, stringB)
print(f"Recursion Solution: {recursionAns}")

memoizedAns = ss.solveMemoized(stringA, stringB, HASHMAP)
print(f"Memoized Solution: {memoizedAns}")