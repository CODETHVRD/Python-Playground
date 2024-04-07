#!/usr/bin/python3

#function to convert pascal or camel cased string to  snake case
def convert_to_snake_case(pascal_or_camel_cased_string):
	snake_cased_char_list = [
		'_' + char.lower() if char.isupper()
		else char
		for char in pascal_or_camel_cased_string
]
	return ''.join(snake_cased_char_list).strip('_')

#main function that calls the other functions
def main():
	convert_to_snake_case()
	print(convert_to_snake_case('aLongAndComplexString'))

if __name__=='__main__':
	main()



