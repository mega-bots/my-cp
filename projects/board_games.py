import os,random,itertools
class Square:
  def __init__(self,size):
    self.r = []  #STORES ROW
    self.c = []  #STRORES COLUMN
    self.d = []  #STORES DIAGONAL
    self.sqr = {} #StoresValueforBoxes
    self.main = [-1] #STORES
                     #MAX_LengthOfVal
    self.l=[i for i in range(1,size**2+1)] #JustReference
    self.represent =[[],[]] #Represent
    self.size = size #SizeOfSquare
    self.mk_clear=1 #RefForBoxLength
    self.sqr_control = [' '*(self.mk_clear) for i in range(self.size**2)] #IntializeValFor
                     #Box(spaced str)
    #Here linking val for box names
    #str1,str2... are box names
    for i in range(1,self.size**2+1):
      self.sqr[f'str{i}'] = self.sqr_control[i-1]
  def row(self):
    '''
  GENERATE ROWS FOR SQUARE IN TERMS 
  OF NUMBERS(UseRowMethodToUnderstand)
    '''
    self.r = []
    R=[]
    for i in range(1,self.size**2+1):
      R.append(i)
      if i%self.size == 0:
        self.r.append(R)
        R=[]
    return self.r
  def diagonal(self):
    '''
    GENERATE DIAGONALS FOR SQUARE IN
    TERMS OF NUMBERS USING ROWS
    '''
    d1=[]
    d2=[]
    for i,j in enumerate(self.r):
      d1.append(j[i])
      d2.append(j[-i-1])
    self.d = [d1]+[d2]
    return self.d
  def column(self):
    '''
    GENERATE COLUMNS FOR SQUARE IN
    TERMS OF NUMBERS USING ROWS
    '''
    count = 0
    while True:
      C=[]
      if count == len(self.r):
        break
      for i in self.r:
        C.append(i[count])
      self.c.append(C)
      count += 1
    return self.c
  def make_square(self):
    '''
    MAKES SQUARE OF ANY SIZE ,AND IS    
    CONTROLABLE(BECAUSE THE SPACES FOR 
    THESE BOXES ARE THE SPACES VALUES 
    WE INITIATED AND LINKED TO BOX 
    NAMES(DICTIONARY WITH KEY VALUES) 
    AND HERE I AM USING THOSE BOX
    NAMES TO REPRESENT SPACED STRING.
    *IT WILL ALSO REPRESENT IF NEEDED
    *X,Y VALUES
    '''
    line_break = True
    zz1=self.represent[0][:self.size].copy()
    if zz1 !=[]:
      zz1_mx = len(max(zz1,key=len))
    else:
      zz1_mx = 0
      zz1.append('')
    for i in range(1,self.size**2+1):
      if zz1 == []:
        zz1.append('')
      if (i-1)%self.size == 0:
        print((' '*zz1_mx+'|'+('`')*(self.mk_clear+2)+'|')+('|'+('`')*(self.mk_clear+2)+'|')*(self.size-1))
      if (i-1)%self.size != self.size-1:
        space=''
        if line_break == True:
          space = ' '*(zz1_mx-len(zz1[0]))
        print((zz1[0]+space+'|'+' '+self.sqr[f'str{i}']+' '+'|'),end='')
        if line_break == True and zz1_mx != 0:
          zz1.pop(0)
          zz1.insert(0,'')
          line_break = False
      else:
          print(('|'+' '+self.sqr[f'str{i}']+' '+'|'))
          if zz1_mx !=0:
            zz1.pop(0)
          line_break = True
    
    print(' '*(zz1_mx+1),end='')
    print(('`'*(self.mk_clear+2)+'  ')*self.size)
    print(' '*(zz1_mx+1),end='')
    print(' '*(-(-self.mk_clear//2)),end='')
    print(*self.represent[1],sep = ' '*(self.mk_clear+3))
    print('\n')
  def renew(self,full = False):
    '''
    CLEARS WHOLE SQUARE,YOU HAVE 
    OPTIONAL FULL PARAMETER WHICH WILL 
    MAKE THE SQUARE TO INTIAL SQUARE 
    IF YOU HAVEN'T MENTIONED IT JUST 
    CLEARS THE SQUARE AND SPACES CAN 
    BE OF ANY LENGTH AS YOU MIGHT 
    CONTROL THE SQUARE  BEFORE
    RENEWING AND ITS SPACE LENGTHS ARE 
    CHANGED
    '''
    self.mk_clear =1
    sqr_control = [' '*self.mk_clear for i in range(self.size**2)]
    for i in range(1,self.size**2+1):
      self.sqr[f'str{i}'] = sqr_control[i-1]
    if full == 'O':
      self.cstate(1)
  def control(self,val,block,full=False):
####    os.system('clear')
    '''
    BASICALLY CONTROLS THE SQUARE
    *SINCE VALUES CAN BE OF DIFFERENT 
    LENGTH KEEPING THE MAXIMUM LENGTH 
    FOR EVERY VALUE WITH CENTER METHOD
    '''
    
    if val == 'all':
         val = self.l[:len(block)]
    self.mk_clear=len(max(block,key=len))
    
    if type(val) == list:
     self.main.append(self.mk_clear)
     if not full:
       self.mk_clear = max(self.main)
     else:
       self.mk_clear = 1
       self.main = [-1,1] #print(self.mk_clear)@@@@@@@@@@@@@@@@
     for i in val:
       if i>self.size**2:
        print(f'The value {i} is not available in this square of size {self.size}*{self.size} you have initiated try bigger squares\n')
        return
     for i in range(1,self.size**2+1):
       if i in val:
        j = val.index(i)
        self.sqr[f'str{i}'] = block[j].center(self.mk_clear) 
       else:
         self.sqr[f'str{i}']=self.sqr[f'str{i}'].center(self.mk_clear)
     return self.make_square()
    else:
      val = [val]
      block=[block]
      self.control(val,block)
  def show(self):
    '''
    SHOWS THE SQUARE WITH ALL BLOCKS 
    FILLED IN WITH NUMBERS
    '''
    self.control([i for i in range(1,self.size**2+1)],[str(i) for i in range(1,self.size**2+1)])
    self.renew()
  def cstate(self,full = False):
       '''
       REPRESENTS CURRENT STATE OF    
       SQUARE
       '''
       self.control([i for i in range(1,len(self.sqr)+1)],[self.sqr[i] for i in self.sqr],full)
       
       
       
'''
Instead of using control method and using numbers to access and changing values..you can access them via your keys.
sqr dictionary will contain the box names with values,you can make a dictionary with your own keys and places the sqr dictionary keys as values for your dictionary,so you can control the boxes individually with your own keys(use cstate to get the current state)(SEE THE CHESS BOARD CLASS BELOW) 
'''







print()
print('TIC TAC TOE RANDOM GAME')

d=Square(3)
import random
lis = [1,2,3,4,5,6,7,8,9]
x_choices = []
o_choices = []
comb = d.row()+d.column()+d.diagonal()
for i in range(1,10):
  choice = random.choice(lis)
  lis.remove(choice)
  if i%2 == 0:
    z = 'X'
    x_choices.append(choice)
    check_choice = x_choices
  else:
    z = 'O'
    o_choices.append(choice)
    check_choice = o_choices
  d.control(choice,z)
  if i > 4:
   try:
    checker = itertools.permutations(check_choice,3)
    for i in checker:
         if sorted(list(i)) in comb:
            2/0
   except ZeroDivisionError:
    print(z,'won\n')
    break

a = Square(3)

print('\nA full representation')
a.show()

print('rows- ',a.row())
print('columns- ',a.column())
print('diagonals- ',a.diagonal())
print('Initial state using cstate method')
a.cstate() #current state of board
print("using represent attribute to represent [['1','23','4'],[]]")
a.represent=[['1','23','4'],[]]
a.cstate()
print("changing represent  attribute to [['7','2','9'],['a','d','c']]")
a.represent=[['7','2','9'],['a','d','c']]
print("using cstate() method to show after changing represent attribute")
a.cstate()
print("using control method a.control(1,'3')")
a.control(1,'3')
print("using control method a.control(5,'abd')")
a.control(5,'abd')
print("changing represent attribute to [['*']*3,['@']*2]")
a.represent =[['*']*3,['@']*2]
print('and using control method')
a.control(9,'hlo')
print('using control method')
a.control([1,3,8],list('gpu'))
a.renew() #making board clear
print('using control method after renewing the board a.renew()')
a.control(2,'h')
print('using control method')
a.control('all',list('hello'))



b = Square(4)
print('rows- ',b.row())
print('columns- ',b.column())
print('diagonals- ',b.diagonal())
b.show()
b.cstate() #current state of board
b.control([1,3,8],list('gpu'))
b.control(9,'hii')
b.renew('O') #making board clear(full)
b.control(2,'a')
print("Trying to use b.control(100,'dino') in a square size of 4*4 \n")
b.control(100,'dino')
b.control(1000,'h')
b.control(999,'hello')

c=Square(6)
c.control('all',list('abcdefghijklmnopqrstuvwxyz'))
c.control(40,'p')






'''
#BETTER ON PC @@@@@@@@@@@@@@@@@@@@@@@@@@


class Chess_board(Square):
     
     def __init__(self):
      
       super().__init__(8)
       self.represent = [list('87654321'),list('abcdefgh')]
       self.row()
     def start(self):
       lis1 = itertools.cycle(list('abcdefgh'))
       self.d1={}
       for i in range(1,self.size**2+1):
         self.d1[f'{next(lis1)    }{(self.size-(i-1)//self.size)}'] = f'str{i}'
      # print(self.d1)
       self.control('all',('brook1 bknight1 bbishop1 bqueen bking bbishop2 bknight2 brook2 ' +' '.join([f'bpawn{i}' for i in range(1,9)])).split())
       self.control(self.l[48:],(' '.join([f'wpawn{i}' for i in range(1,9)])+' wrook1 wknight1 wbishop1 wqueen Wking wbishop2 wknight2 wrook2').split())
      # print(self.sqr)
      # print(self.rep_c)
    
     def Piece_value(self,Piece):
          for i,j in enumerate(self.sqr.values(),1):
            if j.strip() == Piece:
              val = i
              break
         # print(val)
          for i,j in enumerate(self.r):
               if val in j:
                  return [val,i,j.index(val)]

       
     def move(self,piece,To):
          z = self.Piece_value(piece)
          #print(self.r[z[1]-by][z[2]])
          #print(self.sqr[f'str{z[0]}'][1:])
          self.sqr[self.d1[To]] = self.sqr[f'str{z[0]}']
          self.sqr[f'str{z[0]}'] = ' '
          #print(self.sqr)
          self.cstate()
         
a = Chess_board()
a.start()
a.move('wpawn6','f4')
a.move('bpawn7','g5')
a.move('wpawn5','e4')
a.move('bpawn6','f5')
a.move('wqueen','h5')
'''



