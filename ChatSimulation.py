#This script demonstrates Chat Simulation while implementing if-else statements.
# It simulates a simple chat interaction based on user input.

print("Welcome to ChatBot Simulator!")
while True:
    user_input = str(input('You: '))
    if user_input == 'Hello':
        print('Bot: Hi there!')
    elif user_input == 'How are you?':
        print('Bot: I am just a program, but thanks for asking!')
    elif user_input == 'What is your name?':
        print('Bot: I am ChatBot 3000.')
    elif user_input == 'Bye':
        print('Bot: Goodbye!')
    elif user_input == 'End':
        print('Bot: Ending the chat. Bye!')
        break
    else:
        print('Bot: Sorry, I do not understand.')

#Prints response based on user input.
#User can add more phrases and responses as needed.
#Use elif to expand the chatbot's capabilities.
#End of Chat Simulation script.