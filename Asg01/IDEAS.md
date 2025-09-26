# Programming Exercise Ideas

## Overview

This document contains additional programming exercise ideas that complement the existing problem bank. The exercises are designed to reinforce fundamental programming concepts including conditionals, loops, strings, lists, and dictionaries, with difficulty levels ranging from Easy to Medium.

The exercises are organized by concept area and build upon the pedagogical approach established in the existing curriculum materials.

## 1. Mathematical and Numerical Patterns

### Exercise 1: Find Minimum Without Built-ins
**Description:** Write a program that finds the minimum value in a list of numbers without using the built-in `min()` function. The program should read a comma-separated list of numbers from the user.

**Keywords:** Lists, Loops, Conditionals, Comparison operations, Variable tracking
**Difficulty:** Easy
**Hints:** Use a variable to track the current minimum, iterate through the list comparing each element.

---

### Exercise 2: Find Maximum Without Built-ins
**Description:** Write a program that finds the maximum value in a list of numbers without using the built-in `max()` function. The program should also report the position (index) where the maximum occurs.

**Keywords:** Lists, Loops, Conditionals, Index tracking, Variable management
**Difficulty:** Easy
**Hints:** Similar to minimum finding, but also keep track of the index where maximum occurs.

---

### Exercise 3: Calculate Mean Without Built-ins
**Description:** Write a program that calculates the arithmetic mean (average) of a list of numbers without using built-in functions like `sum()`. Display the result with 2 decimal places.

**Keywords:** Lists, Loops, Mathematical operations, Accumulation, String formatting
**Difficulty:** Easy-Medium
**Hints:** Use an accumulator to sum values, then divide by list length. Use string formatting for decimal precision.

---

### Exercise 4: Prime Number Checker
**Description:** Write a program that determines if a given number is prime. A prime number is only divisible by 1 and itself. The program should handle numbers up to 1000.

**Keywords:** Loops, Conditionals, Modular arithmetic, Mathematical algorithms, Boolean logic
**Difficulty:** Easy-Medium
**Hints:** Check divisibility from 2 up to the square root of the number. Use early termination for efficiency.

---

### Exercise 5: Prime Numbers in Range
**Description:** Write a program that finds all prime numbers between two given numbers (inclusive). Display the primes and count how many were found.

**Keywords:** Loops, Conditionals, List operations, Mathematical algorithms, Counting
**Difficulty:** Medium
**Hints:** Combine prime checking algorithm with range iteration. Store results in a list.

---

### Exercise 6: Fibonacci Sequence Generator
**Description:** Write a program that generates the first n numbers of the Fibonacci sequence. Each number is the sum of the two preceding numbers (starting with 0, 1).

**Keywords:** Loops, Mathematical sequences, Variable management, List operations
**Difficulty:** Easy-Medium
**Hints:** Use two variables to track the previous two numbers, or build a list incrementally.

---

### Exercise 7: Perfect Number Detector
**Description:** Write a program that determines if a number is "perfect" - a positive integer equal to the sum of its proper positive divisors (excluding itself). Example: 6 is perfect because 1+2+3=6.

**Keywords:** Loops, Mathematical operations, Modular arithmetic, Accumulation, Divisibility
**Difficulty:** Medium
**Hints:** Find all divisors less than the number, sum them, and compare to the original number.

---

### Exercise 8: Digital Root Calculator
**Description:** Write a program that calculates the digital root of a number - repeatedly sum the digits until a single digit is obtained. Example: 9875 → 9+8+7+5=29 → 2+9=11 → 1+1=2.

**Keywords:** Loops, String conversion, Mathematical operations, Digit manipulation
**Difficulty:** Medium
**Hints:** Convert to string to access digits, use nested loops or recursion concept with while loop.

---

## 2. Geometric and Visual Patterns

### Exercise 9: Triangle Pattern
**Description:** Write a program that prints a right triangle pattern using asterisks (*). The user specifies the height. Example for height 4:
```
*
**
***
****
```

