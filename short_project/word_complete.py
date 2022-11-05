# complete word : 
print('hi ,  this is a  completing word game : complete the ap_ _ e word ')
e= str(input('guess first chracter of this word  : '))
l = str(input('guess next chracter of this word  : '))
po=  0 # point 
a='ap', e ,l , 'e'
if e== 'p' and l== 'l' :
    po+=1 
    print('win ', po)
elif e== 'p' or l== 'l' :
    
    print('not far from win , try another time : ')
else : 
    print('you lose : ')
    
