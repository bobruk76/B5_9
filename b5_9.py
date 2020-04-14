



def func_run(func):
    def wrap(param):
        for _ in range(NUM_RUNS):
            dt = func(param)
        return True
    return wrap


NUM_RUNS = 10

#@avg_wrap(NUM_RUNS)

class sec_mer():
    import time

    @func_run
    def __init__(self,NUM_RUNS):
        self._t0=time.time()



class Fib:
    def __init__(self, len=100):
        self._list = [0, 1]
        self._len = len
        n = 1
        while n < len-1:
            self._list.append(self._list[n]+self._list[n-1])
            n += 1

    def __len__(self):
        return len(self._list)

    def __getitem__(self, position):
        return str(self._list[position])

    def __str__(self):
        return ','.join(map(str,self._list))


fib_list = Fib(len=100)
print(fib_list)
print(fib_list[10])