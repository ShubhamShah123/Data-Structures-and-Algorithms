import lcs_functions as lcs

stringA, stringB = input("Enter string A: "), input("Enter string B: ")

spm_output = lcs.SequencePatternMatching(stringA, stringB)
print(f"Sequency Pattern Matching: {spm_output}")