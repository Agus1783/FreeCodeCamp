def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 50:
        return 'Shift must be an integer between 1 and 50.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz1234567890'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)

def text_input():
    print(f"1. Decrypt text\n2. Encrypt text\n3. Exit")
    choice = input('Enter your choice: ')

    if choice == '1':
        text = input('Enter text to decrypt: ')
        shift_choice = int(input("Shift : \n 1. According to the length of the text. \n2. Enter your shift number."))
        if shift_choice == 1:
            print(f'Decrypted text: {decrypt(text, len(text))}')
        elif shift_choice == 2 :
            shift = int(input('Enter shift value: '))
            print(f'Decrypted text: {decrypt(text, shift)}')
        else :
            print("Invalid input.")
    elif choice == '2':
        text = input('Enter text to encrypt: ')
        shift_choice = int(input("Shift : \n 1. According to the length of the text. \n2. Enter your shift number."))
        if shift_choice == 1:
            print(f'Encrypted text: {encrypt(text, len(text))}')
        elif shift_choice == 2:
            shift = int(input('Enter shift value: '))
            print(f'Encrypted text: {encrypt(text, shift)}')
        else :
            print("Invalid input.")
    elif choice == '3':
        return
    else:
        print('Invalid choice. Please try again.')

text_input()

# this comment is solution for freecodecamp workshop
# encrypted_text = 'UjMwITLzEDMxYUSU1iMw4yMw4yMw4SM' or #encrypt('freeCodeCamp', 3)
# decrypted_text = decrypt(encrypted_text, len(encrypted_text))
# # print(encrypted_text)
# print(decrypted_text)