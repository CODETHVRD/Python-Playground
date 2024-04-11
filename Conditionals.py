#[10:44 AM] Unknown User
#If / Elif / Else Lab:
#Try creating your own if, elif, else statement - what will you be assessing? Age, Grades, bank balance?
#Try to set the input value to be all lower case
#Try to find a way to change the input so that users will not make spelling mistakes

while True:
    print('\nOptions')
    print('1. Stamps')
    print('2. Envelopes')
    print('3. Make a copy')
    print('4. Exit')
    
    userReply = input('Would you like to buy stamps, buy an envelope, or make a copy? (Enter stamps, envelope, or copy)\n').lower()

    if userReply == '1':
        print('We have many stamp designs to choose from.')

    elif userReply == '2':
        print('We have many envelope sizes to choose from.')

    elif userReply == '3':
        copies = input('How many copies would you like? (Enter a number) ')
        print(f'Here are your {copies} copies')

    elif userReply == '4':
        print('Thank you, please come again.')
    break