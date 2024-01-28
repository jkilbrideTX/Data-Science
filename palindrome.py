import sys
text = (sys.argv[1])

def palindrome():
    x = "".join(x for x in text if x.isalnum())
    if x.lower() == x[::-1].lower():
      print ("It's a palindrome!")
    else:
      print ("It's not a palindrome!")

  
palindrome()
