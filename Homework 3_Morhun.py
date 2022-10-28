def Task_1_Print_only_negativ():
    number = int(input("Type any number:"))
    print((number < 0) and number or "Number is not negative")

def Task_2_Less_Than_20():
    number =  int(input("Type any number:"))
    print((number < 20) and "Number is less than 20" or (number == 20) and
          "Number is 20" or (number > 20) and
          "Number is more than 20")

def Task_3_Is_it_Zero():
    number = int(input("Type any number:"))
    print((number == 0) and "Number is 0" or
          f"Number isn't 0")

def Task_4_Even_or_Odd():
    number = int(input("Type any number:"))
    print(bool(number % 2) and "Number is Odd" or "Number is Even")

def Task_5_Largest_of_three():
    number1, number2, number3 = input("Type any number:").split()
    print(max(int(number1), int(number2), int(number3)))
