import queue
import re

NUM_GROUPS_PER_CHILD = 3
NUM_INITIAL_GROUPS = 3

def calculate_num_sub_bags(forward_graph, bag_name):
    child_bags = forward_graph[bag_name]
    initial_count = 1
    for child_bag in child_bags:
        count = int(child_bag[0])
        child_name = child_bag[1]
        initial_count += count * calculate_num_sub_bags(forward_graph, child_name)

    return initial_count

if __name__ == '__main__':
    f = open('input_day7')

    forward_graph = {}
    backward_graph = {}
    for line in f:
        line = line.strip()
        children = []
        if 'no other bags' in line:
            parent_bag = line.split(' bags contain ')[0]
        else:
            parts = line.split(' bags contain ')
            parent_bag = parts[0]
            listed_bags = parts[1].split(', ')
            for i in range(0, len(listed_bags)):
                bag_with_count = listed_bags[i]
                bag_parts = bag_with_count[:-1].split(' ')
                child_count = bag_parts[0]
                child_name = bag_parts[1] + ' ' + bag_parts[2]
                children.append((child_count, child_name))

                if child_name not in forward_graph:
                    forward_graph[child_name] = []

        forward_graph[parent_bag] = children
        for child_pair in children:
            child_name = child_pair[1]
            child_count = child_pair[0]

            if child_name not in backward_graph:
                backward_graph[child_name] = []

            backward_graph[child_name].append((child_count, parent_bag))

        if parent_bag not in backward_graph:
            backward_graph[parent_bag] = []

    queue = ['shiny gold']
    bags = set()
    while len(queue) > 0:
        current = queue.pop(0)
        parent_bags = [bag_data[1] for bag_data in backward_graph[current]]

        if len(bags.intersection(parent_bags)) < len(parent_bags):
            bags.update(parent_bags)
            queue += parent_bags

    print(f"Num bags that can eventually contain shiny gold: {len(bags)}")

    queue = ['shiny gold']
    num_bags = 0
    child_bags = forward_graph['shiny gold']
    for child_bag in child_bags:
        count = int(child_bag[0])
        name = child_bag[1]
        num_bags += count * calculate_num_sub_bags(forward_graph, name)

    print(f"Number of bags shiny gold bag eventually contains: {num_bags}")
    f.close()

