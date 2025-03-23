q0 = "q0"
qf = "qf"

LEFT = -1
RIGHT = 1

START = "S"
END = "E"

MAX_STEPS = 10000
    

class TuringMachine:
    def __init__(self):
        self.word = None
        self.transitions = dict()
        self.tape = None
        self.validWord = None
        self.processed_word = None
        self.debug_mode = False
        self.max_steps = MAX_STEPS
        
    def load_transitions(self, transitions: list[list]):
        for transition in transitions:
            self.validate(transition)
            self.transitions[(transition[0], transition[1])] = (transition[2], transition[3], transition[4])

    def load_word(self, word: list):
        self.word = word
        self.tape = [START] + word


    def is_loaded_word_valid(self):
        if self.processed_word is None:
            raise Exception("No Word Processed")
        return self.validWord
    
    def get_processed_word(self):
        if self.processed_word is None:
            raise Exception("No Word Processed")
        return self.processed_word
    

    
    def validate(self, transition):
        self.validate_start_state(transition[0])
        self.validate_start_symbol(transition[1])
        self.validate_end_state(transition[2])
        self.validate_end_symbol(transition[3])
        self.validate_direction(transition[4])

    def validate_start_state(self, state: str):
        if state == qf:
            raise Exception("Transitions can't start with qf")
        if state is None:
            raise Exception("Start state can't be None")
    
    def validate_start_symbol(self, start_symbol: str):
        if start_symbol is None:
            raise Exception("Start symbol can't be None")

    def validate_end_state(self, state: str):
        if state is None:
            raise Exception("End state can't be None")

    def validate_end_symbol(self, end_symbol: str):
        if end_symbol is None:
            raise Exception("End symbol can't be None")
    
    def validate_direction(self, direction: int):
        if direction not in (LEFT, RIGHT):
            raise Exception("Direction has to be either 1 or -1")


    def run(self):
        self.validWord = False
        if self.tape is None:
            raise Exception("No tape loaded")
        
        step_count = 0
        state = q0
        pointer = 1
        while state!= qf:
            if step_count > MAX_STEPS:
                raise Exception("Exceeded maximum number of steps. Possible infinite loop.")
            
            if self.debug_mode:
                if input().lower() == "end":
                    return
                self.print_configuration(state, self.tape, pointer)

            symbol = self.tape[pointer]

            if (state, symbol) not in self.transitions:
                self.validWord = False
                self.processed_word = self.tape
                return
            
            new_state, new_symbol, direction = self.transitions[(state, symbol)]
            state = new_state
            self.tape[pointer] = new_symbol
            pointer += direction

            if pointer >= len(self.tape):
                self.tape.append(END)

        self.validWord = True
        self.processed_word = self.tape
        step_count += 1

    @staticmethod
    def print_configuration(state, list, index):
        colored_text = [f"\033[31m{x}\033[0m" if i == index else x for i, x in enumerate(list)]
        print(f"{state}, {' '.join(colored_text)}")

    def print_word_validity(self):
        if self.word is None:
            raise Exception("Tape not loaded")
        word_str = "".join(self.word)
        print(f"'{word_str}' is valid: {self.is_loaded_word_valid()}")

