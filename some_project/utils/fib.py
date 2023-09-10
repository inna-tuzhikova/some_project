def fib(n: int):
    if not isinstance(n, int):
        raise TypeError(
            f'Invalid `n` argument type: '
            f'expected int, got {n.__class__.__name__}'
        )
    if n < 0:
        raise ValueError(f'`n` should be >= 0, got {n}')
    return n if n <= 1 else fib(n-2) + fib(n-1)
