import colorama 
from colorama import Fore 

a=str(input('enter your Text : '))
b=  str(input('enter your response  c for copy ,  x  for cut: and p  for paste  '))
if b== 'copy ' or b== 'c': 
    c= str(input('enter p or paste to paste  '))
    
    if c== 'p' or c=='paste': 
        d= a 
        print(Fore.GREEN, 'real text ',  a)
        print(Fore.CYAN , 'copied  text ' , d  )
    else: 
        print('invalid input: ')
        
    
elif b== 'x' or b=='cut': 
    print(Fore.BLACK, 'text cuted ')
    cx= str(input('enter p or paste to paste  '))
    
    
    if cx== 'p' or cx=='paste': 
        ed= a 
        print(Fore.GREEN, 'real text ',  a)
        print(Fore.CYAN , 'copied  text ' , ed  )
    else: 
        print('invalid input: ')
        
    
else : 
    print(Fore.RED, 'Invalid Input  ')