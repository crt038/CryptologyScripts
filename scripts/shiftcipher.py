import sys
import util
import argparse
import textwrap

def encrypt(plaintext: str, key: int) -> str:
    try:
        plaintext_numbers = util.convert_string_to_number_list(plaintext)
    except ValueError as e:
        print(e)
        sys.exit(1)
    shifted_plaintext_numbers = shift_numbers_caesar(plaintext_numbers, key)
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
    shifted_ciphertext_numbers = shift_numbers_caesar(ciphertext_numbers,
                                                      reversed_key)
    try:
        return util.convert_number_list_to_string(shifted_ciphertext_numbers).lower()
    except ValueError as e:
        print(e)
        sys.exit(1)

def decrypt_brute_force(ciphertext: str) -> str:
    print('Here is every possible decryption of the ciphertext: \n')
    for i in range (0, 26):
        print(f'{decrypt_with_known_key(ciphertext, i)} (key = {i})\n')
    return 'Brute force complete.'

def shift_numbers_caesar(numbers: list[int], shift: int) -> list[int]:
    for i in range (0, len(numbers)):
        numbers[i] = (numbers[i] + shift) % 26
    return numbers

def main():
    descriptionstring = textwrap.dedent('''\
        shiftcipher.py: encrypt/decrypt text via a caesarian shift.
        
        Examples:
        - Encrypt "helloworld" with shift = 9:
          INPUT: shiftcipher.py encrypt helloworld --key 9
          OUTPUT: "QNUUXFXAUM"
          
        - Decrypt "QNUUXFXAUM" with KNOWN shift = 9:
          INPUT: shiftcipher.py decrypt QNUUXFXAUM --key 9
          OUTPUT: "helloworld"
          
        - Decrypt "QNUUXFXAUM" with UNKNOWN shift (bruteforce):
          INPUT: shiftcipher.py decrypt QNUUXFXAUM --bruteforce
          OUTPUT: "qnuuxfxaum (key = 0), pmttwewztl (key = 1),
          olssvdvysk (key = 2)..." (tries all keys 0-25)

        Notes:
        - plaintext will be outputted as lowercase
        - CIPHERTEXT will be outputted as UPPERCASE
        - Do not include spaces or non-alphabetic characters in the text input.
        - The --bruteforce and --key options are mutually exclusive.
        - --bruteforce will try all keys 0-25 and print the result of each.
        - Using --key for decryption will simply print THAT corresponding result.
        - So, do not try to use both options when decrypting.
        - Also, do not try to use the bruteforce option when encrypting.
    ''')
    usagestring = textwrap.dedent('%(prog)s encrypt|decrypt <text> ( --bruteforce | --key )')
    parser = argparse.ArgumentParser(prog='shiftcipher.py', usage=usagestring,
                                     description=descriptionstring,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('desire', choices=['encrypt', 'decrypt'], help='encrypt or decrypt')
    parser.add_argument('text', help='plaintext or CIPHERTEXT (no spaces)')
    parser.add_argument('--bruteforce', help='displays all possible caesarian decryptions',
                        action='store_true')
    parser.add_argument('--key', type=int, help='specify integer shift amount (if known)')
    args = parser.parse_args()
    
    if args.desire == 'decrypt':
        if not args.bruteforce and args.key is None:
            parser.error('a --key must be given if you dont want to --bruteforce')
        elif args.bruteforce and args.key is not None:
            parser.error('do not enter a --key if you want to --bruteforce')
        elif args.bruteforce:
            print(decrypt_brute_force(args.text))
        else:
            print(decrypt_with_known_key(args.text, args.key))
             
    else:
        if args.bruteforce:
            parser.error('you cannot use --bruteforce when encrypting')
        elif args.key is None:
            parser.error('you must enter a --key to use for encryption')
        else:
            print(encrypt(args.text, args.key))
          
if __name__ == '__main__':
    main()