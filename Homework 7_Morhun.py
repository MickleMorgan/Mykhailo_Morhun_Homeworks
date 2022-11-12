def task1_b_counter():
    text = str(input("Type any text to count b in it:"))
    print(text.lower().count("b"))


def task2_name_verification():
    name = str(input("Type name:"))
    print(name.istitle() and name.isalpha() and "Name is valid" or "Name is invalid, please - check it")


def task3_unicode_char_counter():
    text = str(input("Type any text :"))
    summ_of_codes = 0
    for i in range(len(text)):
        summ_of_codes += ord(text[i])
    print(summ_of_codes)


def task4_pi():
    from math import pi
    for i in range(10):
        print(round(pi, 2 + i))


def task5_longest_word():
    text = str(input("Type any text :"))
    split_text = text.split()
    print("Longest word in text:", max(split_text, key=len))


def task6_Vovochka():
    text = str(input("Vovochka has written :"))
    list_of_codes = [*text]
    shortest = []
    if len(list_of_codes) <= 1 or len(set(list_of_codes)) == len(list_of_codes):
        print(''.join(list_of_codes))
    for x in range(1, len(list_of_codes)):
        if list_of_codes[0:x] == list_of_codes[x:2 * x] and len(shortest) == 0:
            shortest = (list_of_codes[0:x])
    print(''.join(shortest))


def task7_HTML_cleaner():
    import re
    import codecs
    #To use this script, please put the text with HTML tags in .txt file with name "HTML_to_clean" and put it in D/
    # if you want to use any other location - please, correct the related PATH lines in script. Result will be
    # in new file on the D root with name HTML_cleaned.txt
    f = open("D:\HTML_to_clean.txt", "r", encoding='utf-8')
    text = f.readlines()
    clear_text = re.sub("<.*?>", " ", str(text))
    clear_text = codecs.decode(clear_text, 'unicode_escape')
    clear_text = clear_text.replace("', '", "")
    with open("D:\HTML_cleaned.txt", 'w', encoding='utf-8') as f:
        f.write(clear_text)

