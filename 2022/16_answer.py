from common import get_lines

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
            "values": {}
        }

    for valve in valves:
        pass

    


    

part_one()

# value of being in a tunnel = flow rate * (time-1) + value of best open neighbour