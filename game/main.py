import random

options = ('piedra', 'papel', 'tijera')

computer_wins = 0
user_wins = 0
rounds = 1

while True:

  print('*' * 10)
  print('ROUND', rounds)
  print('*' * 10)
  print ('Score Usuario', user_wins)
  print ('Score Computer', computer_wins)
  
  user_option = input("Elije piedra, papel o tijera = ")
  user_option = user_option.lower()
  computer_option = random.choice(options)
  
  print('User option: ', user_option)
  print('Computer option: ', computer_option)
  
  if user_option not in options:
    print('Esa opcion no es valida')
    continue
  
  if user_option == computer_option:
    print("Empate")
  elif user_option == "piedra":
    if computer_option == "tijera":
      print("User gano")
      user_wins += 1
    else:
      print("Computer gano")
      computer_wins += 1
  elif user_option == "papel":
    if computer_option == "piedra":
      print("User gano")
      user_wins += 1
    else:
      print("Computer gano")
      computer_wins += 1
  elif user_option == "tijera":
    if computer_option == "papel":
      print("User gano")
      user_wins += 1
    else:
      print("Computer gano")
      computer_wins += 1

  if computer_wins == 2:
    print('Computer gana 2 rounds')
    break
  elif user_wins == 2:
    print('User gana 2 rounds')
    break

  rounds += 1
  
  