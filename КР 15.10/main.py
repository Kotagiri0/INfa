from collections import Counter

count = 0

with open('09_6602.xls') as f:
    for line in f:
        # Преобразуем строку в список чисел
        nums = list(map(int, line.split()))
        if len(nums) != 6:
            continue  # пропускаем странные строки

        freq = Counter(nums)

        # Числа, которые повторяются ровно дважды
        repeated = [x for x, c in freq.items() if c == 2]
        # Остальные, которые встречаются ровно один раз
        others = [x for x, c in freq.items() if c == 1]

        # Условие 1: одно число повторяется 2 раза, остальные разные
        if len(repeated) == 1 and len(others) == 4:
            rep_num = repeated[0]
            avg_unique = sum(others) / len(others)
            # Условие 2: среднее неповторяющихся ≥ суммы повторяющихся
            if avg_unique >= 2 * rep_num:
                count += 1

print(count)
