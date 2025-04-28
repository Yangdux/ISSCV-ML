print("Hello, World!")

user_input = input("Enter a command: ")
eval(user_input)  # unsafe usage

import os
os.system('rm -rf /')  # very unsafe!

password = "123456"  # hardcoded password

with open('data.txt', 'w') as f:
    f.write('example')  # maybe safe but write mode
