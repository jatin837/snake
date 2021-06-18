import os
import json

def add_data(head_pos, food_pos, current_direction, length, next_direction, status):
    DATA_FILE:str = os.path.abspath('./snake.dat.json')
    with open(DATA_FILE, 'r') as f:
        data = json.load(f)
        data["headPos"].append(head_pos)
        data["foodPos"].append(food_pos)
        data["length"].append(length)
        data["current-direction"].append(current_direction)
        data["next-direction"].append(next_direction)
        data["status"].append(status)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent = 1)

