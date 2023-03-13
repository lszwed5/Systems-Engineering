import re


Q = ('q0', 'q1', 'q2', 'q3')
E = ('a', 'b', 'c', 'd')
q = 'q0'
F = 'q0'


inp = input('Enter the input string: ')

pattern = "^a+bcd+$"
if not re.match(pattern, inp):
    raise ValueError("Wrong sequence - the string contains characters that do "
                     "not belong to the alphabet")


def func(character):
    global q
    print(f"{q}({character}) --> ", end='')
    match q:
        case 'q0':
            q = 'q1' if character == 'a' else 'q0'
        case 'q1':
            match character:
                case 'a': q = 'q1'
                case 'b': q = 'q2'
                case _: q = 'q3'
        case 'q2':
            match character:
                case 'c': q = 'q0'
                case 'd': q = 'q1'
                case _: q = 'q3'
        case 'q3':
            q = 'q3'
    print(q)


for char in inp:
    func(char)

if q == F:
    print("\nAccepted")
else:
    print("\nNot accepted")
