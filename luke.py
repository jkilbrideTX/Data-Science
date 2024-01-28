import sys

relations = {'Darth Vader':'father', 'Leia':'sister', 'Han':'brother in law',
'R2D2':'droid', 'Rey':'Padawan', 'Tatooine':'homeworld'}

key = (sys.argv[1])

def relationship():
  if key == 'Darth Vader': 
    print('No, I am your father') 
  else: print(f'Luke, I am your {relations[key]}')

relationship()
