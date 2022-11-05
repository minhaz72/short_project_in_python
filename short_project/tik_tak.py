# tik tok toe : 
import random
from re import L 
f= random.randint(0,1)
print('hey this is tik tak toe game : ')
e= int(input('enter your move  in 0 and 1 '))
a=  [ 
     [e, 1 , f ], 
     [1,f, e],
     [e, 1,  f]
     ]
if e==f :
    print('win ')
else:
    print('lost;')
print(a)