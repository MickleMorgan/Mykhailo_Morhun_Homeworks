def task_1_lucky_ticket():
    number = list(input("Please, put a number:"))
    number_converted = list(map(int, number))
    first_half = number_converted[:int(len(number) / 2)]
    second_half = number_converted[int(len(number) / 2):]
    print((len(number) % 2 or not sum(first_half) == sum(second_half)) and "Unlucky" or  "Lucky")

def task_2_palindrome():
    number = list(input("Please, put any number:"))
    number_reversed = number.copy()
    number_reversed.reverse()
    print(number == number_reversed and "It's Palindrome" or "It's not a palindrome")

def task_3_circle_and_point():
    RADIUS = 4
    coords = list(input("Please, put the coords:").split())
    coords = list(map(float, coords))
    print((coords[0] ** 2 + coords[1] ** 2) ** 0.5 <= RADIUS and "Point is in circle" or "Point is outside of the circle")


task_3_circle_and_point()