
from heapq import *

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(s[i] != 0 and s[i] != goal[i] for i in range(9))

def solve(start):
    q = [(h(start), 0, start, [])]
    seen = set()

    while q:
        _, cost, s, path = heappop(q)

        if s == goal:
            return path + [s]

        if s in seen:
            continue
        seen.add(s)

        i = s.index(0)
        for j in range(9):
            if abs(i//3-j//3) + abs(i%3-j%3) == 1:
                t = list(s)
                t[i], t[j] = t[j], t[i]
                t = tuple(t)
                if t not in seen:
                    heappush(q, (cost+1+h(t), cost+1, t, path+[s]))
    return None

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
ans = solve(start)

if ans:
    for s in ans:
        print(s[:3], s[3:6], s[6:])
else:
    print("No solution")
