def task1_sequence(sequence: str):
    sequence_list = list(map(int, sequence.split(',')))
    if sequence_list[1] - sequence_list[0] == sequence_list[2] - sequence_list[1]:
        next_element = sequence_list[len(sequence_list) - 1] + (sequence_list[1] - sequence_list[0])
        return f'{next_element}, arithmetic sequence'
    if sequence_list[1] // sequence_list[0] == sequence_list[2] // sequence_list[1]:
        next_element = sequence_list[len(sequence_list) - 1] * (sequence_list[1] // sequence_list[0])
        return f'{next_element}, geometric sequence'
    for i in range(10):
        if sequence_list[1] == sequence_list[0] ** i:
            next_element = int(sequence_list[len(sequence_list) - 1] ** (1 / i) ** i)
            return f'{next_element}, exponential sequence'
    for i in range(10):
        if sequence_list[1] == (sequence_list[0] + 1) ** i:
            next_element = int((sequence_list[len(sequence_list) - 1] ** (1 / i) + 1) ** i)
            return f'{next_element}, incremental exponential sequence'


# we can count any rank palindrome
def palindrome(rank):
    start = int("".join(map(str, [9]*(rank - 1)))) + 1
    stop = int("".join(map(str, [9]*rank))) + 1
    biggest_palindrome = [0, 0, 0]
    for first_number in range(start, stop):
        for second_number in range(start, stop):
            mult_result = first_number * second_number
            if list(str(mult_result)) == list(reversed(str(mult_result))) and mult_result > biggest_palindrome[0]:
                biggest_palindrome[0] = mult_result
                biggest_palindrome[1] = first_number
                biggest_palindrome[2] = second_number

    return biggest_palindrome

# based on theory that biggest palindrome will always be result of multiplying of numbers started with 9
# we can ignore all number below, but if task will be changed we still need full calculation algorithm,
# so i've made second one simplified and first one will full scale calculations
def palindrome_simplified(rank):
    start = 9 * (10 ** (rank - 1))
    stop = int("".join(map(str, [9]*rank))) + 1
    biggest_palindrome = [0, 0, 0]
    for first_number in range(start, stop):
        for second_number in range(start, stop):
            mult_result = first_number * second_number
            if list(str(mult_result)) == list(reversed(str(mult_result))) and mult_result > biggest_palindrome[0]:
                biggest_palindrome[0] = mult_result
                biggest_palindrome[1] = first_number
                biggest_palindrome[2] = second_number
    return biggest_palindrome







