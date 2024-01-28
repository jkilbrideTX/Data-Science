import sys

text = sys.argv[1]

def count_vowels():
  x = text.lower()
  vowels = set()
  count_unique = 0
  for i in x:
    if i in "aeiou":
      vowels.add(i)
  print(len(vowels))
  
count_vowels()
