# Python Topics Covered

All Python concepts detected across every `.py` file in this repository.

---

## Variables & Data Types

| Concept | Where Used |
|---|---|
| Integer, float, string, bool, NoneType | `Practice/basics.py` |
| `type()` to inspect data types | `Practice/basics.py` |
| Type conversion: `int()`, `float()`, `str()` | `Practice/basics.py`, `Practice/loops.py` |
| Variable assignment and reassignment | All files |
| `None` type | `Practice/basics.py` |

---

## Operators

| Concept | Where Used |
|---|---|
| Arithmetic operators `+ - * / // ** %` | `task_1.py`, `Practice/basics.py`, `Practice/loops.py` |
| Comparison operators `> < == != >= <=` | `Practice/control_statements.py`, `Practice/loops.py` |
| Logical operators `and`, `or`, `not` | `Practice/basics.py`, `Practice/control_statements.py` |
| Assignment operators `+=`, `-=`, `*=` | `Practice/basics.py`, `Practice/loops.py` |
| Membership operator `in` | `Practice/basics.py`, `Practice/tuples_sets_dict.py`, `Leetcode/find-words-containing-character.py` |
| Modulo operator `%` | `ASSIGNMENT 2/Task_1.py`, `Practice/control_statements.py`, `Practice/loops.py` |

---

## Strings

| Concept | Where Used |
|---|---|
| f-strings | `ASSIGNMENT 2/Task_1.py`, `Practice/basics.py`, `Practice/loops.py`, many others |
| String slicing `[start:end:step]` | `Practice/basics.py`, `Practice/lists.py` |
| Reverse string with `[::-1]` | `Practice/basics.py`, `Leetcode/length_of_last_word.py` |
| `.count()` | `Practice/basics.py` |
| `.replace()` | `Practice/basics.py`, `Leetcode/defanging-an-ip-address.py` |
| `.upper()`, `.lower()` | `Practice/basics.py`, `Practice/roll_dice.py`, `Leetcode/Valid_palindrome.py` |
| `.strip()` | `Leetcode/length_of_last_word.py`, `Leetcode/reverse_words_in_a_string.py` |
| `.startswith()`, `.endswith()` | `Practice/basics.py` |
| `.isalnum()` | `Leetcode/Valid_palindrome.py` |
| `len()` on strings | `Practice/basics.py`, `Practice/count_digits.py` |
| String concatenation | `task_2.py` |
| Escape sequences `\n`, `\t` | `Practice/basics.py` |
| `in` membership test on strings | `Practice/basics.py`, `Practice/loops.py` |
| `" ".join()` | `Leetcode/reverse_words_in_a_string.py` |
| `ord()` for ASCII values | `Leetcode/score-of-a-string.py` |
| `sorted()` on strings | `Leetcode/valid-anagram.py` |
| f-string number format spec `:.2f` | `Practice/compound_interest.py` |

---

## Conditional Statements

| Concept | Where Used |
|---|---|
| `if / else` | `ASSIGNMENT 2/Task_1.py`, `Practice/control_statements.py`, many others |
| `if / elif / else` | `Practice/control_statements.py`, `Practice/loops.py` |
| Nested `if` | `Practice/control_statements.py` |
| Ternary-style conditions | `Practice/1d_Array.py` (generator expressions with `if`) |

---

## Loops

| Concept | Where Used |
|---|---|
| `for` loop with `range()` | `ASSIGNMENT 2/Task_2.py`, `Practice/loops.py`, many Leetcode files |
| `for` loop over list/string/set | `Practice/loops.py`, `Practice/tuples_sets_dict.py`, `Practice/lists.py` |
| `while` loop | `Practice/loops.py`, `Practice/banking.py`, many Leetcode files |
| `while True` infinite loop | `Practice/loops.py`, `Practice/banking.py`, `Practice/roll_dice.py` |
| `break` | `Practice/loops.py`, `Practice/banking.py`, `Practice/number_guess.py` |
| `continue` | `Practice/loops.py` |
| `for / else` clause | `Practice/loops.py`, `Practice/number_guess.py` |
| Nested loops | `Practice/Patterns/pattern1.py`, `Practice/Patterns/pattern3.py`, `Practice/Patterns/pattern4.py` |
| `enumerate()` | `Leetcode/find-words-containing-character.py` |

