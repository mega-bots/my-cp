class Graph:
     def __init__(self,x,y):
          self.x = x
          self.y = y
     def correct_order(self,x):
       a,b = x
       c1,d1 = [],[]
       for i in b.copy():
          val = b.index(max(b))
          c1.append(a.pop(val))
          d1.append(b.pop(val))
       c2 = c1.copy()
       d2 = d1.copy()
       for i in d1:
          z = []
          if d2.count(i) > 1:
             for k in range(d1.count(i)):
                z.append(c2.pop(d2.index(i)))
                d2.pop(d2.index(i))
          c1 = c1[:d1.index(i)]+sorted(z)+c1[d1.index(i)+len(z):] 
     

       x = [c1,d1]          
       return x

     def draw(self,lis=[[],[]]):
          #print('your list: ',lis)
          print('\n')
          x,y = self.correct_order(lis)
          #print('ordered list: ',[x,y])
          for i in range(self.y,-self.y,-1):
            if i != 1:######
              try:
                if i == y[0]:
                  #print(i)
                  lis2 = [x[j] for j,k in enumerate(y) if k == i]
                  neg_x = 0
                  neg_ref_x = self.x
                  pos_x = 0
                  pos_ref_x = 0
                  for z in lis2:
                    if z < 0:
                      #print(lis2)
                      #print(neg_ref_x,z)
                      print(' '*(neg_ref_x-abs(z)-1)+'  '*(neg_ref_x-abs(z))+'*',end='')
                      neg_x += 1
                      neg_ref_x = abs(z)
                      if neg_x == len([i for i in lis2 if i<0]):
                          print(' '*(neg_ref_x-1)+'  '*(neg_ref_x)+'|',end='')#####
                          try:
                           if (y[0] != y[1]) or len(y)-neg_x == 0:####################### 
                              print()
                          except:
                               print()
                          for i in range(neg_x):
                               x.pop(0)
                               y.pop(0)
                          #print(neg_ref_x,z)
                    else:
                      if neg_x == 0:
                           print('  '*self.x+' '*(self.x-1)+'|',end = '')####
                           neg_x += 1
                      print(' '*(z-pos_ref_x-1)+'  '*(z-pos_ref_x)+'*',end='')
                      pos_x += 1
                      pos_ref_x = z
                      if len([i for i in lis2 if i>=0]) == pos_x:
                         print()                         
                         for i in range(pos_x):
                              x.pop(0)
                              y.pop(0)
                             
                else:
                 2/0
              except:
                print('  '*self.x+' '*(self.x-1)+'|')
            elif i == 1:
              print('_',end='')
              for op in range(self.x,-self.x,-1):
                if op != 0:
                 if op == 1:
                    if len(y) > 0:
                      if y[0] == 1 and x[0] == 0:
                        print('_|*',end = '_')
                      else:
                       print('_|',end = '_')
                    else:
                      print('_|',end = '_')
                 else:
                   addon=0 
                   if len(y) > 0:
                     if x[0] < 0:
                        addon += 1     
                     if y[0] == 1 and op == -x[0]+addon:
                       print('_*_',end = '')
                       y.pop(0)
                       x.pop(0)
                     else:
                       print('_ _',end = '')
                   else:
                      print('_ _',end = '')
              print('_')
     
a = Graph(5,5)
a.draw([[-4,-3,-2,-1,1,2,3,4],[-4,-3,-2,-1,1,2,3,4]])
print()
a.draw([[2,1,3,-4],[3,-1,0,-2]])
print()
print()
a.draw([[3,2,1,3,2,1,-3,-2,-1,-3,-2,-1],[1,3,4,-1,-3,-4,1,3,4,-1,-3,-4]])
a.draw([[2],[3]])
x = []
y=[]
b = Graph(15,15)
for i in range(10):
     pass

'''
correct_order FUNCTION CHANGES LIST SO THAT AS THE CODE PRINTS FROM TOP AND FROM LEFT TO RIGHT 
IN A LINE ,IT MAKES COORDINATES ACCORDINGLY 
([-3,4,6,2],[3,5,3,2])→→↓
([4,-3,6,2],[5,3,3,2])←←

    
DRAW FUNCTION DRAWS IT(I CREATED ON PC AND PASTED HERE)REPORT ANY BUGS IN COMMENT,UPVOTE IF YOU LIKE
(THANKS,YOU ARE STILL WITH ME)
'''