**Keywords:** Loops, String repetition, Pattern generation, Nested loops
**Difficulty:** Easy
**Hints:** Use nested loops - outer for rows, inner for columns. Use string multiplication for repeated characters.

---

### Exercise 10: Inverted Triangle Pattern
**Description:** Write a program that prints an inverted right triangle pattern. Example for height 4:
```
****
***
**
*
```

**Keywords:** Loops, String repetition, Pattern generation, Counting operations
**Difficulty:** Easy
**Hints:** Similar to regular triangle but decreasing number of characters per row.

---

### Exercise 11: Diamond Pattern
**Description:** Write a program that creates a diamond pattern using asterisks. The user specifies the width of the middle row (odd number). Example for width 5:
```
  *
 ***
*****
 ***
  *
```

**Keywords:** Loops, String operations, Nested loops, Pattern symmetry, Mathematical calculations
**Difficulty:** Medium
**Hints:** Think of it as two triangles - expanding then contracting. Calculate spaces and asterisks for each row.

---

### Exercise 12: Number Triangle
**Description:** Write a program that creates a triangle where each row contains consecutive numbers. Example for 4 rows:
```
1
1 2
1 2 3
1 2 3 4
```

**Keywords:** Loops, Number sequences, String formatting, Nested loops
**Difficulty:** Easy-Medium
**Hints:** Outer loop for rows, inner loop for numbers in each row.

---

### Exercise 13: Floyd's Triangle
**Description:** Write a program that generates Floyd's triangle - a right triangle of natural numbers. Example for 4 rows:
```
1
2 3
4 5 6
7 8 9 10
```

**Keywords:** Loops, Number sequences, Pattern generation, Counter variables
**Difficulty:** Easy-Medium
**Hints:** Use a counter that continues across rows, incrementing for each position.

---

### Exercise 14: Checkerboard Pattern
**Description:** Write a program that creates a checkerboard pattern using two different characters (like 'X' and 'O'). The user specifies the size (n x n grid).

**Keywords:** Loops, Conditionals, Pattern generation, Nested loops, Modular arithmetic
**Difficulty:** Medium
**Hints:** Use modular arithmetic to determine which character based on position coordinates.

---

## 3. String Processing and Text Analysis

### Exercise 15: Word Reverser
**Description:** Write a program that takes a sentence and reverses each word individually while keeping the word order the same. Example: "Hello World" becomes "olleH dlroW".

**Keywords:** Strings, String methods, List operations, String slicing, Text processing
**Difficulty:** Easy-Medium
**Hints:** Split sentence into words, reverse each word using slicing, join back together.

---

### Exercise 16: Initials Extractor
**Description:** Write a program that extracts the initials from a person's full name. Handle multiple middle names. Example: "John Michael Smith" → "J.M.S."

**Keywords:** Strings, String methods, List processing, Text formatting
**Difficulty:** Easy
**Hints:** Split name into parts, take first character of each part, format with periods.

---

### Exercise 17: Character Frequency Analyzer
**Description:** Write a program that counts the frequency of each character in a text string (case-insensitive). Display results sorted by frequency, then alphabetically.

**Keywords:** Strings, Dictionaries, Loops, Text analysis, Sorting concepts
**Difficulty:** Medium
**Hints:** Use dictionary to count characters, iterate through string, handle case conversion.

---

### Exercise 18: Caesar Cipher Encoder
**Description:** Write a program that implements a simple Caesar cipher - shifting each letter by a fixed number of positions in the alphabet. Handle wrapping (z+1=a) and preserve non-alphabetic characters.

**Keywords:** Strings, ASCII values, Modular arithmetic, Character manipulation, Encryption concepts
**Difficulty:** Medium
**Hints:** Use ord() and chr() functions, handle uppercase and lowercase separately, use modulo for wrapping.

---

