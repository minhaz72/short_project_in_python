# DIctonary : 
# we are going to  create a simple and short dict : 
class Dict : 
    def num(): 
        a=  {
            "one" : 1 , 
            "two" : 2 , 
            "three" : 3 , 
            "four" : 4 , 
            "five" : 5 , 
            "Six" : 6,
            'seven': 7 ,
            "eight" : 8 , 
            "Nine" : 9 , 
            "ten" : 10 , 
             
                        
            
        }
    def word(): 
        a= {
            'bird' : 'pakhi ', 
            'cat' : 'bilai' , 
            'bat' :  'bat ', 
            'bol': 'boll ', 
            'apple': 'apple', 
            'elephent' : 'hati' ,
            'small' :'choto', 
            'big': 'boro', 
            'tiny' : 'khddra', 
            'huge' : 'bishal', 
            'cow' :  'goru', 
            'hat' : 'tupi', 
            'goat' : 'chagol' , 
            'parot': 'tiya', 
            'forward': 'age', 
            'before' : 'age', 
            'after': 'pore'
             
            
        }
        
c= Dict()
b= input('which  section dp  you  want to go : num , word ')
if b==  'word': 
    cx= str(input('enter your word : '))
    v=c.word()
    print(v[cx])

else:
    cs= str(input('enter a number name : '))
    
