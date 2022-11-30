length = [1,2,3,4,5,6,7,8]
price = [1,5,8,9,10,17,17,20]
size = len(length)
def solve(length_arr,price_arr,cost,rod_length,hashmap):
    if rod_length==0:
        return cost
    if rod_length<0:
        return 0
    maxx = -float('inf')
    if rod_length in hashmap:
        return hashmap[rod_length]
    for i in range(len(length_arr)):
        if length[i]>rod_length:
            break
        maxx = max(maxx,solve(length_arr,price_arr,cost+price_arr[i],rod_length-length_arr[i],hashmap))
    if rod_length not in hashmap:
        hashmap[rod_length] = maxx
    return maxx
print(solve(length,price,0,int(input()),{}))

