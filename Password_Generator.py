#!/usr/bin/python3

import re
import secrets
import string

def generate_password(length, nums, special_chars, uppercase, lowercase):
#Defines the possible characters for the password
	digits = string.digits
	symbols = string.punctuation
	letters = string.ascii_letters
#Combine all the characters
	all_characters = letters + digits + symbols
	
	#Generate Password
	while True:
		password = ''
        # Generate password
        	for _ in range(length):
            		password += secrets.choice(all_characters)
        
        	constraints = [
            	(nums, r'\d'),
            	(special_chars, fr'[{symbols}]'),
            	(uppercase, r'[A-Z]'),
            	(lowercase, r'[a-z]')
        	]

        # Check constraints        
        if all(
            constraint <= len(re.findall(pattern, password))
            for constraint, pattern in constraints
        ):
            break
    
	return password


if __name__ == '__main__':
	new_password = generate_password()
	print('Generated password:', new_password)
    
