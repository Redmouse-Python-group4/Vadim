import os
import json


def scan(path):
    name = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        name['type'] = 'directory'
        name['children'] = [scan(os.path.join(path, x)) for x in os.listdir(path)]
    else:
        name['type'] = 'file'
    return name

path = raw_input('Enter your path: ')

f = open('result.json', 'wb')
json.dump(scan(path), f)
f.close()