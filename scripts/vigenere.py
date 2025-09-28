import sys
import util

def shift_numbers_vigenere(plaintext_nums: list[int], key_nums: list[int]) -> list[int]:
    for i in range (0, len(plaintext_nums)):
        plaintext_nums[i] = (plaintext_nums[i] + (key_nums[i % len(key_nums)])) % 26
    return plaintext_nums

def encrypt(plaintext: str, key:str) -> str:
    try:
        plaintext_numbers = util.convert_string_to_number_list(plaintext)
        key_numbers = util.convert_string_to_number_list(key)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_plaintext_numbers = shift_numbers_vigenere(plaintext_numbers, 
                                                         key_numbers)
    try:
        return util.convert_number_list_to_string(shifted_plaintext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)

def decrypt_with_known_key(ciphertext: str, key:str) -> str:
    try:
        ciphertext_numbers = util.convert_string_to_number_list(ciphertext)
        key_numbers = util.convert_string_to_number_list(key)
    except ValueError as e:
        print(e)
        sys.exit(1)
    for i in range (0, len(key_numbers)):
        key_numbers[i] = (26 - key_numbers[i]) % 26
    shifted_ciphertext_numbers = shift_numbers_vigenere(ciphertext_numbers,
                                                          key_numbers)
    try:
        return util.convert_number_list_to_string(shifted_ciphertext_numbers)
    except ValueError as e:
        print(e)
        sys.exit(1)

def main():
    print('CLI TOOLS ARE NOT READY YET!')

if __name__ == '__main__':
    main()