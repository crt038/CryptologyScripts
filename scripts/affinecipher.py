import sys
import util

def is_valid_affine_key(a: int, b: int) -> bool:
    return (a % 26) in {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

def encrypt(plaintext: str, a: int, b: int) -> str:
    if not is_valid_affine_key(a, b):
        print('Invalid a value for key: Must be coprime with 26 \n')
        sys.exit(1)
    
    try:
        plaintext_numbers = util.convert_string_to_number_list(plaintext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_plaintext_numbers = shift_numbers_affine(plaintext_numbers, a, b)
    try:
        return util.convert_number_list_to_string(shifted_plaintext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)

def decrypt_with_known_key(ciphertext: str, a: int, b: int) -> str:
    return 'NOT YET IMPLEMENTED!'

def shift_numbers_affine(numbers: list, a: int, b: int) -> list:
    for i in range (0, len(numbers)):
        numbers[i] = ((a * numbers[i]) + b) % 26
    return numbers

print(encrypt('HELLOWORLD', 5, 8))