### Exercise 19: Text Formatter
**Description:** Write a program that formats text by capitalizing the first letter of each sentence and ensuring proper spacing. Handle multiple punctuation marks that end sentences (. ! ?).

**Keywords:** Strings, String methods, Text processing, Conditionals, Character classification
**Difficulty:** Easy-Medium
**Hints:** Identify sentence endings, capitalize following letter, handle spacing consistently.

---

### Exercise 20: Anagram Checker
**Description:** Write a program that determines if two words are anagrams (contain the same letters with the same frequency). Case should be ignored.

**Keywords:** Strings, Character counting, Dictionaries or sorting concepts, Comparison operations
**Difficulty:** Medium
**Hints:** Count character frequencies in both words, compare the results. Alternative: sort characters and compare.

---

### Exercise 21: Text Statistics
**Description:** Write a program that analyzes text and reports: total characters, total words, total sentences, average word length, and most common word.

**Keywords:** Strings, Text analysis, Dictionaries, Mathematical operations, String methods
**Difficulty:** Medium
**Hints:** Use split() for words, count sentence markers, track word frequencies, calculate averages.

---

### Exercise 22: Acronym Generator
**Description:** Write a program that generates an acronym from a phrase by taking the first letter of each significant word (ignore common words like "the", "and", "of"). Example: "North Atlantic Treaty Organization" → "NATO".

**Keywords:** Strings, Lists, String methods, Conditionals, Text processing
**Difficulty:** Easy-Medium
**Hints:** Create list of common words to ignore, split phrase, check each word, extract first letters.

---

## 4. List Operations and Data Processing

### Exercise 23: List Intersection
**Description:** Write a program that finds the common elements between two lists (intersection). The result should not contain duplicates and should be sorted.

**Keywords:** Lists, Set operations, Loops, Conditionals, Duplicate removal
**Difficulty:** Easy-Medium
**Hints:** Use nested loops to compare elements, or use dictionary to track occurrences in both lists.

---

### Exercise 24: List Rotation
**Description:** Write a program that rotates a list by k positions to the right. Example: [1,2,3,4,5] rotated by 2 becomes [4,5,1,2,3].

**Keywords:** Lists, List slicing, Index manipulation, Mathematical operations
**Difficulty:** Easy-Medium
**Hints:** Use list slicing with calculated positions, handle cases where k > list length.

---

### Exercise 25: Mode Finder
**Description:** Write a program that finds the mode(s) - the most frequently occurring element(s) in a list. Handle cases with multiple modes.

**Keywords:** Lists, Dictionaries, Frequency counting, Loops, Maximum finding
**Difficulty:** Medium
**Hints:** Count frequencies using dictionary, find maximum frequency, collect all elements with max frequency.

---

### Exercise 26: List Partitioner
**Description:** Write a program that partitions a list into two lists: one with even numbers and one with odd numbers. Maintain original order within each partition.

**Keywords:** Lists, Conditionals, Modular arithmetic, List operations, Classification
**Difficulty:** Easy
**Hints:** Create two empty lists, iterate through original list, append to appropriate list based on even/odd test.

---

### Exercise 27: Moving Average Calculator
**Description:** Write a program that calculates the moving average of a list with a specified window size. Example: [1,2,3,4,5] with window 3 gives [2.0, 3.0, 4.0].

**Keywords:** Lists, Mathematical operations, Loops, List slicing, Average calculation
**Difficulty:** Medium
**Hints:** Use nested loops or list slicing to extract windows, calculate average of each window.

---

### Exercise 28: List Zipper
**Description:** Write a program that "zips" two lists together alternately. If lists are different lengths, append remaining elements from longer list. Example: [1,2,3] and ['a','b'] becomes [1,'a',2,'b',3].

**Keywords:** Lists, Loops, Index management, List operations, Conditional logic
**Difficulty:** Easy-Medium
**Hints:** Use while loop with dual indices, handle different lengths separately.

---

