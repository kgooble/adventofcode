LEN_OF_ROW_STR = 7

ROW_0 = 'F'
ROW_1 = 'B'

COL_0 = 'L'
COL_1 = 'R'

if __name__ == '__main__':
    f = open('input_day5')

    max_seat_id = -1

    seat_id_pairs = {}

    filled_seat_map = {}

    for line in f:
        line = line.strip()
        # convert line to binary then to decimal
        row_string = line[:LEN_OF_ROW_STR]
        col_string = line[LEN_OF_ROW_STR:]

        row = int(''.join(['0' if x == ROW_0 else '1' for x in row_string]), 2)
        col = int(''.join(['0' if x == COL_0 else '1' for x in col_string]), 2)
        seat_id = row * 8 + col

        if seat_id > max_seat_id:
            max_seat_id = seat_id

        if row not in filled_seat_map:
            filled_seat_map[row] = [col]
        else:
            filled_seat_map[row].append(col)

        seat_kept = False
        keys = list(seat_id_pairs.keys())
        for other_seat_id in keys:
            if other_seat_id + 2 == seat_id:
                seat_id_pairs[other_seat_id] = seat_id
                seat_kept = True
                break
            elif other_seat_id - 2 == seat_id:
                seat_id_pairs[seat_id] = other_seat_id
                seat_kept = True

        if not seat_kept:
            seat_id_pairs[seat_id] = None

    for row, col_list in filled_seat_map.items():
        if len(col_list) != 8:
            print(f"Row {row} has only filled columns {col_list}")
            for missing_col in range(0, 8):
                if missing_col not in col_list:
                    missing_seat_id = row * 8 + missing_col
                    print(f"A missing column is {missing_seat_id}; seat ID is {missing_seat_id}")
                    next_seat_in_map = (missing_seat_id - 1) in seat_id_pairs
                    prev_seat_in_map = (missing_seat_id + 1) in seat_id_pairs
                    print(f"Is the -1 seat id in the map? {next_seat_in_map}")
                    print(f"Is the +1 seat id in the map? {prev_seat_in_map}")

    print(f"The max seat id is {max_seat_id}")

    f.close()
