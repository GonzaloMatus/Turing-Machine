from turing_machine import TuringMachine, q0, qf, LEFT, RIGHT, START, END

turing_machine = TuringMachine()

trasitions = [
    [q0, "a", "q1", START, RIGHT],

    ["q1", "a", "q1", "a", RIGHT],
    ["q1", "A", "q2", "A", LEFT],
    ["q1", END, "q2", END, LEFT],

    ["q2", "a", "q3", "A", LEFT],

    ["q3", "a", "q3", "a", LEFT],
    ["q3", START, q0, START, RIGHT],

    [q0, "A", "q4", "a", RIGHT],

    ["q4", "A", "q4", "a", RIGHT],
    ["q4", END, "q3", END, LEFT],

    ["q2", START, "q5", START, RIGHT],
    ["q5", END, qf, END, LEFT]
]


turing_machine.load_transitions(trasitions)

word = "aaaaaa"
turing_machine.load_word(list(word))
turing_machine.debug_mode = False
turing_machine.run()
turing_machine.print_word_validity()