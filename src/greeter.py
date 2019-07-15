
'''
greeter.py

Sends greetings to one and all. How cool is that... - ha ha!
'''
import sys


def greet(name):
    print('Hello %s!' % name)

def complain():
    print('Hey - you have to tell me your name!')
    

if __name__ == '__main__':
    if len(sys.argv) < 2:
        complain()
    else:
        greet(sys.argv[1])
