import re
import csv

def find_supl(f):
    supplies = f.readlines()
    pairs = list()
    items = list()
    for i in supplies:
        p = re.findall(r"pairs", i)
        it = re.findall(r"items", i)
        if it == [] and p == []:
            pass
        elif it == ['items']:
            items += re.findall(r'^\w+', i)
        elif p == ['pairs']:
            pairs += re.findall(r'^\w+' , i)
    items = ", ".join(items)
    pairs = ", ".join(pairs)
    return [items, pairs]