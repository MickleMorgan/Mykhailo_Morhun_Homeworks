import re


def task_1(string):
    pattern = '[Rr][bB]{1,}[Rr]'
    return re.findall(pattern, string)

def task_2(card_num):
    pattern = '([\d]{4}[\s|-]){3}[\d]{4}'
    if not re.search(pattern, card_num):
        raise TypeError('Invalid Card number')
    return card_num
# print(task_2('9919-9999-9999-9199'))

def task_3(e_mail:str):
    pattern = '[a-zA-Z0-9](-?[a-zA-Z0-9_\.])+@[a-zA-Z0-9]+(\.[a-zA-Z0-9-]+)'
    if not re.match(pattern, e_mail):
        raise TypeError('Invalid EMail')
    return e_mail

# print(task_3('misha@gmail.com'))

def task_4(login:str):
    pattern = '^[a-zA-Z0-9]{2,8}$'
    if not re.match(pattern, login):
        raise TypeError('Invalid Login')
    return login

print(task_4('goodone'))
print(task_4('totalybadone'))