def generate_cube_numbers(n):
    number = 2

    while True:
        cube = number ** 3

        if cube >= n:
            return

        yield cube
        number += 1


n = int(input("Введіть число: "))

print(list(generate_cube_numbers(n)))