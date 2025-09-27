import sys
import util

def encrypt(plaintext: str, shift: int) -> str:
    try:
        plaintext_numbers = util.convert_string_to_number_list(plaintext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_plaintext_numbers = shift_numbers(plaintext_numbers, shift)
    try:
        return util.convert_number_list_to_string(shifted_plaintext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)
    
def shift_numbers(numbers: list, shift: int) -> list:
    for i in range (0, len(numbers)):
        numbers[i] = (numbers[i] + shift) % 26
    return numbers

print(encrypt('HELLOWORLD', 3))