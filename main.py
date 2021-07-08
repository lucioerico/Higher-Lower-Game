import random
from art import logo
from art import vs
from game_data import data
import os


#listtocompare 'name' 'follower_count' 'description'  'country'
#list that receive from c
a = []
#lists that first receive
b = []
#reservelist
c = []

def random_select():
  """function to select a data to list c """
  c.clear()
  select = random.choice(data)
  c.append (select)
  return c

def enter_vacuoAB():
  """function to put value into the lists for first try """
  while a == []:
      if b == []:
          b.insert(0, c[0])
      elif a == []:
          first_a = random.choice(data)
          a.append (first_a)

def enter_valueB():
  """function to change valor of b """
  if b != []:
      b.clear()
      b.insert(0, c[0])
      return b

def bchanger():
    """function to change the value of A and B"""
    while a == b:
        b.clear()
        random_select()
        b.insert(0, c[0])
        if a == b:
            b.clear()
            random_select()
            b.insert(0, c[0])
        elif a != b:
            return b and c
        
def enter_valueA():
    """Function to keep the old B to go into A"""
    if a != []:
        a.clear()
        a.insert(0, c[0])
        return a

#GAME LOOP    
print (logo)
current_score = 0
game_is_over = False

while game_is_over == False:   
    random_select()
    enter_vacuoAB()
    enter_valueB()
    bchanger()
    print(f"Compare A: {a[0]['name']}, {a[0]['description']}, {a[0]['country']}")
    print(vs)
    print(f"Against B: {b[0]['name']}, {b[0]['description']}, {b[0]['country']}")
    guess_user = input("Who has more followers? Type 'A' or 'B':").lower()
    if guess_user == 'a':
        if (a [0]['follower_count']) > (b [0]['follower_count']):          
            current_score += 1
            game_is_over += False
            #copiar valor de B para A
            enter_valueA()
            os.system('clear') or None
          
        elif (a [0]['follower_count']) < (b [0]['follower_count']):
            game_is_over += True
            print(f"Sorry, that's wrong. Final score:{current_score}")
            
    elif guess_user == 'b':
        if (a [0]['follower_count']) > (b [0]['follower_count']):
            game_is_over += True
            print(f"Sorry, that's wrong. Final score:{current_score}")
            
           
        elif (a [0]['follower_count']) < (b [0]['follower_count']):
            current_score += 1
            game_is_over += False
            #copiar valor de B para A
            enter_valueA()
            os.system('clear') or None

    #limpar console