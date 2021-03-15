import os
from datetime import date

path = os.path.join(os.getcwd(), str(date.today()))

with open(path + '.md', 'w') as file:
    pass
