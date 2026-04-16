# LeetCode Solutions

All LeetCode problems solved in this repository.

| # | Problem | Difficulty | File | Approach |
|---|---|---|---|---|
| 1 | Two Sum | Easy | `Leetcode/two_pointers/two-sum.py` | Brute-force O(n²) with nested while loops (two pointers) |
| 9 | Palindrome Number | Easy | `Leetcode/Palindrome_number.py` | Reverse digits with modulo arithmetic; compare to original |
| 58 | Length of Last Word | Easy | `Leetcode/length_of_last_word.py` | Strip whitespace, reverse string, count chars until space |
| 121 | Best Time to Buy and Sell Stock | Easy | `Leetcode/best-time-to-buy-and-sell-stock.py` | Greedy single-pass — track running minimum price |
| 121 | Best Time to Buy and Sell Stock | Easy | `Leetcode/two_pointers/best-time-to-buy-and-sell-stock.py` | Two pointers (left = buy day, right = sell day) |
| 125 | Valid Palindrome | Easy | `Leetcode/Valid_palindrome.py` | Two pointers; skip non-alphanumeric chars, compare lowercased |
| 151 | Reverse Words in a String | Medium | `Leetcode/reverse_words_in_a_string.py` | Two pointers on stripped string, collect words right-to-left, join |
| 169 | Majority Element | Easy | `Leetcode/Majority_Element.py` | Approach 1: `statistics.mode()`; Approach 2: frequency dict + `max(key=)` |
| 217 | Contains Duplicate | Easy | `Leetcode/contains-duplicate.py` | Compare `len(nums)` vs `len(set(nums))` |
| 242 | Valid Anagram | Easy | `Leetcode/valid-anagram.py` | Approach 1: sort both strings and compare; Approach 2: frequency dict |
| 283 | Move Zeroes | Easy | `Leetcode/move_zeroes.py` | Iterate list; remove each zero and append to end |
| 344 | Reverse String | Easy | `Leetcode/Reverse_string.py` | Two pointers; swap characters in-place |
| 349 | Intersection of Two Arrays | Easy | `Leetcode/Intersection_of_Two_Arrays.py` | Convert both arrays to sets, use `&` operator |
| 412 | Fizz Buzz | Easy | `Leetcode/FizzBuzz.py` | Iterate 1..n; check divisibility by 15, 5, 3 in order |
| 1108 | Defanging an IP Address | Easy | `Leetcode/defanging-an-ip-address.py` | `str.replace(".", "[.]")` |
| 1929 | Concatenation of Array | Easy | `Leetcode/concatenation-of-array.py` | Return `nums * 2` (list multiplication) |
| 2011 | Final Value of Variable After Performing Operations | Easy | `Leetcode/final-value-of-variable-after-performing-operations.py` | Simulate operations; increment or decrement `x` based on string |
| 2469 | Convert the Temperature | Easy | `Leetcode/Convert_the_Temperature.py` | Apply formulas: Kelvin = celsius + 273.15, Fahrenheit = celsius × 1.8 + 32 |
| 2942 | Find Words Containing Character | Easy | `Leetcode/find-words-containing-character.py` | `enumerate()` over words; collect indices where char is `in` word |
| 3110 | Score of a String | Easy | `Leetcode/score-of-a-string.py` | Sum `abs(ord(s[i]) - ord(s[i+1]))` for all adjacent pairs |

---

**Total solved: 20** (19 unique problems — LC #121 has two implementations)

**Difficulty breakdown:** 19 Easy · 1 Medium