### Exercise 29: Duplicates Remover with Position Tracking
**Description:** Write a program that removes duplicates from a list while reporting the original positions where duplicates occurred.

**Keywords:** Lists, Dictionaries, Index tracking, Loops, Data cleaning
**Difficulty:** Medium
**Hints:** Use dictionary to track first occurrence of each element and positions of duplicates.

---

### Exercise 30: Range Overlap Checker
**Description:** Write a program that takes a list of number ranges (represented as [start, end] pairs) and determines which ranges overlap.

**Keywords:** Lists, Conditionals, Mathematical operations, Nested loops, Range comparison
**Difficulty:** Medium
**Hints:** Compare each pair of ranges, check if one range's start is less than another's end.

---

## 5. Dictionary Applications

### Exercise 31: Grade Book Manager
**Description:** Write a program that manages student grades using dictionaries. Allow adding students, recording grades for different subjects, and calculating averages. Display grade reports sorted by student name.

**Keywords:** Dictionaries, Lists, Mathematical operations, Data management, String formatting
**Difficulty:** Medium
**Hints:** Use nested dictionaries (student → subject → grades), calculate averages using sum and length.

---

### Exercise 32: Inventory Management System
**Description:** Write a program that manages store inventory. Track item names, quantities, and prices. Support operations: add item, update quantity, check stock, calculate total inventory value.

**Keywords:** Dictionaries, Mathematical operations, Conditionals, Data management, Input validation
**Difficulty:** Medium
**Hints:** Use dictionary with item names as keys, values as dictionaries containing quantity and price.

---

### Exercise 33: Contact Directory
**Description:** Write a program that manages a contact directory. Store name, phone, email for each contact. Support searching by partial name, listing all contacts, and updating information.

**Keywords:** Dictionaries, String operations, Loops, Search algorithms, Data organization
**Difficulty:** Easy-Medium
**Hints:** Use contact name as key, contact details as nested dictionary. Use substring matching for search.

---

### Exercise 34: Word Frequency Histogram
**Description:** Write a program that analyzes text and creates a visual histogram of word frequencies using asterisks. Scale the display so the longest bar fits in 50 characters.

**Keywords:** Dictionaries, String processing, Mathematical operations, Data visualization, Scaling
**Difficulty:** Medium
**Hints:** Count word frequencies, find maximum count, scale all counts proportionally for display.

---

### Exercise 35: Menu Ordering System
**Description:** Write a program that simulates a restaurant ordering system. Maintain menu with items and prices, track customer orders, calculate totals including tax, and generate receipts.

**Keywords:** Dictionaries, Mathematical operations, String formatting, Data management, Real-world applications
**Difficulty:** Medium
**Hints:** Use menu dictionary for items/prices, order dictionary to track quantities, calculate totals with tax.

---

### Exercise 36: Election Results Tracker
**Description:** Write a program that tracks election results. Record votes for different candidates across multiple districts, calculate totals, percentages, and determine winners.

**Keywords:** Dictionaries, Mathematical operations, Data aggregation, Loops, Statistical calculations
**Difficulty:** Medium
**Hints:** Use nested dictionaries (district → candidate → votes), aggregate across districts, calculate percentages.

---

## Summary

This collection of 36 additional exercises provides comprehensive coverage of fundamental programming concepts:

- **Mathematical Operations:** 8 exercises focusing on algorithms and numerical processing
- **Pattern Generation:** 6 exercises emphasizing visual and geometric patterns
- **String Processing:** 8 exercises covering text analysis and manipulation
- **List Operations:** 8 exercises exploring data structures and algorithms
- **Dictionary Applications:** 6 exercises demonstrating real-world data management

**Difficulty Distribution:**
- Easy: 12 exercises (33%)
- Easy-Medium: 12 exercises (33%)
- Medium: 12 exercises (33%)

These exercises complement the existing problem bank while introducing new variations and practical applications that reinforce the core concepts taught in the COMP3083 curriculum.