"""
valid input: aaa
"""


Q = ('q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'qa', 'qr')
T = (' ', 'a', '*', '/')
B = ' '
E = (' ', 'a', '*', '/')
q = 'q0'
F = ('qa', 'qr')

head = 0
tape = []
[tape.append(char) for char in input('Enter the input string: ')]

for char in tape:
    if char not in E:
        raise ValueError("Wrong sequence - "
                         "the string contains characters that do not belong "
                         "to the alphabet")


def move_head(direction):
    global head
    match direction:
        case 'R':
            if len(tape) > head + 1:
                head += 1
            else:
                tape.append(' ')
                head += 1
        case 'L': head -= 1 if head > 0 else head


while q not in F:
    print(50*'-')
    print('\n' + head*4*" " + "H")
    print(' | '.join(tape) + ' |')
    print(f'State: {q} --> ', end='')
    match q:
        case 'q0':
            if tape[head] == B:
                move_head('L')
                q = 'qr'
            elif tape[head] == 'a':
                tape[head] = '*'
                move_head('R')
                q = 'q1'
        case 'q1':
            match tape[head]:
                case 'a':
                    move_head('L')
                    q = 'q2'
                case '/':
                    move_head('R')
                case B:
                    move_head('L')
                    q = 'qa'
        case 'q2':
            match tape[head]:
                case '/':
                    move_head('L')
                case '*':
                    move_head('L')
                    q = 'q3'
        case 'q3':
            match tape[head]:
                case '/':
                    move_head('R')
                case 'a':
                    move_head('R')
                    q = 'q4'
                case '*':
                    move_head('R')
                    q = 'q4'
                case B:
                    move_head('L')
                    q = 'q6'
        case 'q4':
            match tape[head]:
                case '/':
                    move_head('R')
                case 'a':
                    tape[head] = '/'
                    move_head('R')
                    q = 'q5'
                case B:
                    move_head('L')
                    q = 'qr'
        case 'q5':
            match tape[head]:
                case '/':
                    move_head('R')
                case 'a':
                    tape[head] = '/'
                    move_head('R')
                    q = 'q3'
                case B:
                    move_head('L')
                    q = 'qr'
        case 'q6':
            match tape[head]:
                case '*':
                    move_head('R')
                    q = 'q1'
                case 'a':
                    move_head('L')
                case '/':
                    move_head('L')
    print(f'{q}\n')

if q == 'qa':
    print("\nHalt\n\nAccepted")
if q == 'qr':
    print("\nHalt\n\nRejected")
