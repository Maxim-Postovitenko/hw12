def is_even(n):
    return (n & 1) == 0


text = input("Введіть число або вираз: ")

if "**" in text:
    parts = text.split("**")
    number = int(parts[0])
    power = int(parts[1])
    n = number ** power
else:
    n = int(text)

print(is_even(n))