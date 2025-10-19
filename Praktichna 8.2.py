import random

s = input("Введіть рядок: ")
    

k = len(s) // 3
part1 = s[:k]
part2 = s[k:2*k]
part3 = s[2*k:]

parts = [part1, part2, part3]
random.shuffle(parts)

print("Результат перемішування:")
for p in parts:
     print(p)