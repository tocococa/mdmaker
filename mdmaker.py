import os
from datetime import date


def mdmaker():
    path = os.path.join(os.getcwd(), str(date.today()))
    with open(path + '.md', 'w') as file:
        pass


if __name__ == '__main__':
    try:
        mdmaker()
    except (OSError, IOError) as e:
        print(f"Error: {e}")