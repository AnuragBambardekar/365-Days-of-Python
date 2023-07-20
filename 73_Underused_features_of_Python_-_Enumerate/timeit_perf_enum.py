#Reference:  https://www.youtube.com/watch?v=KzAGzoXv7II

from timeit import timeit

def enumerate_func(val: list) -> list:
    temp_list: list = []
    for i,val in enumerate(val, start=1):
        temp_list.append((i,val))

    return temp_list

def normal_func(val: list) -> list:
    temp_list: list = []
    for i,val in enumerate(val):
        temp_list.append((i+1, val))

    return temp_list

if __name__ == "__main__":
    fifty_numbers: list[int] = list(range(50))

    normal_time: float = timeit(f"normal_func({fifty_numbers})", globals=globals(), number=1_000_000)
    print('i + 1 ->', normal_time)

    enum_start_time: float = timeit(f"enumerate_func({fifty_numbers})", globals=globals(), number=1_000_000)
    print('start = 1 ->', enum_start_time)

    print('Output is same: ', normal_func(fifty_numbers) == enumerate_func(fifty_numbers))