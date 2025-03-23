# Turing Machine API - README

## Overview

This API provides a simple way to define and execute a **Turing Machine**. You can define states, transitions, and input words to simulate the behavior of a Turing Machine.


## Usage

### 1. Importing the Module

Start by importing the necessary classes and constants:

```python
from turing_machine import TuringMachine, q0, qf, LEFT, RIGHT, START, END
```

### 2. Creating a Turing Machine

Initialize a **TuringMachine** object:

```python
turing_machine = TuringMachine()
```

### 3. Defining Transitions

A Turing Machine's behavior is defined using **transition rules**. Each transition follows this format:

```plaintext
[current_state, read_symbol, next_state, write_symbol, move_direction]
```

Example transition rules:

```python
transitions = [
    [q0, "a", "q1", START, RIGHT],  # Initial transition
    ["q1", "a", "q1", "a", RIGHT],  # Move right over 'a'
    ["q1", "A", "q2", "A", LEFT],   # Transition upon encountering 'A'
    ["q1", END, "q2", END, LEFT],   # End reached
    ["q2", "a", "q3", "A", LEFT],   # Convert 'a' to 'A'
    ["q3", "a", "q3", "a", LEFT],   # Move left
    ["q3", START, q0, START, RIGHT],# Return to start
    [q0, "A", "q4", "a", RIGHT],    # Convert 'A' back to 'a'
    ["q4", "A", "q4", "a", RIGHT],  # Move right
    ["q4", END, "q3", END, LEFT],   # Loop back
    ["q2", START, "q5", START, RIGHT], # Final check
    ["q5", END, qf, END, LEFT]      # Accepting state
]

turing_machine.load_transitions(transitions)
```

### 4. Setting the Input Word

Define the word to be processed:

```python
word = "aaaaaa"
turing_machine.load_word(list(word))
```

### 5. Running the Turing Machine

Enable or disable **debug mode** (for detailed output), then execute:

```python
turing_machine.debug_mode = False
turing_machine.run()
```

### 6. Checking the Result

After execution, check if the input word was accepted:

```python
turing_machine.print_word_validity()
```

## Example Output

```plaintext
'aaaaaa' is valid: True
```

## Customization

- Modify **transition rules** to change machine behavior.
- Change the **input word** to test different cases.
- Enable **debug mode** (`turing_machine.debug_mode = True`) to view step-by-step execution.

## License

This project is open-source. Feel free to modify and extend it as needed. 🚀
