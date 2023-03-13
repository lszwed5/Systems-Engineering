import json


with open('config.json', 'r') as f:
    config = json.load(f)


q = config["q"]
inp = input('Enter the input string: ')
for ch in inp:
    if ch not in config["E"]:
        raise ValueError("Wrong sequence - "
                         "the string contains characters that do not belong "
                         "to the alphabet")


for char in inp:
    print(f"{q}({char}) --> ", end='')
    q = config["d"][q][char]
    print(q)

if q == config["F"]:
    print("\nAccepted")
else:
    print("\nNot accepted")
