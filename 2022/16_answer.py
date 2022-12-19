from common import get_lines

def generate_all_permutations(permutations, valves, current_valve, minutes_remaining, pressure_relieved):
    if minutes_remaining <= 0:
        return permutations

    current_valve_open = valves[current_valve]['is_valve_open']
    available_tunnels = valves[current_valve]['tunnels']
    print("available", available_tunnels)



    


def part_one():
    lines = get_lines('16_input.txt')
    valves = {}
    for x in lines:
        x = x.replace('Valve ', '').replace(' has flow rate=', ',').replace('; tunnels lead to valves ', ',').replace('; tunnel leads to valve ', ',').replace(' ', '').split(',')
        origin = x[0]
        flow_rate = int(x[1])
        tunnels = x[2:]

        valves[origin] = {
            "flow_rate": flow_rate,
            "origin": origin,
            "tunnels": tunnels,
            "values": {},
            "is_valve_open": False
        }

    permutations = {}

    generate_all_permutations(permutations, valves, 'AA', 15, 0)

    

def add_stuff(c, my_list):
    new_arr = []
    if len(my_list) == 0:
        return c
    for x in my_list:
        if x % 2 == 0:
            c = {
                **c,
                [x]: True
            }
        else:
            new_arr.append(x+7)
    return add_stuff(c, new_arr)
    



a = [1,2,3,4]
    
d = {}
obj = add_stuff(d, a)
print(obj)


    

part_one()

# value of being in a tunnel = flow rate * (time-1) + value of best open neighbour