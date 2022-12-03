def task1_concatenation(number1, number2, text):
    return text + str(number1 + number2)


# print(task1_concatenation(2, 3, "Number"))


def task2_square(wide, height):
    # to add possibility of building symmetric objects horizontal and vertical gaps are aligned
    square = f"{'*  ' * wide}\n"
    for i in range(1, height - 1):
        square += f"*{' ' * (len('*  ' * wide) - 4)}*\n"
    square += f"{'*  ' * wide}\n"
    return square


# print(task2_square())


def task3_number_in_list(number):
    # If you want to get Random list - uncomment next 2 lines and comment line after those 2
    # import random
    # check_list = [random.randrange(100) for i in range(20)]
    check_list = [x for x in range(3, 30, 3)]
    if number in check_list:
        return check_list.index(number)
    else:
        return -1


# print(task3_number_in_list(9))


def task4_words_in_string(text):
    return len(text.split())


# print(task4_words_in_string("We can share our meal together"))

def task5_numeric_to_alphabet(number):
    values = {0: '',
              1: 'one',
              2: 'two',
              3: 'three',
              4: 'four',
              5: 'five',
              6: 'six',
              7: 'seven',
              8: 'eight',
              9: 'nine',
              10: 'ten',
              11: 'eleven',
              12: 'twelve',
              13: 'thirteen',
              14: 'fourteen',
              15: 'fifteen',
              16: 'sixteen',
              17: 'seventeen',
              18: 'eighteen',
              19: 'nineteen',
              20: 'twenty',
              30: 'thirty',
              40: 'forty',
              50: 'fifty',
              60: 'sixty',
              70: 'seventy',
              80: 'eighty',
              90: 'ninety',
              }
    number = number.split(',')
    number = list(map(int, number))
    millions = number[0] // 1_000_000
    thousands = (number[0] - millions * 1_000_000) // 1_000
    hundreds = number[0] - thousands * 1_000 - millions * 1_000_000
    cents = number[1]

    def rank_splitter(rank):
        return rank // 100, ((rank % 100 - rank % 10, rank % 10) if rank % 100 not in values
                             else rank % 100)

    millions = rank_splitter(millions)
    thousands = rank_splitter(thousands)
    hundreds = rank_splitter(hundreds)
    cents = rank_splitter(cents)

    def text_conversion(division):
        text = f"{values[division[0]] + (division[0] > 0) * ' hundred'}{'s' if division[0] > 1 else ''}" \
               f" {values[division[1]] if division[1] in values else values[division[1][0]] + ' ' + values[division[1][1]]}"
        return text

    value_text = f"{text_conversion(millions)}{(number[0] > 1_000_000) * ' million'}" \
                 f"{'s' if (number[0] >= 2_000_000) else ''} " \
                 f"{text_conversion(thousands)}{(number[0] > 1000) * ' thousand'}" \
                 f"{'s' if (number[0] >= 2_000) else ''} " \
                 f"{text_conversion(hundreds)}{(number[0] > 0) * ' dollar'}" \
                 f"{'s' if (number[0] % 10  > 1) or (number[0] % 100) == 11 or (number[0] % 100) == 0 else ''}" \
                 f"{text_conversion(cents)} cent{'s' if (number[1] % 10) or number[1] == 11 else ''}"
    return value_text


print(task5_numeric_to_alphabet('0,99'))


def task6_roman_to_digits(roman: str):
    roman_values = {'I': 1,
                    'IV': 4,
                    'V': 5,
                    'IX': 9,
                    'X': 10,
                    'XL': 40,
                    'L': 50,
                    'XC': 90,
                    'C': 100,
                    'D': 500,
                    'CM': 900,
                    'M': 1000,
                    }
    counter = 0
    digital_values = 0
    while counter + 1 <= len(roman):
        if roman[counter:counter + 2] in roman_values:
            digital_values += roman_values[roman[counter:counter + 2]]
            counter += 2
        else:
            digital_values += roman_values[roman[counter]]
            counter += 1
    if counter < len(roman):
        digital_values += roman_values[roman[counter + 1]]
    return digital_values


print(task6_roman_to_digits('MMMCMXCIX'))
