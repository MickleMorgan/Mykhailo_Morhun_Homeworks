def Task_1__3():
    int_from_string = int("123")
    print(int_from_string)
    float_from_int= float(123)
    print(float_from_int)
    int_from_float = int(12.345)
    print(int_from_float)

def Task_4_Credit_card_last_4dgts():
    card_number_raw = input("Please, put card number: ")
    card_number_clean = ""
    for i in range(len(card_number_raw)):
        if card_number_raw[i] == "0" or card_number_raw[i] == "1" or card_number_raw[i] == "2" or \
        card_number_raw[i] == "3" or card_number_raw[i] == "4" or card_number_raw[i] == "5" \
        or card_number_raw[i] == "6" or card_number_raw[i] == "7" or card_number_raw[i] == "8" \
                or card_number_raw[i] == "9" :
            card_number_clean = card_number_clean + card_number_raw[i]
    if len(card_number_clean) != 16:
        return print("Wrong card number")
    print("Last 4 digits :", card_number_clean[12:16])

def Task_5_Summ_of_digits():
    three_digit_number = input("Please, put 3 digit number: ")
    summ_of_digits = 0
    if len(three_digit_number) != 3 :
        return print("Number is wrong")
    if three_digit_number.isdigit():
        for i in range(len(three_digit_number)):
            summ_of_digits += int(three_digit_number[i])
        return print("Summ of the digits =", summ_of_digits)
    print("Number is wrong")

def Task_6_Area_of_triangle():
    import math
    side_a = int(input("Side a ="))
    side_b = int(input("Side b ="))
    side_c = int(input("Side c ="))
    semi_perimetr = (side_a + side_b + side_c) / 2
    if semi_perimetr < side_a or semi_perimetr < side_b or semi_perimetr < side_c:
        return print("Such triangle is IMPOSSIBLE")
    area_of_trianlgle = math.sqrt(semi_perimetr * (semi_perimetr - side_a) * (semi_perimetr - side_b)
                                  * (semi_perimetr - side_c))
    print("Area of triangle = ", area_of_trianlgle)

def Task_7_Summ_of_digits():
    digit = input("Please, put a number:")
    summ_of_digits = 0
    if digit.isdigit():
        for i in range(len(digit)):
            summ_of_digits += int(digit[i])
        return print("Summ of digits in number = ", summ_of_digits)
    print("Wrong number")

def Task_8_Number_of_digits():
    digit = input("Please, put a number:")
    if digit.isdigit():
        return print("Number of digits is: ", len(digit))
    print("Wrong number")

def Taks_9_Reverse_digits():
    digit = input("Please, put a number:")
    if digit.isdigit():
        return print("Reverse number is: ", digit[::-1])
    print("Wrong number")

Task_1__3()
Task_4_Credit_card_last_4dgts()
Task_5_Summ_of_digits()
Task_6_Area_of_triangle()
Task_7_Summ_of_digits()
Task_8_Number_of_digits()
Taks_9_Reverse_digits()









