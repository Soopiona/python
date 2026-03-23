# Assignment #1: Anagram Checker
#
# Background: Anagram Checker is a program that takes two words and determines
# if an anagram can be made from it. If so, the program will return True, otherwise False.


# ── Part 1: Building the base Anagram Checker ──────────────────────────────
# Given two valid strings, check to see if they are anagrams of each other.
# Uppercase letters are treated the same as lowercase characters.
#
# Examples:
#   anagram_checker("Silent", "listen") # True
#   anagram_checker("Silent", "Night")  # False
#   anagram_checker("night", "Thing")   # True

def anagram_checker(word_a, word_b):
    if sorted(word_a) == sorted(word_b):
        print("Anagram")
    else:
        print("Not anagram")

anagram_checker("Silent", "listen")
anagram_checker("Cider", "Cried")
anagram_checker("Race", "Kare")


# ── Part 2: Expanding the functionality of the Anagram Checker ─────────────
# Added a boolean option `is_case_sensitive` to control whether the comparison
# respects letter casing.

def anagram_checker(word_a, word_b, is_case_sensitive):
    if not is_case_sensitive:
        word_a = word_a.lower()
        word_b = word_b.lower()

    if sorted(word_a) == sorted(word_b):
        print("Anagram")
    else:
        print("Not anagram")

anagram_checker("Silent", "listen", False)  # True
anagram_checker("Part", "trap", True)        # False
anagram_checker("heart", "earth", True)      # False
