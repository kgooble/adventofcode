import random

def collect_instructions():
    f = open("input_day8")

    instructions = []
    for line in f:
        instruction, value = line.strip().split(' ')
        instructions.append((instruction, int(value)))

    f.close()

    return instructions


def part_1(instructions):
    num_instructions = len(instructions)
    instructions_run = set()
    instr_pointer = 0
    accumulator = 0

    while True:
        if instr_pointer in instructions_run:
            break
        if instr_pointer >= len(instructions):
            break
        instructions_run.add(instr_pointer)
        current_instruction, current_value = instructions[instr_pointer]
        if current_instruction == 'nop':
            instr_pointer += 1
        elif current_instruction == 'acc':
            accumulator += current_value
            instr_pointer += 1
        elif current_instruction == 'jmp':
            instr_pointer += current_value
        else:
            raise Error(f"Unexpected instruction {current_instruction}, {current_value}")

    print(f"Accumulator has value {accumulator}")


def create_dag(instructions):
    dag = {}

    for i in range(len(instructions)):
        instr = instructions[i]
        next_instr = i + 1
        if instr[0] == 'jmp':
            next_instr = i + instr[1]

        dag[i] = next_instr

    return dag


def cycle_exists(graph):
    nodes_visited = set()
    current_node = graph[0]
    nodes_visited.add(current_node)
    while len(nodes_visited) < len(graph):
        next_node = graph[current_node]
        if next_node in nodes_visited:
            return True

        if next_node >= len(graph):
            return False

        nodes_visited.add(next_node)
        current_node = next_node

    return False


def part_2(instructions):
    nops_and_jumps = [i for i in range(0, len(instructions)) if instructions[i][0] == 'nop' or instructions[i][0] == 'jmp']

    while len(nops_and_jumps) > 0:
        index = random.choice(range(0, len(nops_and_jumps)))
        random_instr_pointer = nops_and_jumps[index]
        nops_and_jumps.pop(index)

        # change instruction to the opposite
        instructions_copy = instructions[:]
        the_instruction = instructions_copy[random_instr_pointer]
        if the_instruction[0] == 'jmp':
            instructions_copy[random_instr_pointer] = ('nop', the_instruction[1])
        elif the_instruction[0] == 'nop':
            instructions_copy[random_instr_pointer] = ('jmp', the_instruction[1])

        # create a DAG
        dag = create_dag(instructions_copy)

        # check for cycle
        if not cycle_exists(dag):
            print(f"Found the instruction to remove, it's at position {random_instr_pointer}")
            part_1(instructions_copy)
            break


if __name__ == '__main__':
    instructions = collect_instructions()
    part_1(instructions)
    part_2(instructions)
