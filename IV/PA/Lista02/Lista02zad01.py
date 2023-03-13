"""
Q : Finite set of states.
Σ : set of Input Symbols.
q : Initial state.
F : set of Final States.
δ : Transition Function.
"""

Q = ('q0', 'q1', 'q2', 'q3')
E = ('0', '1')
q = 'q0'
F = 'q3'


inp = input('Enter the input string: ')

for char in inp:
    if char not in E:
        raise ValueError("Wrong sequence - "
                         "the string contains characters that do not belong "
                         "to the alphabet")


def func(character):
    global q
    print(f"{q}({character}) --> ", end='')
    match q:
        case 'q0':
            q = 'q1' if character == '0' else 'q0'
        case 'q1':
            q = 'q3' if character == '0' else 'q2'
        case 'q2':
            q = 'q2' if character == '0' else 'q0'
        case 'q3':
            q = 'q2' if character == '0' else 'q2'
    print(q)


for char in inp:
    func(char)

if q == F:
    print("\nAccepted")
else:
    print("\nNot accepted")
