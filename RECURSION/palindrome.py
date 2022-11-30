#program to check if a string is a palindrome or not
inp = input()
size = len(inp)
def check(string,l):
    if (l>= size//2):
        return True
    return check(string,l+1) if (string[l]==string[size-l-1]) else False

if check(inp,0):
    print("palindrome")
else:
    print("not a palindrome")
