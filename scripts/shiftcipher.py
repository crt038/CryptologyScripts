import sys
import util

def encrypt(plaintext: str, key: int) -> str:
    try:
        plaintext_numbers = util.convert_string_to_number_list(plaintext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_plaintext_numbers = shift_numbers(plaintext_numbers, key)
    try:
        return util.convert_number_list_to_string(shifted_plaintext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)

def decrypt_with_known_key(ciphertext: str, key: int) -> str:
    try:
        ciphertext_numbers = util.convert_string_to_number_list(ciphertext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    reversed_key = (26 - key) % 26
    shifted_ciphertext_numbers = shift_numbers(ciphertext_numbers, reversed_key)
    try:
        return util.convert_number_list_to_string(shifted_ciphertext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)

def decrypt_brute_force(ciphertext: str) -> str:
    print('Here is every possible decryption of the ciphertext: \n')
    for i in range (0, 26):
        print(decrypt_with_known_key(ciphertext, i) + '\n')
    return 'Brute force complete.'
    
def shift_numbers(numbers: list, shift: int) -> list:
    for i in range (0, len(numbers)):
        numbers[i] = (numbers[i] + shift) % 26
    return numbers