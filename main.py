import characterCreation
import time
import charachterStats
print("WELCOME TO THE GAME!!\n")

player_class, player_name = characterCreation.charCreation()
if(player_class.upper() == 'KNIGHT'):
     charachterStats.strenght = 10
     charachterStats.vitality = 7
     charachterStats.dexterity = 3
     charachterStats.int = 6
     charachterStats.faith = 4
elif(player_class.upper() == 'MAGE'):
     charachterStats.strenght = 4
     charachterStats.vitality = 5
     charachterStats.dexterity = 4
     charachterStats.int = 10
     charachterStats.faith = 7
elif(player_class.upper() == 'ARCHER'):
     charachterStats.strenght = 6
     charachterStats.vitality = 5
     charachterStats.dexterity = 10
     charachterStats.int = 6
     charachterStats.faith = 3
elif(player_class.upper() == 'HEALER'):
     charachterStats.strenght = 4
     charachterStats.vitality = 5
     charachterStats.dexterity = 4
     charachterStats.int = 7
     charachterStats.faith = 10

print('\nYour story begins in a small town...')
time.sleep(1)
print(f'Your name is {player_name}, you are just a small boy in a big world')
time.sleep(1)
print('When you just turned 18 you set out into the world')
time.sleep(1)
print('You find a Dungeon and decide to step inside')
time.sleep(1)
door = input('Before you there are two doors, a red one and a blue one, wich one do you choose to open?\n > ')
checkDoor = 0
while(checkDoor == 0):
     if(door == 'blue' or door == 'red'):
          checkDoor=1
     else:
          door = input('Please choose between blue or red > ')
if(door == 'blue'):
     print('You won the game')
elif(door == 'red'):
     print('You lost the game')


     