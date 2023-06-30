'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    pass


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
#def tic_tac_toe(board):
    a = len(board)
    x='X'
    o='O'
    count=0
    b=False
    
    for i in range(0,a):
        if board[i].count(x)==a:
            b=True
            print(x)
            break
        elif board[i].count(o)==a:
            b=True
            print(o)
            break
        else:
            continue
    
        
    for j in range (0,a):
        if (x in board[j][j])==True:
            count+=1
        elif (o in board[j][j])==True:
            count-=1
        else:
            continue
        
        if count==a:
            b=True
            print(x)
            break
        elif abs(count)==a:
            b=True
            print(o)
            break
        else:
            continue
    
    for d in range (0,a):
        count=0
        for e in range (0,a):
            if (x in board[e][d])==True:
                count+=1
            elif (o in board[e][d])==True:
                count-=1
            else:
                continue
        if count==a:
            b=True
            print (x)
            break
        elif abs(count)==a:
            b=True
            print(o)
            break
        else:
            continue
        
    if b==False:
        print('NO WINNER')

                        
                        
                        
                        


board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
['X','X','O',''],
['O','X','O','O'],
['X','','','O'],
['O','X','','']
]


tic_tac_toe(board1)

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
#def eta(first_stop, second_stop, route_map):
    route_map=[]
    num=len(legs)
    mins=0
    
    for x in range (0,num):
        y=list(legs.keys())[x][0]
        route_map.append(y)
    
    a=route_map.index(first_stop)
    b=route_map.index(second_stop)
    
    print(a)
    print(b)
    
    
    while b!=a and a<num:
        if a<b:
            mins=mins+legs[(route_map[a],route_map[a+1])]['travel_time_mins']
            a=a+1
        elif a>b:
            while a+1!=num:
                mins=mins+legs[(route_map[a],route_map[a+1])]['travel_time_mins']
                a=a+1
            else:
                mins=mins+legs[(route_map[a],route_map[0])]['travel_time_mins']
                a=0
        else:
            mins=0  
    else:
        print(mins)

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
}}

eta('a1','b1',route_map)