# Python Learning Repository

## Overview

A personal Python learning repo by **Yashasri-g** covering beginner to intermediate topics through hands-on assignments, practice exercises, pattern problems, and LeetCode solutions.

---

## Folder Structure

```
Python/
├── ASSIGNMENT 2/
│   ├── Task_1.py
│   └── Task_2.py
├── Assignment 3/
│   ├── task_1.py
│   └── task_2.py
├── Leetcode/
│   ├── two_pointers/
│   │   ├── best-time-to-buy-and-sell-stock.py
│   │   └── two-sum.py
│   ├── Convert_the_Temperature.py
│   ├── FizzBuzz.py
│   ├── Intersection_of_Two_Arrays.py
│   ├── Majority_Element.py
│   ├── Palindrome_number.py
│   ├── Reverse_string.py
│   ├── Valid_palindrome.py
│   ├── best-time-to-buy-and-sell-stock.py
│   ├── concatenation-of-array.py
│   ├── contains-duplicate.py
│   ├── defanging-an-ip-address.py
│   ├── final-value-of-variable-after-performing-operations.py
│   ├── find-words-containing-character.py
│   ├── length_of_last_word.py
│   ├── move_zeroes.py
│   ├── reverse_words_in_a_string.py
│   ├── score-of-a-string.py
│   └── valid-anagram.py
├── Practice/
│   ├── Patterns/
│   │   ├── pattern1.py
│   │   ├── pattern2.py
│   │   ├── pattern3.py
│   │   └── pattern4.py
│   ├── 1d_Array.py
│   ├── Count_digits_in_a_number.py
│   ├── Frequencies in a Limited Array.py
│   ├── array_logic_building.py
│   ├── banking.py
│   ├── basics.py
│   ├── control_statements.py
│   ├── count_digits.py
│   ├── factorial.py
│   ├── file_handling.py
│   ├── lists.py
│   ├── loops.py
│   ├── number_guess.py
│   ├── roll_dice.py
│   └── tuples_sets_dict.py
├── docs/
│   ├── LEETCODE.md
│   └── TOPICS.md
├── task_1.py
└── task_2.py
```

---

## Topics Covered

- Variables, data types, and type conversion
- Operators (arithmetic, comparison, logical, assignment)
- String methods and f-strings
- Conditional statements (`if`, `elif`, `else`)
- Loops (`for`, `while`, `break`, `continue`)
- Functions and recursion
- Lists, tuples, sets, frozensets, and dictionaries
- Classes and OOP basics
- File handling (`open`, `read`, `write`, `append`)
- Standard library modules (`random`, `math`, `os`, `statistics`)
- Array/list algorithms (search, sort, reverse, frequency)
- Two-pointer technique
- Pattern printing

See [docs/TOPICS.md](docs/TOPICS.md) for a detailed breakdown.

---

## How to Run

Each file is standalone. Run any file with:

```bash
python <filename>.py
```

Example:

```bash
python Practice/banking.py
python Leetcode/FizzBuzz.py
```

Python 3.x is required.

---

## File Summary Table

