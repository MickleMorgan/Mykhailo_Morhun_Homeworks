def task1_numbers_7():
    count = 7
    while count <= 100:
        print(count)
        count += 7

def task2_factorial():
    number = int(input("Please, input number:"))
    factorial = 1
    for i in range(2, number + 1):
        factorial *= i
    print(factorial)

def task3_multiplying():
    number = int(input("Please, put the number to see the multiplying list:"))
    for i in range (1, 11):
        print(f"{number} x {i} = {number * i}")

def task4_square():
    wide, high = int(input("Please, put the wide:")), int(input("Please, put the high:"))
    # to add possibility of building symmetric objects horizontal and vertical gaps are aligned
    print(f"{'*  ' * wide}")
    for i in range(1, high - 1):
        print(f"*{' ' * (len('*  ' * wide) - 4)}*")
    print(f"{'*  ' * wide}")

def task5_list_of_odd():
    numbers = list(input("Please, input list of numbers:").split())
    count = 0
    for i in range(len(numbers)):
        count += int(numbers[i]) % 2
    print(count)

def task6_double_list():
    import random
    first_list = [random.randrange(100) for i in range(4)]
    second_list = first_list[:] + [item * 2 for item in first_list]
    print(first_list, second_list, sep="\n")

def task7_average():
    import random
    salary_list_year = [random.randrange(10_000, 15_000) for i in range(12)]
    print(salary_list_year)
    print(f"average salary is {sum(salary_list_year)/len(salary_list_year)} ")

def task8_matrix():
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    summary = 0
    for row in matrix:
        summary += sum(row)
        print('\t'.join(map(str, row)))
    print(f'summary is {summary}')

def task9_list_mirroring():
    import random
    first_list = [random.randrange(100) for i in range(4)]
    second_list = first_list[::-1]
    print(first_list, second_list, sep='->')

def task10_all_simple_numbers():
    number_range = int(input("Please, put the range of numbers:"))
    for n in range(2, number_range + 1):
        for i in range(2, n):
            if not n % i:
                break
        else:
            print(n)

def task11_sand_clock():
    width = int(input("What is the width ?:"))
    piramide = []
    for i in range(0, width, 2):
        piramide.append(f"{' '*(i // 2)}{'*'*(width - i)}\n")
    piramide += piramide[-2::-1]
    print(''.join(piramide))


