def word_reversing(word:str): 
    return  " ".join([word.swapcase() for word in reversed(word.split)])

if __name__ == '__method__': 
    print(word_reversing('minhaz'))
    