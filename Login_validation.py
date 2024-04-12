import json

def read_json(login):
    global logins
    logins = ''
    try: 
        with open('/workspaces/Python-Projects/.vscode/login.json') as json_file:
            logins = json.loads(json_file)
    except IOError:
            print('Could not read file')
    return logins

def validation(username, password):
    if logins[username] == password:
        print('Account Validated, Welcome back:\n {username}')
    else:
         print('Invalid Username/Password please try again.')


def registration(username, password):
    logins[username] = password
    output = json.dumps(logins, indent=4)
    with open('/workspaces/Python-Projects/.vscode/login.json','w') as json_file:
         json_file.write(output)


def Menu():
    global menu
    global username
    global password
    menu = (print('1. Login'),print('2. Register New User'),print('3. Exit menu'))
    user_choice = input('Please select 1 - 3 to acess user options:\n')
    if user_choice in menu == '1':
        username = input('Please enter Username:\n')
        password = input('Please enter password:\n')
        validation(username,password)
    elif user_choice in menu == '2':
        username = input('Please enter Username:\n')
        password = input('Please enter password:\n')
        registration(username,password)
    elif user_choice in menu == '3':
        print('Exiting Menu')

Menu()
    

     
    




