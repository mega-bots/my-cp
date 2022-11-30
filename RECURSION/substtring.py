a = input()
sub=input()
for i,j in enumerate(a):
    if sub==a[i:i+len(sub)]:
        print("at index",i)
        break
