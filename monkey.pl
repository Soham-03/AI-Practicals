% Main function to start solving with an initial state
solve(InitialState, Moves) :-
    find_solution(InitialState, [], Moves).

% Base case: If the monkey is on the box (goal state), no further moves are needed.
find_solution(state(_, _, true), _, []).

% Recursive case: Find a valid move that leads to a new state, ensuring its not visited already
find_solution(CurrentState, Visited, [Move | Moves]) :-
    valid_move(CurrentState, Move, NewState),
    \+ memberchk(NewState, Visited),
    find_solution(NewState, [NewState | Visited], Moves).

% Rules for valid moves and resulting states
valid_move(state(Monkey, Box, false), move(Monkey, NewPosition), state(NewPosition, Box, false)) :-
    move(Monkey, NewPosition).

valid_move(state(Monkey, Box, false), push(Box, NewPosition), state(NewPosition, NewPosition, false)) :-
    push(Box, NewPosition),
    Monkey = Box.

valid_move(state(Position, Position, false), climb, state(Position, Position, true)).

% Move actions that are valid (defined as simple facts)
move(at_door, at_window).
move(at_window, at_centre).

% Push actions where the box can be pushed from one position to another
push(at_window, at_centre).
