distance(a, b, 10).
distance(a, c, 15).
distance(a, d, 20).
distance(b, c, 35).
distance(b, d, 25).
distance(c, d, 30).
distance(b, a, 10).
distance(c, a, 15).
distance(d, a, 20).
distance(c, b, 35).
distance(d, b, 25).
distance(d, c, 30).

% Find all permutations of the list of cities
permute([], []).
permute(L, [H|T]) :-
    select(H, L, R),
    permute(R, T).

% Calculate the total distance of a route
total_distance([_], 0).
total_distance([H,N|T], D) :-
    distance(H, N, Dist),
    total_distance([N|T], D1),
    D is D1 + Dist.

% Solving the TSP
tsp(Cities, BestRoute, MinDist) :-
    permute(Cities, BestRoute),
    total_distance(BestRoute, MinDist),
    \+ (permute(Cities, Route),
        total_distance(Route, Dist),
        Dist < MinDist).
