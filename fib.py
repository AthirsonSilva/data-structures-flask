class Fibonacci:
    def __init__(self, n):
        self.n = n

    def __iter__(self, n):
        if n <= 2:
            return 1

        return self.__iter__(n - 1) + self.__iter__(n - 2)


fib = Fibonacci(10)
print(fib.__iter__(fib.n))
