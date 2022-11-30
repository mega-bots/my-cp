#program to find range sums,maximums,minimums
"""
Editorial-Apna college

UPDATE OPERATION - O(logN)
QUERY  OPERATION - O(logN)

"""
N = 10**5
tree = [0]*4*N
def build(node,start,end,a):
    if (start==end):
        tree[node]=a[start]
        return
    mid = (start+end)//2
    build(2*node,start,mid,a)
    build(2*node+1,mid+1,end,a)
    #tree[node]=tree[2*node]+tree[2*node+1]
    tree[node] = max(tree[2*node],tree[2*node+1])
    #tree[node] = min(tree[2*node],tree[2*node+1])

def query(node,start,end,l,r):
    if (end<l or start>r):
        #return 0              #=> sum query
        return -float('inf')   #=> max query
        #return float('inf')   #=> min query
    if (l<=start and end<=r):
        return tree[node]
    mid = (start+end)//2
    left = query(2*node,start,mid,l,r)
    right = query(2*node+1,mid+1,end,l,r)
    #return left+right
    return max(left,right)
    #return min(left,right)
def update(node,start,end,idx,val,a):
    if (start==end):
        a[idx]=val
        tree[node]=val
        return 
    mid = (start+end)//2
    if (idx<=mid):
        update(2*node,start,mid,idx,val,a)
    else:
        update(2*node+1,mid+1,end,idx,val,a)
    #tree[node]=tree[2*node]+tree[2*node+1]
    tree[node] = max(tree[2*node],tree[2*node+1])
    #tree[node] = min(tree,[2*node],tree[2*node+1])


"""
=========================================================================================================
"""

arr = [1,2,3,4,5,6,7,8]
build(1,0,len(arr)-1,arr)
print("INITIAL ARRAY: ",arr)
#print("INITIAL SUM = ",sum(arr))
print("INITIAL MAX = ",max(arr))
#print("INITIAL MIN = ",min(arr))
while(1):
    choice = int(input("enter 1:update 2:query "))
    if (choice==1):
        idx,val = map(int,input("enter index and value to be updated: ").split())
        print("Initial array :",arr)
        update(1,0,len(arr)-1,idx,val,arr)
        print("updated array :",arr)
    elif(choice == 2):
        start,end = map(int,input("enter the range start,end to query ").split())
        #print(f"sum in {start}...{end} = ",query(1,0,len(arr)-1,start,end))
        print(f"max in {start}...{end} = ",query(1,0,len(arr)-1,start,end))
        #print(f"min in {start}...{end} = ",query(1,0,len(arr)-1,start,end))
    else:
        print("\nTHANK YOU FOR LEARNING SEGMENT TREES PRABHAS")
        print("\n\n"+"*"*33+'-'*10+"HAPPY CODING"+"-"*10+"*"*33)
        break
