from itertools import product    ## Import product to generate all possible combinations


def variants(word):
    return [word, word.capitalize(), word.upper()]

names = ['elliot']    #your target_uesrname
roles = ['alderson', 'hacker']    #target second_name or their roles or nickname
separators = ['', '-', '_','@']    #special-char or symbols to place between name and role

with open('usernames.txt', 'w') as f:
    for n, r, sep in product(names, roles, separators):
      for nv, nr in product(variants(n), variants(r)):
          f.write(f'{nv}{sep}{nr} \n')
