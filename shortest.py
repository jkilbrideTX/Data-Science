import sys
text = sys.argv[1]

def shortest_word():
  shortest_word = min(text.split(" "), key = len)
  print(f"The shortest word is {shortest_word.upper()}")

shortest_word()
