import os, sys

def command_sequence(branch):
    os.system('git add .')
    os.system('git commit -m "default message"')
    os.system(f'git push origin {branch}')

command_sequence(sys.argv[1])
