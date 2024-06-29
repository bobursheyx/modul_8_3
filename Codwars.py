#1 New £5 notes collectors!

def get_new_notes(salary, bills):
    return max((salary - sum(bills)), 0) // 5

#2 The highest profit wins!\

def min_max(arr):
    return [min(arr), max(arr)]


#3 List of all Rationals

def all_rationals():
    yield (1, 1)
    for a, b in all_rationals():
        yield from [(a, a + b), (a + b, b)]


#4 Sum of odd numbers

def row_sum_odd_numbers(n):
    return n ** 3

#5 Monotone travel

def is_monotone(heights):
    return sorted(heights) == heights










