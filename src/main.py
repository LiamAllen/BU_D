import dice_operations as dice_ops
import groq_operations as groq_ops
import os

splash_art = r"""

                                                    
    _..---.  .--.-. .-.-.               _,..---._   
  .' .'.-. \/==/ -|/=/  |,--.--------./==/,   -  \  
 /==/- '=' /|==| ,||=| -/==/,  -   , -\==|   _   _\ 
 |==|-,   ' |==|- | =/  \==\.-.  - ,-./==|  .=.   | 
 |==|  .=. \|==|,  \/ - |`--`--------`|==|,|   | -| 
 /==/- '=' ,|==|-   ,   /             |==|  '='   / 
|==|   -   //==/ , _  .'              |==|-,   _`/  
`-._`.___,' `--`..---'                `-.`.____.'   
"""

print(splash_art)
print("Bu-D - The CLI Helper Tool")
print("========================================")
print("type 'exit' to exit the application.")
print("type 'help' for a list of commands.")

global x
x = 0

def exit():
    print("Exiting the application. Goodbye!")
    global x
    x = 1
    return

def help():
    global commands
    print("Available commands:")
    for command in commands:
        print(f"{command} - {commands[command]['description']}")

commands = {
    "roll": {
    "function": dice_ops.roll_query, 
    "description": "Roll dice and calculate sum and average."
    },
    "groq": {
    "function": groq_ops.groq_query,
    "description": "Talk to the Groq AI model."
    },
    "exit": {
    "function": exit,
    "description": "Exit the application."
    },
    "help": {
    "function": help,
    "description": "Show this help message."
    }
}

while x == 0:
    user_input = input("#! ")
    if user_input in commands:
        commands[user_input]["function"]()
    else:
        print("Invalid command.")

# This is the main entry point for the dice rolling application.
# It allows users to roll dice, calculate sums and averages, and exit the application.
# The user can enter commands to interact with the application.
# The application will continue to prompt for commands until the user chooses to exit.
# The operations module contains the logic for rolling dice and calculating results.