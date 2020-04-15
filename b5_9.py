class Stopwatch:
    def __init__(self, NUM_RUNS):
        self._NUM_RUNS = NUM_RUNS

    def __call__(self, fn):
        import time
        import statistics as st
        def wrapp(*args):
            self._time_list = []
            for _ in range(self._NUM_RUNS):
                _t0 = time.time()
                _f = fn(*args)
                self._time_list.append(time.time() - _t0)
            self._avg_time = st.mean(self._time_list)
            self._fn_result = _f
            return "{}\n Выполнение заняло {} секунд\n Время выполнения каждого шага:{}".format(self._fn_result, '%.5f' % self._avg_time, ','.join([str(item) for item in self._time_list]))
        return wrapp

    def __str__(self):
        return str(self._time)

NUM_RUNS = 100
@Stopwatch(NUM_RUNS)
def fib_list(num=5000):
    fib_list = [0, 1]
    for n in range(1,num):
        fib_list.append(fib_list[n]+fib_list[n-1])
    return 'Сумма первых {} членов последовательности Фиббоначи равна {}'.format(num, sum(fib_list))

def main():
    num = 500
    print(fib_list(num))

if __name__ == "__main__":
    main()