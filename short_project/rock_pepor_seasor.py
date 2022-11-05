 #rock pepor seasor : 
import random 
def rock_pepor_seasor(p1, p2 ) : 
    if p1 == p2 : 
        return 'tie'
    elif p1 == 'rock ' and p2 == 'seasor': 
        return p1 + 'win '
    
    elif p1 ==  'seasor' and p2 ==  'rock':
            return p2 + 'win '
    elif p1==  'rock'  and p2==  'peper ': 
            return p1 + 'win '
    elif p1==  'peper'  and p2==  'rock': 
            return p2 + 'win '
    elif p1 ==  'seasor' and p2 ==  'peper' : 
            return p1 + 'win '
    elif p1== 'peper' and p2== 'seasor': 
            return p2 + 'win '
    else:
        print('invalid input  : ')


p1=  str(input('enter a move betwenn rock , pepor and seasor '))
a= ['rock ', 'pepor', 'seasor']
p2= random.choice(a)
print(rock_pepor_seasor(p1, p2))

     
        
