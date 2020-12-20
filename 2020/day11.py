FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
ADJACENT_NEIGHBOUR_STRATEGY = 'A'
SIGHT_NEIGHBOUR_STRATEGY = 'S'

class GridRow:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return ''.join([str(cell) for cell in self.cells])

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.cells)

    def get_cell(self, index):
        return self.cells[index]

class GridCell:
    def __init__(self, current_state):
        self.current_state = current_state
        self.next_state = None

    def __str__(self):
        return self.current_state

    def __repr__(self):
        return str(self)

    def is_floor(self):
        return self.current_state == FLOOR

    def is_occupied(self):
        return self.current_state == OCCUPIED

    def is_seat(self):
        return not self.is_floor()

    def set_next_state(self, next_state):
        self.next_state = next_state

    def maintain_state(self):
        self.next_state = self.current_state

    def apply(self):
        if self.next_state is None:
            raise Exception("Cannot apply when next state is None.")

        changed = self.current_state != self.next_state
        self.current_state = self.next_state
        self.next_state = None
        return changed

class Grid:
    def __init__(self, rows, max_occupied_neighbours, neighbour_strategy):
        self.rows = rows
        self.max_occupied_neighbours = max_occupied_neighbours
        self.neighbour_strategy = neighbour_strategy

    def run_round(self):
        num_rows = len(self.rows)
        num_cols = len(self.rows[0])
        state_changed = False

        for i in range(num_rows):
            for j in range(num_cols):
                num_adjacent_neighbours = 0
                if self.neighbour_strategy == SIGHT_NEIGHBOUR_STRATEGY:
                    num_adjacent_neighbours = self.count_visible_occupied_seats(i, j)
                else:
                    num_adjacent_neighbours = self.count_adjacent_neighbours(i, j)
                #num_adjacent_neighbours = self.count_adjacent_neighbours(i, j)

                cell = self.rows[i].get_cell(j)
                if cell.is_floor():
                    cell.set_next_state(FLOOR)
                elif num_adjacent_neighbours == 0:
                    cell.set_next_state(OCCUPIED)
                elif (self.neighbour_strategy == ADJACENT_NEIGHBOUR_STRATEGY and num_occupied_neighbours >= self.max_occupied_neighbours) or (self.neighbour_strategy == SIGHT_NEIGHBOUR_STRATEGY and self.count_visible_occupied_seats(i, j) >= self.max_occupied_neighbours):
                    cell.set_next_state(EMPTY)
                else:
                    cell.maintain_state()

        for i in range(num_rows):
            for j in range(num_cols):
                cell = self.rows[i].get_cell(j)
                state_changed_this_time = cell.apply()
                state_changed = state_changed or state_changed_this_time

        return state_changed

    def count_num_occupied_seats(self):
        num_rows = len(self.rows)
        num_cols = len(self.rows[0])
        occupied_count = 0
        for i in range(num_rows):
            for j in range(num_cols):
                cell = self.rows[i].get_cell(j)
                if cell.is_occupied():
                    occupied_count += 1

        return occupied_count

    def count_adjacent_neighbours(self, row_index, col_index):
        num_rows = len(self.rows)
        num_cols = len(self.rows[0])

        num_occupied_neighbours = 0
        for i in range(row_index - 1, row_index + 2):
            if i < 0 or i >= num_rows:
                continue

            for j in range(col_index - 1, col_index + 2):
                if j < 0 or j >= num_cols:
                    continue

                if i == row_index and j == col_index:
                    continue

                cell = self.rows[i].get_cell(j)
                if cell.is_occupied():
                    num_occupied_neighbours += 1

        return num_occupied_neighbours

    def count_visible_occupied_seats(self, row_index, col_index):
        num_rows = len(self.rows)
        num_cols = len(self.rows[0])

        num_occupied_neighbours = 0

        directions = [
          (-1, -1),
          (-1, 0),
          (-1, 1),
          (0, -1),
          (0, 1),
          (1, -1),
          (1, 0),
          (1, 1)
        ]

        for direction in directions:
            position_to_check = (row_index + direction[0], col_index + direction[1])
            direction_modifier = 1
            while self.__is_valid_position(position_to_check[0], position_to_check[1]):
                cell = self.rows[position_to_check[0]].get_cell(position_to_check[1])
                if cell.is_seat():
                    num_occupied_neighbours += 1 if cell.is_occupied() else 0
                    break
                else:
                    direction_modifier += 1
                    position_to_check = (row_index + direction[0] * direction_modifier,
                                         col_index + direction[1] * direction_modifier)

        return num_occupied_neighbours

    def __str__(self):
        return '\n'.join([str(row) for row in self.rows])

    def __repr__(self):
        return str(self)

    def __is_valid_position(self, row, col):
        num_rows = len(self.rows)
        num_cols = len(self.rows[0])
        return row >= 0 and row < num_rows and col >= 0 and col < num_cols


if __name__ == '__main__':
    grid = []

    f = open('input_day11')

    # create grid
    for line in f:
        line = line.strip()
        row = []
        for char in line:
            row.append(GridCell(char))

        row = GridRow(row)
        grid.append(row)

    grid = Grid(grid, 5, SIGHT_NEIGHBOUR_STRATEGY)

    num_rounds_run = 0

    print(grid)

#    while True:
#        the_input = input('q=quit, r=run round, c1,2=check occupied neighbor count ')
#        if the_input == 'q':
#            break
#        elif the_input == 'r':
#            grid.run_round()
#            print(grid)
#        elif the_input[0] == 'c':
#            coords = the_input.split('c')[1].split(',')
#            coords = [int(coords[0]), int(coords[1])]
#            print(f"Checking coordinates {coords}")
#            print(grid.count_visible_occupied_seats(coords[0], coords[1]))

    while grid.run_round():
        num_rounds_run += 1
        #print('---------------------------')
        #print(grid)

    print(f"Number of occupied seats: {grid.count_num_occupied_seats()}")

    f.close()
