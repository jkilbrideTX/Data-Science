import sys
text = sys.argv[1]

def cap_count():
  string_count = 0
  index_string_sum = 0
  for i, char in enumerate(text):
    if char.isupper():
      string_count += 1
      index_string_sum += i
  print(string_count)
  print(index_string_sum)

cap_count()