---

## Functions

| Concept | Where Used |
|---|---|
| Function definition with `def` | `Practice/factorial.py`, `Practice/banking.py`, `Practice/Count_digits_in_a_number.py`, all Leetcode files |
| Return values | `Practice/factorial.py`, all Leetcode files |
| Parameters and arguments | `Practice/banking.py`, all Leetcode files |
| Recursion | `Assignment 3/task_1.py`, `Practice/factorial.py` |
| Base case in recursion | `Assignment 3/task_1.py`, `Practice/factorial.py` |
| `global` variables | `Practice/banking.py` |
| `pow()` built-in | `Practice/compound_interest.py` |
| Type hints / annotations | `Leetcode/Convert_the_Temperature.py`, `Leetcode/FizzBuzz.py`, `Leetcode/contains-duplicate.py`, `Leetcode/valid-anagram.py` |

---

## Lists

| Concept | Where Used |
|---|---|
| List creation and indexing | `Practice/lists.py`, `Practice/1d_Array.py` |
| List slicing `[start:end:step]` | `Practice/lists.py` |
| `.append()` | `Practice/lists.py`, `Practice/1d_Array.py`, many Leetcode files |
| `.insert()` | `Practice/lists.py` |
| `.extend()` | `Practice/lists.py` |
| `.remove()`, `.pop()` | `Practice/lists.py`, `Leetcode/move_zeroes.py` |
| `.sort()`, `.reverse()` | `Practice/lists.py` |
| `.count()` on lists | `Practice/lists.py` |
| `sum()`, `max()`, `min()` | `Practice/lists.py`, `Practice/1d_Array.py` |
| List multiplication `nums * 2` | `Leetcode/concatenation-of-array.py` |
| `float('-inf')` for initializing max/min | `Practice/1d_Array.py` |
| Generator expressions | `Practice/1d_Array.py` |

---

## Tuples

| Concept | Where Used |
|---|---|
| Tuple creation and indexing | `Practice/tuples_sets_dict.py` |
| Tuple slicing | `Practice/tuples_sets_dict.py` |
| Tuple methods: `.count()`, `in` | `Practice/tuples_sets_dict.py` |
| Tuple concatenation with `+` | `Practice/tuples_sets_dict.py` |
| Converting list to tuple with `tuple()` | `Practice/tuples_sets_dict.py` |
| Immutability of tuples | `Practice/tuples_sets_dict.py` |
| Tuple swap `a, b = b, a` | `Leetcode/Reverse_string.py` |

---

## Sets

| Concept | Where Used |
|---|---|
| Set creation with `set()` | `Practice/tuples_sets_dict.py`, `Practice/array_logic_building.py` |
| `.add()`, `.discard()` | `Practice/tuples_sets_dict.py` |
| Set union `\|`, intersection `&`, difference `-` | `Practice/tuples_sets_dict.py`, `Practice/array_logic_building.py`, `Leetcode/Intersection_of_Two_Arrays.py` |
| `frozenset` (immutable set) | `Practice/tuples_sets_dict.py` |
| Removing duplicates with `set()` | `Leetcode/contains-duplicate.py`, `Leetcode/Intersection_of_Two_Arrays.py` |

---

## Dictionaries

