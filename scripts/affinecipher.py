import sys
import util

def is_valid_affine_key(a: int, b: int) -> bool:
    return (a % 26) in {1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25}

def affine_modular_inverse(a: int) -> int:
    if a == 1:
        return 1
    elif a == 3:
        return 9
    elif a == 5:
        return 21
    elif a == 7:
        return 15
    elif a == 9:
        return 3
    elif a == 11:
        return 19
    elif a == 15:
        return 7
    elif a == 17:
        return 23
    elif a == 19:
        return 11
    elif a == 21:
        return 5
    elif a == 23:
        return 17
    elif a == 25:
        return 25
    else:
        return -1
    
def encrypt_numbers_affine(numbers: list[int], a: int, b: int) -> list[int]:
    for i in range (0, len(numbers)):
        numbers[i] = ((a * numbers[i]) + b) % 26
    return numbers

def decrypt_numbers_affine(numbers: list[int], a: int, b: int) -> list[int]:
    for i in range (0, len(numbers)):
        numbers[i] = (a * (numbers[i] - b)) % 26
    return numbers

def encrypt(plaintext: str, a: int, b: int) -> str:
    if not is_valid_affine_key(a, b):
        print('Invalid a value for key: Must be coprime with 26 \n')
        sys.exit(1)
    
    try:
        plaintext_numbers = util.convert_string_to_number_list(plaintext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_plaintext_numbers = encrypt_numbers_affine(plaintext_numbers, a, b)
    try:
        return util.convert_number_list_to_string(shifted_plaintext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)

def decrypt_with_known_key(ciphertext: str, a: int, b: int) -> str:
    if not is_valid_affine_key(a, b):
        print('Invalid a value for key: Must be coprime with 26 \n')
        sys.exit(1)
    inverse_key = affine_modular_inverse(a)
    
    try:
        ciphertext_numbers = util.convert_string_to_number_list(ciphertext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_ciphertext_numbers = decrypt_numbers_affine(ciphertext_numbers,
                                                      inverse_key, b)
    try:
        return util.convert_number_list_to_string(shifted_ciphertext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)  