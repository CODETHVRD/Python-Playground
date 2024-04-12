
from email import message

from matplotlib.pylab import choice


def get_duo_alpha(alpha):
    duo_alpha = alpha * 2
    return duo_alpha

def Recieve_message():
    encryption_input = input('Please enter a message to encrypt: ')
    return encryption_input

def Recieve_encrypted():
    decryption_input = input('Please enter the encrypted message: ')
    return decryption_input

def get_cipher_key():
    displacement_key = int(input('Please enter a key (whole number from 1 - 25): '))
    while displacement_key not in range(1,26):
        displacement_key = int(input('Please enter a key between 1 and 25: ')) 
    return displacement_key

def encryption(message, cipher_key, alphabet):
    encrypted_message = ''
    uppercase_message = ''
    uppercase_message = message.upper()
    for current_char in uppercase_message:
        index_position = alphabet.find(current_char)
        new_index_position = index_position + int(cipher_key)
        if current_char in alphabet:
            encrypted_message = encrypted_message + alphabet[new_index_position]
        else:
            encrypted_message = encrypted_message + current_char
    return encrypted_message

def decryption(message, cipher_key, alphabet):
    decryption_key = -1 * int(cipher_key)
    return encryption(message,decryption_key,alphabet)

def run_Ceasar():
        Alphabet_String = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    #print(f'Alphabet: {Alphabet_String}')
        Alphabet_String_2 = get_duo_alpha(Alphabet_String)
    #print(f'Alphabet2: {Alphabet_String_2}')
    #creates a loop which starts the menu, it also works to ensure that any number that isnt in the choices gets relooped to the start point
        while True:
            # createda a tuple that contains the menu, makes it easier to call the menu later
            menu = (print('1. Encryption'),
            print('2. Decryption'),
            print('3. Exit'))
            
            # this is the input question below the menu, displays the number options available to select, if any number apart from the ones displayed are choses it loops
            Choice_question = input('Please select number 1 - 3 to access the programs:\n')

            #maps the encryption to the 1st choice
      
            if Choice_question =='1':
                Message = Recieve_message()
                Cipher_key = get_cipher_key()
                Encrypted_message = encryption(Message, Cipher_key,Alphabet_String_2)
                print(f'Encrypted message: {Encrypted_message}')
                # adds a choice to see if the user is done with the program, if he is done, he exists the program, if he isnt he returns to the base menu
                while True:
                    try:
                        choice_question_2 = input('Do you wish to return to the menu, Enter Y or N: ').upper()
                        if choice_question_2 != 'Y' or choice_question_2 != 'N':
                            raise ValueError
                    except ValueError:
                            print('Please input Y or N')
                            continue
                    else:
                        break
                if choice_question_2 == 'Y':
                        menu
                        Choice_question
                elif choice_question_2 == 'N':
                        print('Exiting Cipher program')
                        break

        #maps the decryption to the 2nd choice
            elif Choice_question =='2':
                Message = Recieve_encrypted()
                Cipher_key = get_cipher_key()
                Decrypted_message = decryption(Message,Cipher_key,Alphabet_String_2)
                print(f'Decrypted message: {Decrypted_message}')
                while True:
                    try:
                        choice_question_2 = input('Do you wish to return to the menu, Enter Y or N: ').upper()
                        if choice_question_2 != 'Y' or choice_question_2 != 'N':
                            raise ValueError
                    except ValueError:
                            print('Please input Y or N')
                            continue
                    
                    else:
                        break
                if choice_question_2 == 'Y':
                        menu
                        Choice_question
                elif choice_question_2 == 'N':
                        print('Exiting Cipher program')
                        break
        #allows to exit the loop and shut down the program
            elif Choice_question =='3':
                print('Exiting Cipher program')
                break
            
run_Ceasar()


    



    

