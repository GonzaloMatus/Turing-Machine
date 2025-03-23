q0 = "q0"
qf = "qf"

LEFT = -1
RIGHT = 1

START = "S"
END = "E"

    

class TuringMachine:
    def __init__(self):
        self.transitions = dict()
        self.tape = None
        self.validWord = None
        self.proccessed_word = None
        self.debug_mode = False
        
    def load_transitions(self, transitions: list[list]):
        for transition in transitions:
            self.validate(transition)
            self.transitions[(transition[0], transition[1])] = (transition[2], transition[3], transition[4])

    def load_word(self, word: list):
        self.tape = [START] + word


    def is_loaded_word_valid(self):
        if self.proccessed_word is None:
            Exception("No Word Processed")
        return self.validWord
    
    def get_processed_word(self):
        if self.proccessed_word is None:
            Exception("No Word Processed")
        return self.proccessed_word
    

    
    def validate(self, transition):
        self.validate_start_state(transition[0])
        self.validate_start_symbol(transition[1])
        self.validate_end_state(transition[2])
        self.validate_end_symbol(transition[3])
        self.validate_direction(transition[3])

    def validate_start_state(self, state: str):
        if state == qf:
            Exception("Transitions can't start with qf")
        if state is None:
            Exception("Start state can't be None")
    
    def validate_start_symbol(self, start_symbol: str):
        if start_symbol is None:
            Exception("Start symbol can't be None")

    def validate_end_state(self, state: str):
        if state is None:
            Exception("End state can't be None")

    def validate_end_symbol(self, end_symbol: str):
        if end_symbol is None:
            Exception("End symbol can't be None")
    
    def validate_direction(self, direction: int):
        if direction not in (LEFT, RIGHT):
            Exception("Direction has to be either 1 or -1")


    def run(self):
        self.validWord = False
        if self.tape is None:
            Exception("No tape loaded")

        state = q0
        pointer = 1
        while state!= qf:
            if self.debug_mode:
                if input().lower() == "end":
                    return
                print_configuration(state, self.tape, pointer)

            symbol = self.tape[pointer]

            if (state, symbol) not in self.transitions:
                self.validWord = False
                return
            
            new_state, new_symbol, direction = self.transitions[(state, symbol)]
            state = new_state
            self.tape[pointer] = new_symbol
            pointer += direction

            if pointer >= len(self.tape):
                self.tape.append(END)

        self.validWord = True
        self.proccessed_word = self.tape

def print_configuration(state, list, index):
    colored_text = [f"\033[31m{x}\033[0m" if i == index else x for i, x in enumerate(list)]
    print(f"{state}, {' '.join(colored_text)}")
