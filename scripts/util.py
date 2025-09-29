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
    
def convert_num_to_letter(num: int) -> str:
    if num == 0:
        return 'A'
    elif num == 1:
        return 'B'
    elif num == 2:
        return 'C'
    elif num == 3:
        return 'D'
    elif num == 4:
        return 'E'
    elif num == 5:
        return 'F'
    elif num == 6:
        return 'G'
    elif num == 7:
        return 'H'
    elif num == 8:
        return 'I'
    elif num == 9:
        return 'J'
    elif num == 10:
        return 'K'
    elif num == 11:
        return 'L'
    elif num == 12:
        return 'M'
    elif num == 13:
        return 'N'
    elif num == 14:
        return 'O'
    elif num == 15:
        return 'P'
    elif num == 16:
        return 'Q'
    elif num == 17:
        return 'R'
    elif num == 18:
        return 'S'
    elif num == 19:
        return 'T'
    elif num == 20:
        return 'U'
    elif num == 21:
        return 'V'
    elif num == 22:
        return 'W'
    elif num == 23:
        return 'X'
    elif num == 24:
        return 'Y'
    elif num == 25:
        return 'Z'
    else:
        return 'CONVERSIONPROBLEM'
    
def convert_string_to_number_list(string: str) -> list[int]:
    number_list: list[int] = list()
    for i in range (0, len(string)):
        num = convert_letter_to_num(string[i])
        if num != -1:
            number_list.append(num)
        else:
            raise ValueError('Invalid character in input string: Input string must only include alphabetic characters.')
    return number_list

def convert_number_list_to_string(number_list: list[int]) -> str:
    string = ''
    for i in range (0, len(number_list)):
        letter = convert_num_to_letter(number_list[i])
        if letter != 'CONVERSIONPROBLEM':
            string += letter
        else:
            raise ValueError('Invalid number in input list: Numbers must be from 0 to 25 (inclusive).')
    return string