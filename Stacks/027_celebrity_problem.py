def celebrity_approach1(M, n):
    # print(f"N: {n}\nMatrix:\n{M}")
    # print("[APPROACH 1]\n")
    
    indegree = [0]*n
    outdegree = [0]*n
    # print(f"Indegree Array: {indegree}\nOutdegree Array: {outdegree}")
    for i in range(n):
        for j in range(n):
            if M[i][j] == 1:
                indegree[j] += 1
                outdegree[i] += 1
    
    for i in range(n):
        # print(f"ID: {i} | InDeg: {indegree[i]} | OutDeg: {outdegree[i]}")
        if indegree[i] == n-1 and outdegree[i] == 0:
            return i
    return -1

def celebrity_approach2(M, n):
    # print(f"N: {n}\nMatrix:\n{M}")
    # print("[APPROACH 2]\n")
    c = 0 # Init celebrity
    for i in range(n):
        if M[c][i] == 1:
            c = i
            
    for i in range(n):
        if c != i and (M[c][i] == 1 or M[i][c] == 0):
            return -1
    return c


t = 1
for _ in range(t) :
    n = int(input())
    a = list(map(int,input().strip().split()))
    k = 0
    m = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(a[k])
            k+=1
        m.append(row)

print(f"Approach 1 - Celebrity ID: {celebrity_approach1(m, n)}")
print(f"Approach 2 - Celebrity ID: {celebrity_approach2(m, n)}")