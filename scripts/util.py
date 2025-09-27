def convert_letter_to_num(letter: str) -> int:
    lowercase_letter = str.lower(letter)
    
    if lowercase_letter == 'a':
        return 0
    elif lowercase_letter == 'b':
        return 1
    elif lowercase_letter == 'c':
        return 2
    elif lowercase_letter == 'd':
        return 3
    elif lowercase_letter == 'e':
        return 4
    elif lowercase_letter == 'f':
        return 5
    elif lowercase_letter == 'g':
        return 6
    elif lowercase_letter == 'h':
        return 7
    elif lowercase_letter == 'i':
        return 8
    elif lowercase_letter == 'j':
        return 9
    elif lowercase_letter == 'k':
        return 10
    elif lowercase_letter == 'l':
        return 11
    elif lowercase_letter == 'm':
        return 12
    elif lowercase_letter == 'n':
        return 13
    elif lowercase_letter == 'o':
        return 14
    elif lowercase_letter == 'p':
        return 15
    elif lowercase_letter == 'q':
        return 16
    elif lowercase_letter == 'r':
        return 17
    elif lowercase_letter == 's':
        return 18
    elif lowercase_letter == 't':
        return 19
    elif lowercase_letter == 'u':
        return 20
    elif lowercase_letter == 'v':
        return 21
    elif lowercase_letter == 'w':
        return 22
    elif lowercase_letter == 'x':
        return 23
    elif lowercase_letter == 'y':
        return 24
    elif lowercase_letter == 'z':
        return 25
    else:
        return -1
    
def convert_string_to_number_list(plaintext: str) -> list:
    number_list = list()
    for i in range (0, len(plaintext)):
        num = convert_letter_to_num(plaintext[i])
        if num != -1:
            number_list.append(num)
        else:
            raise ValueError('Invalid character in input string: Input string must only include alphabetic characters.')
    return number_list