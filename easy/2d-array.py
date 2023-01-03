n = 6
m = []
for i in range(n):
    m.append(list(map(int, input().split()[:n])))
print("mmmmmmmmmmmmmmm",m)
    
def sum_glass(m, i, j):
    """Assumes hour-glass is in bounds of m!"""
    print("11111111111111111111")
    print("1st part",m[i][j:j+3])
    print("2222222222222222")
    print("2nd part",m[i+1][j+1])
    print("3333333333333333333")
    print("3rd part",m[i+2][j:j+3])
    return sum(m[i][j:j+3]) + m[i+1][j+1] + sum(m[i+2][j:j+3])

best = float("-inf")
for i in range(4):
    for j in range(4):
        s = sum_glass(m, i, j)
        if s > best:
            best = s
            
print (best)
