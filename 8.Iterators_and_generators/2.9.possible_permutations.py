from itertools import permutations


def possible_permutations(nums: list):
    for perm in permutations(nums):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]