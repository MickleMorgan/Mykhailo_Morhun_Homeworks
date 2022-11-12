def task1_week():
    WEEK = {1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"}
    day = int(input("Put the day number:"))
    print(WEEK.get(day, 'Wrong number'))


def task2_cat():
    my_cat = {"color": "Gray",
              "breed": "Mixed",
              "size": "Average",
              "behaviour": "Calm",
              "age": "4 years",
              "vaccination certificate": "Till 2024"}
    print(my_cat.get(input("What you what to know about my cat?"), "Ask something different"))

def task3_chars_counter():
    # To use dictionary and set
    text = str(input('Please, put some text:'))
    counter = {}
    for char in set(text.replace(" ", "")):
        counter[char] = text.count(char)
    print(counter)

def task3_1_chars_counter():
    # To create output in accordance with mentioned in task
    text = str(input('Please, put some text:'))
    for char in set(text.replace(" ", "")):
        print(f'"{char}" - {text.count(char)}')


def task4_two_strings():
    text_1 = str.lower(input('Please, put some text:'))
    text_2 = str.lower(input('Please, put some text:'))
    print(set(text_1) & set(text_2))


def task5_6_two_lists_compare():
    list_3 = [x for x in range(3, 100, 3)]
    list_5 = [x for x in range(5, 100, 5)]
    common_list = list(set(list_3) & set(list_5))
    print(common_list)
