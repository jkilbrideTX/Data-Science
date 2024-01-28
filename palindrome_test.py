import sys
text = (sys.argv[1])

def palindrome():
    x = text.replace(" ", "")
    x = "".join(c for c in text.lower() if c not in text.punctuation)
    palindrome = x [::-1]
    if palindrome == x:
      print ("It's a palindrome!")
    else:
      print ("It's not a palindrome!")

  
palindrome()
