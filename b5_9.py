class Stopwatch:
    def __init__(self, func, NUM_RUNS = 10):
        import time
        self._NUM_RUNS = NUM_RUNS
        self._t0=time.time()

        for _ in range(NUM_RUNS):
            dt = func()

        self._t1=time.time()
        self._time = self._t1 - self._t0

    def __str__(self):
        return str(self._time)

def fib_list(num):
    fib_list = [0, 1]
    n = 1
    while n < num-1:
        fib_list.append(fib_list[n]+fib_list[n-1])
        n += 1
    return ','.join([str(item) for item in fib_list])

def main():
    NUM_RUNS = 10
 #   fib_stopwatch = Stopwatch()
    print(fib_list())

if __name__ == "__main__":
    main()
