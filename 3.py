def all_rationals():
    yield (1, 1)
    for a, b in all_rationals():
        yield from [(a, a + b), (a + b, b)]