| Filename | Folder | What It Does | Key Python Concepts |
|---|---|---|---|
| task_1.py | root | Takes two numbers as input and prints addition, subtraction, multiplication, and division | `input()`, arithmetic operators, `print()` |
| task_2.py | root | Takes first and last name as input and prints a greeting | `input()`, `str()`, string concatenation |
| Task_1.py | ASSIGNMENT 2 | Checks if a number is even or odd | `if/else`, modulo operator, f-strings |
| Task_2.py | ASSIGNMENT 2 | Computes the sum of integers from 1 to 50 using a loop | `for` loop, `range()`, accumulator pattern |
| task_1.py | Assignment 3 | Computes the factorial of a number using recursion | Functions, recursion, base case |
| task_2.py | Assignment 3 | Computes square root, logarithm, and sine of a number | `import math`, `math.sqrt`, `math.log`, `math.sin` |
| basics.py | Practice | Covers data types, type conversion, string methods, operators, and f-strings through multiple mini-exercises | `type()`, `int()`, `float()`, `str()`, f-strings, string slicing, `.count()`, `.replace()`, `.upper()`, `len()` |
| control_statements.py | Practice | Demonstrates conditional logic: positive/negative check, even/odd, voting eligibility, grade calculator, simple calculator, nested conditions | `if/elif/else`, nested `if`, logical operators |
| loops.py | Practice | Covers for/while loops with exercises: sum to N, vowel count, even numbers, multiplication table, max/min in list, digit sum, prime check, password loop | `for`, `while`, `break`, `continue`, `range()`, infinite loop |
| lists.py | Practice | Exercises on list operations: slicing, append/insert/extend/remove/pop, sort/reverse, sum/max/min, filtering, second largest, manual reverse | List indexing, slicing `[::2]`, `[::-1]`, `.append()`, `.sort()`, `.reverse()`, `sum()`, `max()`, `min()` |
| tuples_sets_dict.py | Practice | Exercises covering tuples, sets (union/intersection/discard), frozensets, and dictionaries (CRUD, iteration) | Tuples, sets, `frozenset`, dicts, `.items()`, `.keys()`, `.values()`, set operators |
| factorial.py | Practice | Implements factorial both iteratively (while loop) and recursively | Functions, recursion, `while` loop |
| banking.py | Practice | Simple banking app with check balance, withdraw, and deposit using a menu-driven while loop | Functions, `global` variables, `while True`, `break`, user input |
| file_handling.py | Practice | Creates, writes to, reads from, and appends to a text file; checks file existence | `open()`, `with` statement, file modes `w/r/a`, `os.path.exists()` |
| 1d_Array.py | Practice | Array fundamentals: find max/min/second-largest, count even/odd and positive/negative/zero, reverse array, check if sorted, sum and average | `for` loops, list indexing, `float('-inf')`, generator expressions |
| Count_digits_in_a_number.py | Practice | Counts the number of digits in an integer using a class method | Classes, `str()`, `len()` |
| Frequencies in a Limited Array.py | Practice | Counts frequency of each element (1 to n) in an array using a dictionary | Classes, `dict`, frequency counting, `range()` |
| array_logic_building.py | Practice | Finds the missing number in a sequence; finds intersection and union of two arrays | `sum()`, `range()`, `set()`, set operators `&` and `\|` |
| count_digits.py | Practice | Counts digits in a number by converting to string | Classes, `str()`, `len()` |
| number_guess.py | Practice | Number guessing game: random number 1–100, up to 10 attempts with high/low hints | `import random`, `random.randint()`, `for/else`, `break` |
| roll_dice.py | Practice | Dice rolling game: user rolls or quits, prints a random number 1–6 each roll | `import random`, `while True`, `.lower()`, `break` |
| pattern1.py | Practice/Patterns | Prints a left-aligned triangle of stars | Nested `for` loop, string multiplication, `range()` |
| pattern2.py | Practice/Patterns | Prints a filled rectangle of stars using a class method | Classes, `for` loop, string multiplication |
| pattern3.py | Practice/Patterns | Prints a right-triangle of incrementing numbers (1, 12, 123…) | Classes, nested `for` loops, `print(end="")` |
| pattern4.py | Practice/Patterns | Prints rows where each row repeats its row number (1, 22, 333…) | Classes, nested `for` loops, `print(end="")` |
| Convert_the_Temperature.py | Leetcode | LC #2469 — Converts Celsius to Kelvin and Fahrenheit | Arithmetic, list, type hints |
| FizzBuzz.py | Leetcode | LC #412 — Classic FizzBuzz up to n | `for` loop, modulo, `list.append()` |
| Intersection_of_Two_Arrays.py | Leetcode | LC #349 — Returns unique intersection of two arrays | `set()`, `&` operator, `list()` |
| Majority_Element.py | Leetcode | LC #169 — Finds element appearing more than n/2 times; two approaches | `statistics.mode`, `dict`, `max(key=)` |
| Palindrome_number.py | Leetcode | LC #9 — Checks if an integer is a palindrome by reversing its digits | `while` loop, modulo, integer reversal |
| Reverse_string.py | Leetcode | LC #344 — Reverses a character list in-place | Two pointers, tuple swap |
| Valid_palindrome.py | Leetcode | LC #125 — Checks if a string is a palindrome ignoring non-alphanumeric chars | Two pointers, `.isalnum()`, `.lower()` |
| best-time-to-buy-and-sell-stock.py | Leetcode | LC #121 — Finds maximum profit from a single buy-sell transaction (greedy) | Greedy, min tracking, single pass |
| concatenation-of-array.py | Leetcode | LC #1929 — Returns array concatenated with itself | List multiplication `nums*2` |
| contains-duplicate.py | Leetcode | LC #217 — Checks if any value appears at least twice | `set()`, `len()` comparison |
| defanging-an-ip-address.py | Leetcode | LC #1108 — Replaces `.` with `[.]` in an IP address string | `.replace()` |
| final-value-of-variable-after-performing-operations.py | Leetcode | LC #2011 — Simulates `++X`, `X++`, `--X`, `X--` operations on a variable | `for` loop, string comparison, simulation |
| find-words-containing-character.py | Leetcode | LC #2942 — Returns indices of words containing a given character | `enumerate()`, `in` operator |
| length_of_last_word.py | Leetcode | LC #58 — Returns the length of the last word in a string | `.strip()`, string reversal, `for` loop |
| move_zeroes.py | Leetcode | LC #283 — Moves all zeroes to the end of a list in-place | `.remove()`, `.append()`, in-place mutation |
| reverse_words_in_a_string.py | Leetcode | LC #151 — Reverses the order of words in a string | Two pointers, `.strip()`, `" ".join()` |
| score-of-a-string.py | Leetcode | LC #3110 — Sums absolute differences of ASCII values of adjacent characters | `ord()`, `abs()`, `for` loop |
| valid-anagram.py | Leetcode | LC #242 — Checks if two strings are anagrams; two approaches (sorting and hashmap) | `sorted()`, `dict`, `.get()` |
| best-time-to-buy-and-sell-stock.py | Leetcode/two_pointers | LC #121 — Same problem with explicit two-pointer (left/right) approach | Two pointers, `while` loop, `max()` |
| two-sum.py | Leetcode/two_pointers | LC #1 — Finds two indices that sum to target using brute-force O(n²) nested pointers | Two pointers, nested `while` loops |
