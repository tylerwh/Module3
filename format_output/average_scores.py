"""
Author: Tyler Hochstetler
For: Python CIS189
Purpose: This program is to demonstrate gathering user input, formatting the data, and the ouput of that data.
"""


def average():
  score1 = input("Score 1: ")
  score2 = input("Score 2: ")
  score3 = input("Score 3: ")
  number_of_tests = 3
  return (score1 + score2 + score3) / number_of_tests