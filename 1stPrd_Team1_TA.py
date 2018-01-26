import random

####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = '1stPrd_1'
strategy_name = 'Late Game'
strategy_description = 'Until my score becomes more than my opponents then it will do a random choice between C and B, once that happens then it will always do betray.'
    
def move(my_history, their_history, my_score, their_score):
    if my_score < their_score :
        print random.choice(['b','c'])
    elif their_score < my_score :
        print 'b'
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    #This example player always betrays.      
    #return 'c'
