from collections import deque
def water_jug(a,b, target):
    def get_all_states(state):
        (x,y) = state
        return [
            (a,y),
            (x,b),
            (0,y),
            (x,0),
            (x - min(x,b-y), x + min(x,b-y)),
            (x - min(y,a-x), x + min(y,a-x))
        ]
    queue = deque([(0,0)])
    visited = set((0,0))

    while queue:
        state = queue.popleft()
        
        if state[0] == target or state[1] == target:
            return True

        for next_state in get_all_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
    return False

res = water_jug(4,3,2)
print(res)
