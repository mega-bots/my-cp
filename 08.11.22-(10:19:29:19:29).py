#printing in reverse
def pprint(num):
    if num>0:
      pprint(num-1)
      print(num)
pprint(10)
