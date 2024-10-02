from EggDroppingClass import EggDropping

egg = EggDropping()
e, f = map(int, input("Enter e and f: ").split())
num_ways = egg.SolveRecursion(e, f)
print(f"Number of trials when number of eggs is {e} and number of floors is {f}:{num_ways}")
