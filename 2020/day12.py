def part_1(instructions):
    current_heading = 90
    current_position = { 0: 0, 90: 0, 180: 0, 270: 0 }

    for instruction in instructions:
        action = instruction[0]
        magnitude = instruction[1]

        if action == 'F':
            current_position[current_heading] += magnitude
        elif action == 'L':
            current_heading = (current_heading - magnitude) % 360
        elif action == 'R':
            current_heading = (current_heading + magnitude) % 360
        elif action == 'N':
            current_position[0] += magnitude
        elif action == 'E':
            current_position[90] += magnitude
        elif action == 'S':
            current_position[180] += magnitude
        elif action == 'W':
            current_position[270] += magnitude

    east_west = abs(current_position[90] - current_position[270])
    north_south = abs(current_position[0] - current_position[180])
    print(f"Manhattan distance from start position: {east_west + north_south}")

def part_2(instructions):
    ship_psn = { 0: 0, 90: 0, 180: 0, 270: 0 }

    # relative to ship
    waypoint_psn = { 0: 1, 90: 10, 180: 0, 270: 0 }

    for instruction in instructions:
        action = instruction[0]
        magnitude = instruction[1]

        if action == 'F':
            ship_psn[0] += magnitude * waypoint_psn[0]
            ship_psn[90] += magnitude * waypoint_psn[90]
            ship_psn[180] += magnitude * waypoint_psn[180]
            ship_psn[270] += magnitude * waypoint_psn[270]
        elif action == 'L':
            new_waypoint_psn = {}
            for (heading, psn) in waypoint_psn.items():
                new_waypoint_psn[(heading - magnitude) % 360] = waypoint_psn[heading]

            waypoint_psn = new_waypoint_psn
        elif action == 'R':
            new_waypoint_psn = {}
            for (heading, psn) in waypoint_psn.items():
                new_waypoint_psn[(heading + magnitude) % 360] = waypoint_psn[heading]

            waypoint_psn = new_waypoint_psn
        elif action == 'N':
            waypoint_psn[0] += magnitude
        elif action == 'E':
            waypoint_psn[90] += magnitude
        elif action == 'S':
            waypoint_psn[180] += magnitude
        elif action == 'W':
            waypoint_psn[270] += magnitude

    east_west = abs(ship_psn[90] - ship_psn[270])
    north_south = abs(ship_psn[0] - ship_psn[180])
    print(f"Manhattan distance from start position: {east_west + north_south}")

if __name__ == '__main__':
    f = open('input_day12')

    instructions = []

    for line in f:
        line = line.strip()
        action = line[0]
        magnitude = int(line[1:])
        instructions.append((action, magnitude))

    part_1(instructions)
    part_2(instructions)

    f.close()
