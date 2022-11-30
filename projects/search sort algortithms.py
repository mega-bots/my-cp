def linear_search(arr,x):
    steps = 1
    for i in arr:
        if (i==x):
            print(f"{x} found at index {arr.index(i)}\n")
            break
        steps+=1
    print("total steps = {}\n\n".format(steps))
def binary_search(a,x):
    '''It is only for sorted array'''
    left = 0
    right = len(a)-1
    steps = 1
    while(left<=right):
        mid = (left+right)//2
        if (a[mid]==x):
            print(f"{x} found at index {mid}\n")
            break
        elif(a[mid]<x):
            left = mid+1
        elif (a[mid]>x):
            right = mid-1
        steps+=1
    print("total steps = {}".format(steps))
def bubble_sort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]
    print("sorted array",a)

a = [5,2,7,3,6,8]
#linear_search(a,4)
#binary_search(a,4)
#bubble_sort(a)







