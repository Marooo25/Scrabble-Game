# --- Header ---
# File: CS112_A1_T2_2_ 20230379

# Purpose:  This Game is played with Two Players and list of numbers between 1 and 9 
#           Each player takes turns picking a number from the list
#           Once a number has been picked,it cannot be picked again
#           If a player has picked three numbers that add up to 15 that player wins the game.

# Author: Marawan Ashraf Hanafy
# ID: 20230379




# --- Start Messages ---

print()
print('----- Welcome To Scrabble Game ----- \n')
print('** This Game is played with Two Players and list of numbers between 1 and 9 \n')
print('** Each player takes turns picking a number from the list.\n')
print('** Once a number has been picked,it cannot be picked again.\n   If a player has picked three numbers that add up to 15,\n   that player wins the game.\n')
print('** However, if all the numbers are used and no player gets exactly 15, the game is a draw.\n')
print('----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ' )
print() 


# --- Some Data ---
list_of_numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = 0
player2 = 0


# --- The Game ---
for i in range(0,3):

    # --- Player1 Round ---
    print()
    print('List of Numbers ==> ', list_of_numbers)
    player1_choise = int(input('Pleayer1..\nPlease Take Number From List\n  ==> '))
    
    if (1<= player1_choise <=9 and player1_choise in list_of_numbers):
        list_of_numbers.remove(player1_choise)
        player1 = player1 + player1_choise
    else:
        print('**Invaild Number..\n')
        print('List of Numbers ==> ', list_of_numbers)
        player1_choise = int(input('Pleayer1..\nPlease Take an Availble Number From List\n  ==> '))
        list_of_numbers.remove(player1_choise)

# --- Cheak If Player1 Win ---
    if(player1 == 15): 
        print()
        print('**Congratulations...\nPlayer1 is Winner..!')
        print()
        break

# --- Player2 Round ---
    print()
    print('List of Numbers ==> ', list_of_numbers)
    player2_choise = int(input('Player2..\nPlease Take Number From List\n  ==> '))
    if (1<= player2_choise <=9 and player2_choise in list_of_numbers):
        list_of_numbers.remove(player2_choise)
        player2 = player2 + player2_choise
    else:
        print('**Invaild Number..\n')
        print('List of Numbers ==> ', list_of_numbers)
        player1_choise = int(input('Pleayer1..\nPlease Take an Availble Number From List\n  ==> '))
        list_of_numbers.remove(player1_choise)

# --- Cheak If Player2 Win ---
    if(player2 == 15): 
        print()
        print('**Congratulations...\nPlayer2 is Winner..!')
        print()
        break
# --- Draw Condetion ---
if (player1 !=15 and player2 !=15):
    print()
    print('*** The Game End With Draw ***')

# --- Show Final Result --- 
print()
print('Additional Feature')
print('---------------------------------------')
print('Final Results is ')
print('player1 = ',player1)
print('player2 = ',player2)
print()
