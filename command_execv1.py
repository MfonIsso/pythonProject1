import subprocess

#fixing os command execution vulnerability in python
def command_exec():
    allowed_commands =['ls','pwd','whoami']
    user_input = input("Enter a command: ")
    if user_input in allowed_commands:
        subprocess.run (user_input)
    else:
        print("error. command not allowed ")

command_exec()
