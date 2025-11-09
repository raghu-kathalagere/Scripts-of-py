from itertools import product

def variants(word):
    return [word, word.capitalize(), word.upper()]

names = ['elliot']
roles = ['alderson', 'hacker']
separators = ['', '-', '_','@']

with open('usernames.txt', 'w') as f:
    for n, r, sep in product(names, roles, separators):
      for nv, nr in product(variants(n), variants(r)):
          f.write(f'{nv}{sep}{nr} \n')
