import random

n = int(input("Скільки рядків будете вводити: "))

for i in range(n):
    s = input("Введіть рядок (довжина кратна 3): ")
    k = len(s) // 3

    part1 = s[:k]
    part2 = s[k:2*k]
    part3 = s[2*k:]

    parts = [part1, part2, part3]
    random.shuffle(parts)  # перемішуємо частини

    new_s = parts[0] + parts[1] + parts[2]
    print("Новий рядок:", new_s)