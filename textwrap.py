#textwrap
import textwrap

s = "AABCAAADA"
t = 3
x = len(s) // t
words = textwrap.wrap(s, width=2)
print(words)