import time 
from tqdm import tqbm 

for i in range(100): 
    time.sleep(2)
for i in tqbm(range(10)): 
    time.sleep(2)
    
