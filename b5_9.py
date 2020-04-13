import time

def avg_wrap(NUM_RUNS):
    def avg_time(func):
        def wrap(param):
            avg_t = 0.0
            for _ in range(NUM_RUNS):
                t0 = time.time()
                dt = func(param)
                t1 = time.time()
                avg_t += (t1-t0)
            avg_t /= NUM_RUNS
            return avg_t
        return wrap
    return avg_time

NUM_RUNS = 10
@avg_wrap(NUM_RUNS)
def fib_list(num):
    fib_list = [0, 1]
    n = 1
    while n < num-1:
        fib_list.append(fib_list[n]+fib_list[n-1])
        n += 1
    return ','.join([str(item) for item in fib_list])

print(fib_list(50000))


