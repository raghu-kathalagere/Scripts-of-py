from itertools import product
#fun
def variants(word):
        return word, word.capitalize(), word.upper()

#specify your target details

victim_name = ["elliot"]
target_name = ["alderson", "fsociety"]
numbers = ["123", "2005", "1986"]
special_chars = ["@", "!", "#", "$"]

#save passwords into the txt file
with open("passwords.txt", "w") as f:
        for n,t,num,sc in product(victim_name, target_name, numbers, special_chars):
                for nv, tv in product(variants(n), variants(t)):
                        f.write(f"{nv}{tv}{num}{sc} \n")
                        f.write(f"{nv}{tv}{sc}{num} \n")
                        f.write(f"{tv}{nv}{num}{sc} \n")
                        f.write(f"{tv}{nv}{sc}{num} \n")
