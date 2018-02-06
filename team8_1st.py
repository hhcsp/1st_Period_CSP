def move(my_history, their_history, my_score, their_score):
    
    if len(their_score)== +0:
        return 'c'
    else:
        return 'b'

    if len(their_history)== +0:
        return 'bb'
    else:
        return 'c'
        
    if len(my_score)== -0:
        return 'b'
    else: 
        return 'b'