def charCreation():
     check_player = 1
     check_class = 1
     while(check_player==1):
          player_name = input("Please tell us your name > ")
          if (input(f'Is your name {player_name} > ') == 'yes'):
               check_player=0
     while(check_class==1):
          classes=['KNIGHT', "ARCHER", "MAGE", "HEALER"]
          print(f'{classes}')
          player_class = input("Please choose your class > ") 
          if(player_class.upper() in classes ):
               if(input(f'Is your classe {player_class} > ') == 'yes'):
                    check_class=0
     return player_class, player_name
