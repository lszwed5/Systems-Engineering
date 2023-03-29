"""
Q is a finite set of states

T is the tape alphabet (symbols which can be written on Tape)

B is blank symbol (every cell is filled with B except input alphabet initially)

∑ is the input alphabet (symbols which are part of input alphabet)

δ is a transition function which maps Q × T → Q × T × {L,R}. Depending on its
    present state and present tape alphabet (pointed by head pointer), it will
    move to new state, change the tape symbol (may or may not) and move head
    pointer to either left or right.

q0 is the initial state

F is the set of final states. If any state of F is reached, input string is
    accepted
"""
import json


class TuringMachine:
    """Class representing a single tape Turing Machine."""

    def __init__(self, config):
        """Initiates the machine."""
        self.Q = config["Q"]
        self.T = config["T"]
        self.B = config["B"]
        self.E = config["E"]
        self.d = config["d"]
        self.q = config["q"]
        self.F = config["F"]

        self.head = 0
        self.tape = []
        self.tape = []
        self.direction = ''

    def check_input(self):
        for char in self.tape:
            if char not in self.E:
                raise ValueError("Wrong sequence - "
                                 "the string contains characters that do not "
                                 "belong to the alphabet")

    def get_input(self):
        """Asks the user for the input to compute."""
        [self.tape.append(char) for char in input('Enter the input string: ')]
        self.check_input()

    def move_head(self):
        """Moves the head to the left or right depending on given function."""
        match self.direction:
            case 'R':
                if len(self.tape) > self.head + 1:
                    self.head += 1
                else:
                    self.tape.append('_')
                    self.head += 1
            case 'L':
                self.head -= 1 if self.head > 0 else self.head

    def assess(self):
        """Assesses the effect of computing."""
        if self.q == 'qa':
            print("\nHalt\n\nAccepted")
        if self.q == 'qr':
            print("\nHalt\n\nRejected")

    def simulate(self):
        """Simulates the working Machine step-by-step."""
        while self.q not in self.F:
            print(50 * '-')
            print('\n' + self.head * 4 * " " + "H")
            print(' | '.join(self.tape) + ' |')
            print(f'State: {self.q} --> ', end='')

            self.direction, self.q, self.tape[self.head] = \
                self.d[self.q][self.tape[self.head]]
            self.move_head()

            print(f'{self.q}\n')

        self.assess()


with open('config_2.json', 'r', encoding='utf-8') as f:
    config_2 = json.load(f)

with open('config_3.json', 'r', encoding='utf-8') as f:
    config_3 = json.load(f)

"""
Accepted input: b
"""

"---------------------------------- Zad 2 ----------------------------------"

tm2 = TuringMachine(config_2)
tm2.get_input()
tm2.simulate()

"---------------------------------- Zad 3 ----------------------------------"

tm3 = TuringMachine(config_3)
tm3.get_input()
tm3.simulate()
