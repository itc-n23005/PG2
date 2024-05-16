import random
number_of_streaks = random.randint(0, 1)
for experiment_number in range(10000):
    print(f"同じ面が6連続出現する確率: {number_of_streaks / 100}%")
