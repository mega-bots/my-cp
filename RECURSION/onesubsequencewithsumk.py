#program to print only one subsequence whose sum is k
lis = input("enter the sequence ").split()
size = len(lis)
val = int(input("enter k value "))
def subseqone(ind,arr,summ):
    if (ind>=size):
        if (summ==val):
            print("".join(arr))
            return True
        return False
    arr.append(lis[ind])
    summ+=int(lis[ind])
    if subseqone(ind+1,arr,summ) == True:
        return True
    summ-=int(lis[ind])
    arr.pop()
    if subseqone(ind+1,arr,summ) == True:
        return True
    return False
subseqone(0,[],0)
