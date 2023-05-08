import time
import typing
# import functools

def wrapper_time(a_function: typing.Callable) -> typing.Callable:
    def a_wrapped_function(*args, **kwargs):
        time_start = time.time()
        v = a_function(*args, **kwargs)
        time_stop = time.time()
        print(">>>>>Function {} executed in {:3.1f}s".format(a_function.__name__, time_stop - time_start))
        return v

    return a_wrapped_function


def get_sequence(n: int) -> int:
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

wrapper_get_sequence = wrapper_time(get_sequence)
print(wrapper_get_sequence(16))
# exit()

print("-------------")

# wrapper defined by decorator
@wrapper_time
def get_sequence2(n):
    if n <= 0:
        return 1
    else:
        v = 0
        for i in range(n):
            v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
        return v

print(get_sequence2(16))