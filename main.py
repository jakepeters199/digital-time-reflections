import time


def is_time_valid(input_time: str) -> bool:
    try:
        time.strptime(input_time, '%H%M')
        return True
    except ValueError:
        return False


def get_reflected_time(time: str) -> str:
    reflected_time = ''
    for digit in time[::-1]:
        if (digit == '2'):
            new_digit = digit.replace('2', '5')
        else:
            new_digit = digit.replace('5', '2')
        reflected_time += new_digit

    return reflected_time


def is_reflectable(digit: str) -> bool:
    return int(digit) in [0, 2, 5, 8]


def is_time_reflectable(time: str) -> bool:
    for digit in time:
        if (is_reflectable(digit) is False):
            return False
    return True


def time_generator():
    times = []

    for i in range(0, 2400):
        if (is_time_valid(str(f"{i:04d}"))):
            times.append(str(f"{i:04d}"))

    return times


if __name__ == '__main__':
    valid_reflectable_times = []
    times = time_generator()

    for _time in times:
        if is_time_reflectable(_time):
            # Check the reflected time is valid also.
            reflected_time = get_reflected_time(_time)
            if (is_time_valid(reflected_time)):
                valid_reflectable_times.append([_time, reflected_time])

    print(len(valid_reflectable_times))
    print(valid_reflectable_times)
