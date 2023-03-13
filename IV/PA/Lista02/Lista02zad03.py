import re


Q = ('q0', 'q1', 'q2', 'q3')
E = ('a', '0', '1')
q = 'q0'
F = 'q3'


inp = input('Enter the input string: ')

pattern = "^a[01]+a[01]+$"
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
            q = 'q2' if character == 'a' else 'q1'
        case 'q2':
            q = 'q2' if character == 'a' else 'q3'
        case 'q3':
            q = 'q3'
    print(q)


for char in inp:
    func(char)

if q == F:
    print("\nAccepted")
else:
    print("\nNot accepted")
