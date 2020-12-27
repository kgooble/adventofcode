def part_1(ealiest_departure, bus_ids):
    min_wait_time = None
    min_wait_time_bus_id = None
    for bus_id in bus_ids:
        cycles = int(earliest_departure / bus_id)
        bus_departure = cycles * bus_id
        if bus_departure < earliest_departure:
            bus_departure += bus_id

        wait_time = bus_departure - earliest_departure

        if min_wait_time is None or wait_time < min_wait_time:
            min_wait_time = wait_time
            min_wait_time_bus_id = bus_id

    print(f"Bus ID: {min_wait_time_bus_id}, wait time: {min_wait_time}")
    print(f"The product: {min_wait_time_bus_id * min_wait_time}")


def part_2(bus_ids):
    first_bus_id = int(bus_ids[0])

    multiplier = 2
    while True:
        multiple = multiplier * first_bus_id
        faulty = False
        for i in range(1, len(bus_ids)):
            if bus_ids[i] == 'x':
                continue

            # Find out if multiple + i is divisible by bus_id
            if (multiple + i) % int(bus_ids[i]) != 0:
                faulty = True
                break

        if not faulty:
            print(f"Found t: {multiple}")
            break

        multiplier += 1

if __name__ == '__main__':
    f = open('input_day13')

    earliest_departure = int(f.readline().strip())
    raw_bus_ids = f.readline().strip().split(',')
    bus_ids = [int(bus_id) for bus_id in raw_bus_ids if bus_id != 'x']

    part_1(earliest_departure, bus_ids)

    # this runs forever :(
    #part_2(raw_bus_ids)

    f.close()
