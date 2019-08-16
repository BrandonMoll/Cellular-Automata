cur_states = [0] * 400
cur_states[10] = 1
cur_states[30] = 1
cur_states[50] = 1
next_states = [0] * 400

def check_neighbors(current, index):
        alive_neighbors = []
        if index == 0:
            if current[index + 20] == 1:
                alive_neighbors.append(1)

            if current[index + 1] == 1:
                alive_neighbors.append(1)

            if current[index + 21] == 1:
                alive_neighbors.append(1)
        elif index == 19:
            if current[index + 20] == 1:
                alive_neighbors.append(1)

            if current[index - 1] == 1:
                alive_neighbors.append(1)

            if current[index + 19] == 1:
                alive_neighbors.append(1)
        elif index == 380:
            if current[index - 20] == 1:
                alive_neighbors.append(1)

            if current[index + 1] == 1:
                alive_neighbors.append(1)

            if current[index - 19] == 1:
                alive_neighbors.append(1)
        elif index == 399:
            if current[index - 20] == 1:
                alive_neighbors.append(1)

            if current[index - 1] == 1:
                alive_neighbors.append(1)

            if current[index - 21] == 1:
                alive_neighbors.append(1)
        elif index % 20 == 0:
            if current[index - 20] == 1:
                alive_neighbors.append(1)

            if current[index + 20] == 1:
                alive_neighbors.append(1)

            if current[index - 19] == 1:
                alive_neighbors.append(1)

            if current[index + 1] == 1:
                alive_neighbors.append(1)

            if current[index + 21] == 1:
                alive_neighbors.append(1)
        elif (index + 1) % 20 == 0:
            if current[index - 20] == 1:
                alive_neighbors.append(1)

            if current[index + 20] == 1:
                alive_neighbors.append(1)

            if current[index - 21] == 1:
                alive_neighbors.append(1)

            if current[index - 1] == 1:
                alive_neighbors.append(1)

            if current[index + 19] == 1:
                alive_neighbors.append(1)
        elif index - 19 <= 0:
            if current[index - 1] == 1:
                alive_neighbors.append(1)

            if current[index + 1] == 1:
                alive_neighbors.append(1)

            if current[index + 19] == 1:
                alive_neighbors.append(1)

            if current[index + 20] == 1:
                alive_neighbors.append(1)

            if current[index + 21] == 1:
                alive_neighbors.append(1)
        elif index + 19 >= 400:
            if current[index - 1] == 1:
                alive_neighbors.append(1)

            if current[index + 1] == 1:
                alive_neighbors.append(1)

            if current[index - 19] == 1:
                alive_neighbors.append(1)

            if current[index - 20] == 1:
                alive_neighbors.append(1)

            if current[index - 21] == 1:
                alive_neighbors.append(1)
        else:
            if current[index + 1] == 1:
                alive_neighbors.append(1)

            if current[index - 1] == 1:
                alive_neighbors.append(1)

            if current[index + 20] == 1:
                alive_neighbors.append(1)

            if current[index - 20] == 1:
                alive_neighbors.append(1)

            if current[index + 21] == 1:
                alive_neighbors.append(1)

            if current[index - 21] == 1:
                alive_neighbors.append(1)

            if current[index + 19] == 1:
                alive_neighbors.append(1)

            if current[index - 19] == 1:
                alive_neighbors.append(1)

        if current[index] == 0:
            if len(alive_neighbors) >= 3:
                print('Dead cell lives: ', index)
                return 1
            else:
                return 0
        else:
            if len(alive_neighbors) == 2 or len(alive_neighbors) == 3:
                print('alive cell stays alive', index)
                return 1
            elif len(alive_neighbors) >= 4:
                print('alive cell dies', index)
                return 0
            elif len(alive_neighbors) <= 1:
                print('alive cell dies', index)
                return 0
        
for i in range(len(cur_states)):
    next_states[i] = check_neighbors(cur_states, i)
