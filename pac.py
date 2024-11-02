global agent_pos  
global env  
global perception_history  
global dim  

perception_history = []  

file = open('input.txt', 'r')  
lines = file.readlines()  

dim = [int(i) for i in lines[0].split(',')]  
del lines[0]  
agent_pos = [int(i) for i in lines[0].split(',')]  
del lines[0]; del lines[0]  

env = []  
for line in lines:  
    env.append(list(filter(('\n').__ne__, line.strip())))  



def environment(action, pos):  
    new_pos = pos[:] 

    match action:  
        case 'UP':   
            new_pos[0] -= 1  
        case 'RIGHT':  
            new_pos[1] += 1  
        case 'DOWN':  
            new_pos[0] += 1  
        case 'LEFT':   
            new_pos[1] -= 1  
        case _:  
            raise ValueError("Invalid action")  

    if 0 <= new_pos[0] < dim[0] and 0 <= new_pos[1] < dim[1]:  
        return [new_pos[0], new_pos[1], env[new_pos[0]][new_pos[1]]]  
    return None  



def pos_to_str(node):  
    return str(node[0]) + str(node[1])  



def recursive_dfs(pos, path, directions, limit, move_count):  
    percept = [pos[0], pos[1], env[pos[0]][pos[1]]]  
    perception_history.append(percept)  

    if env[pos[0]][pos[1]] == 'f':  
        return path + [pos_to_str(pos)], directions, move_count  

    if len(path) >= limit:  
        return None, directions, move_count   

    visited.add(pos_to_str(pos))

    action = agent(percept)  
    if action:  
        next_pos = environment(action, pos[:])  
        move_count += 1  
        if next_pos and next_pos[-1] != '*' and pos_to_str(next_pos) not in visited:  
            new_directions = directions + [f"[{pos[0]},{pos[1]}]--{action}-->"]  
            result, new_directions, move_count = recursive_dfs(next_pos, path + [pos_to_str(pos)], new_directions, limit, move_count)  
            if result:  
                return result, new_directions, move_count  

    for action in ['UP', 'RIGHT', 'DOWN', 'LEFT']:  
        next_pos = environment(action, pos[:])  
        move_count += 1   
        attempted_directions = directions + [f"[{pos[0]},{pos[1]}]--{action}-->"]  
        if next_pos and next_pos[-1] != '*' and pos_to_str(next_pos) not in visited:  
            new_path, attempted_directions, move_count = recursive_dfs(next_pos, path + [pos_to_str(pos)], attempted_directions, limit, move_count)  
            if new_path:  
                return new_path, attempted_directions, move_count  

    visited.remove(pos_to_str(pos)) 
    return None, directions, move_count  


def agent(percept):  
    actions = ['RIGHT', 'DOWN', 'UP', 'LEFT']  
    for action in actions:  
        next_pos = environment(action, percept[:2])  
        if next_pos and next_pos[-1] != '*':  
            return action  
    return None  


def ids(max_depth=20):  
    for limit in range(max_depth):  
        global visited  
        visited = set()   
        result, directions, move_count = recursive_dfs(agent_pos[:], [], [], limit, 0)  

        if result:  
            return result, directions, move_count   

    return None, [], 0  



if env[agent_pos[0]][agent_pos[1]] == '*': print('Agent is not in a valid position.')
else:
    result = ids(max_depth=20)  

    if result[0]: 
        print(f"Number of Moves: {result[2]}")  
        x, y = result[0][-1]
        path = "".join(result[1]) + f"[{x},{y}]" 
        print(f"Moves Steps:\n{path}")   
    else:  
        print("No path found.")