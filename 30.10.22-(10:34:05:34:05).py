#program to print minimum cost to reach top
def solve(ind,cost):
    if ind<=1:
        return 0
    return min(cost[ind-1]+solve(ind-1,cost),cost[ind-2]+solve(ind-2,cost))

print(min(cost[-1]+solve(n-1,cost),cost[-2]+solve(n-2,cost)))