| Concept | Where Used |
|---|---|
| Dictionary creation | `Practice/tuples_sets_dict.py`, `Leetcode/Majority_Element.py` |
| Accessing, updating, adding keys | `Practice/tuples_sets_dict.py` |
| `.pop()` to remove a key | `Practice/tuples_sets_dict.py` |
| `.keys()`, `.values()`, `.items()` | `Practice/tuples_sets_dict.py` |
| `.get()` with default value | `Leetcode/valid-anagram.py` |
| `max(dict, key=dict.get)` | `Practice/tuples_sets_dict.py`, `Leetcode/Majority_Element.py` |
| Frequency counting with dict | `Leetcode/Majority_Element.py`, `Practice/Frequencies in a Limited Array.py` |
| Iterating over dict | `Practice/tuples_sets_dict.py` |

---

## Classes & OOP

| Concept | Where Used |
|---|---|
| Class definition with `class` | `Practice/Count_digits_in_a_number.py`, `Practice/count_digits.py`, `Practice/Frequencies in a Limited Array.py`, all Leetcode solution files, all Pattern files |
| Instance methods (`def method(self, ...)`) | All Leetcode files, `Practice/banking.py` (function-based equivalent) |
| `self` parameter | All Leetcode files |

---

## Modules & Standard Library

| Module | What's Used | Where |
|---|---|---|
| `math` | `math.sqrt`, `math.log`, `math.sin` | `Assignment 3/task_2.py` |
| `random` | `random.randint()` | `Practice/number_guess.py`, `Practice/roll_dice.py` |
| `os` | `os.path.exists()` | `Practice/file_handling.py` |
| `statistics` | `statistics.mode()` | `Leetcode/Majority_Element.py` |

---

## File Handling

| Concept | Where Used |
|---|---|
| `open()` with `with` statement | `Practice/file_handling.py` |
| Write mode `"w"` | `Practice/file_handling.py` |
| Read mode `"r"` | `Practice/file_handling.py` |
| Append mode `"a"` | `Practice/file_handling.py` |
| `.write()`, `.read()` | `Practice/file_handling.py` |
| `os.path.exists()` | `Practice/file_handling.py` |

---

## Algorithms & Patterns

| Concept | Where Used |
|---|---|
| Two-pointer technique | `Leetcode/Reverse_string.py`, `Leetcode/Valid_palindrome.py`, `Leetcode/reverse_words_in_a_string.py`, `Leetcode/two_pointers/best-time-to-buy-and-sell-stock.py`, `Leetcode/two_pointers/two-sum.py` |
| Greedy algorithm (min tracking) | `Leetcode/best-time-to-buy-and-sell-stock.py` |
| Frequency counting | `Leetcode/Majority_Element.py`, `Practice/Frequencies in a Limited Array.py` |
| Missing number (sum formula) | `Practice/array_logic_building.py` |
| Set-based intersection/union | `Practice/array_logic_building.py`, `Leetcode/Intersection_of_Two_Arrays.py` |
| Number reversal (digit by digit) | `Leetcode/Palindrome_number.py` |
| Simulation | `Leetcode/final-value-of-variable-after-performing-operations.py` |
| Sorting-based comparison | `Leetcode/valid-anagram.py` |
| Pattern printing (triangle, rectangle, number patterns) | `Practice/Patterns/` |
| Prime number check (sqrt optimization) | `Practice/loops.py` |
| Second largest element | `Practice/lists.py`, `Practice/1d_Array.py` |
| In-place array mutation | `Leetcode/move_zeroes.py` |
| `abs()` for absolute difference | `Leetcode/score-of-a-string.py` |

---

## Exception Handling

| Concept | Where Used |
|---|---|
| `try / except` block | `Practice/compound_interest.py` |
| Catching `ValueError` | `Practice/compound_interest.py` |

---

## Input / Output

| Concept | Where Used |
|---|---|
| `input()` for user input | `task_1.py`, `task_2.py`, `ASSIGNMENT 2/`, `Assignment 3/`, `Practice/basics.py`, `Practice/loops.py`, many others |
| `print()` with f-string | Most files |
| `print(end="")` to suppress newline | `Practice/Patterns/pattern3.py`, `Practice/Patterns/pattern4.py` |
| String formatting | `task_2.py`, `Practice/basics.py` |
