import os
import time

def screenGrab():
    box=()
    cwd = os.getcwd()
    timeLocal=int(time.time())

    'print(cwd + str(timeLocal))'
    '''
    '''
    print(os.environ.get('PYTHONPATH'))


def main():
    screenGrab()

if __name__ == '__main__':
    main()

