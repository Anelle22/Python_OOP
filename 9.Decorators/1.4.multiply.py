def number_increment(numbers):
    def increase():
        numbers_increment = []
        for number in numbers:
            numbers_increment.append(number + 1)
        return numbers_increment

    return increase()

print(number_increment([1, 2, 3]))