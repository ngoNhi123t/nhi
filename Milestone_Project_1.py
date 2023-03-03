#Tic Tac Toe game

#khởi tạo
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
### hiển thị 
def display_board(row1, row2, row3):
    print("Here is present board !")
    # print(row1)
    # print(row2)
    # print(row3)
    print('   |   |')
    print(' ' + row1[0] + ' | ' + row1[1] + ' | ' + row1[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + row2[0] + ' | ' + row2[1] + ' | ' + row2[2])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + row3[0] + ' | ' + row3[1] + ' | ' + row3[2])
    print('   |   |')


## chọn vị trí
#chọn hàng
def row_choice():
    choice = 'wrong'
    #check xem có pải digit ko, có thuộc 1,2,3
    while choice not in ['1','2','3']:
        choice= input("choose the row you want to tick: ")
        if choice not in ['1','2','3']:
            print('Error: please enter a num(1,2,3)!!!')
    return int(choice)
# print(row_choice())
#chọn index trong hàng
def position_choice():
    choice='wrong'
    ## kiểm tra đk: [0,1,2]
    while choice not in ['0','1','2']:
        choice = input("choose your position : ")
        if choice not in ['0','1','2']:
            print("Error: Please enter a num(0,1,2!!!)")
    return int(choice)
# chọn kí tự cần thay đổi : X or O
def choice_letter():
    letter = ' wrong'
    while letter not in ['X', 'O']:
        letter = input("Player 1 choose your letter : ")
        if letter not in ['X','O']:
            print("choose letter X or O")
    return letter
# print(choice_letter())
def display_letter(letter):
    if letter =='X':
       print("Player 1 : 'X' \nPlayer2: 'O' \n Let's start play game")
    elif letter =='O':
       print("Player 1 : 'O' \nPlayer2: 'X' \n Let's start play game")
# print(position_choice())
def changed_board(row, position, letter):
    if row ==1:
        row1[position]= letter
        # return row1
    elif row ==2:
        row2[position] = letter
        # return row2
    elif row ==3:
        row3[position] = letter
        # return row3
    return display_board(row1, row2, row3)
    
## điều kiện win
def win(letter, row1,row2,row3):
    add = False
    if row1[0]==row1[1]==letter and row1[0]==row1[2]==letter or row2[0]==row2[1]==letter and row2[0]==row2[2]==letter or row3[0]==row3[1]==letter and row3[0]==row3[2]==letter or row1[0] == row2[0]==letter and row1[0]==row3[0]==letter or row1[1] == row2[1]==letter and row1[1]==row3[1]==letter or row1[2] == row2[2]==letter and row1[2]==row3[2]==letter or row1[0]==row2[1]==letter and row2[1]==row3[2]==letter or row1[2]==row2[1]==letter and row2[1]==row3[0]==letter :
        print(f'WInner is player with {letter}')
        add = True
    else:
        if letter =='X':
            print(f' player2: Your turn!!!')
        if letter =='O':
            print(f'Player1: your turn!!!')
        add = False
    return add
# row1=[' ',' ',' ']
# row2=[' ',' ',' ']
# row3=[' ',' ',' ']
# print(win('M',row1,row2,row3))
def turn_play(letter):
    
    row=row_choice()
    position=position_choice()
    changed_board(row, position, letter)
def changed_player(letter):   
    if letter =='X':
      letter ='O'
    elif letter =='O':
     letter ='X'
    return letter
# print(changed_player('X'))
def gameon_choice():
    #khởi tạo giá trị ban đầu
    choice ='wrong'
    #vòng lặp 
    while choice not in ['Y','N']:
        #ko nên bỏ qua mà nên báo lỗi Error
        choice = input("Would you like to keep playing? Y or N ")
        if choice not in ['Y','N']:
            print("sorry, I didn't understand. Please make sure to choose Y or N.")
    if choice =='Y':
        # game is on
        return True
    else:
        #game is over
        return False
    
    
### FINALLY
game_on = True
row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']
while game_on:
    display_board(row1, row2, row3)
    letter =choice_letter()
    display_letter(letter)
    turn_play(letter)
    rel=False
    while rel ==False:
        letter =changed_player(letter)
        turn_play(letter)
        rel = win(letter, row1,row2,row3)
    
    game_on= gameon_choice()
    row1=[' ',' ',' ']
    row2=[' ',' ',' ']
    row3=[' ',' ',' ']
        
    
    