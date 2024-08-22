from itertools import combinations

def get_decreasing_number(N):
    decreasing_numbers = []

    for length in range(1, 11):
        for comb in combinations(range(10), length):
            num_str = ''.join(map(str, sorted(comb, reverse=True)))
            decreasing_numbers.append(int(num_str))

    decreasing_numbers.sort()

    if N < len(decreasing_numbers):
        return decreasing_numbers[N]
    else:
        return -1

N = int(input())
result = get_decreasing_number(N)
print(result)