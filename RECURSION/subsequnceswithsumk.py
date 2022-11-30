#program to print subsequences whose sum is k
lis = input("enter a sequence ").split()
size = len(lis)
val = int(input("enter the k value "))
def subseq(ind,arr,summ):
    if (ind>=size):
        if (summ==val):
            print("".join(arr))
        return
    arr.append(lis[ind])
    subseq(ind+1,arr,summ+int(lis[ind]))
    arr.pop()
    subseq(ind+1,arr,summ)
subseq(0,[],0)
