#frog jump with k steps
def tot_jumps(ind,k):
    if ind<=1:
        return ind
    c=0
    for i in range(1,k+1):
        c+=tot_jumps(ind-i,k)*(ind-i>0)
    return c
n,k = map(int,input("enter the number of stairs,jump value k: ").split())
print(tot_jumps(n,k))
