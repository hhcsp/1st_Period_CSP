#########################################################
#
#  James Wong & Rohan Storachi
#  Team 4
#  1st Period
#
#########################################################

team_name = 'team4_1st'
strategy_name = 'Collude but retaliate'
strategy_description = '''\
Collude first round. Collude, except in a round after getting 
a severe punishment.'''
my_history = '0'
their_history = '0'
my_score = 0
their_score = 0
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; collude.
        return 'b'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b' # Betray if they were severely punished last time,
    else:
        return 'c' # otherwise collude.