a = b = c = d = e = f = g = h = i = "-"
winner = 0
print("\nplayer 1: X    Player 2:O")
print("Note:- Player 1 will get the 1st chance and if you perform any player performs any invalid \nmove then it will be considerd a foul and your chance will be given to next player \n")
print("Enter the following no to enter at that pirticular position")
print("\n",1 , 2, 3 , "\n" , 4 , 5 , 6 , "\n" , 7 ,8 , 9 )
print("\n",a , b , c , "\n" , d , e , f , "\n" , g , h , i )
nameP1 = input("player 1 name:-")
nameP2 = input("player 2 name:-")
while(winner == 0):
    player1 = int(input(str(nameP1) + " please make a move:"))
    if(player1 == 1 and a != "O"):
        a = "X"
    elif(player1 == 2 and b != "O"):
        b = "X"
    elif(player1 == 3 and c != "O"):
        c = "X"
    elif(player1 == 4 and d != "O"):
        d = "X"
    elif(player1 == 5 and e != "O"):
        e = "X"
    elif(player1 == 6 and f != "O"):
        f = "X"
    elif(player1 == 7 and g != "O"):
        g = "X"
    elif(player1 == 8 and h != "O"):
        h = "X"
    elif(player1 == 9 and i != "O"):
        i = "X"
    else:
        print("Invalid move it's a FOUL!!!!!!")
    print("\n",a , b , c , "\n" , d , e , f , "\n" , g , h , i )
    if(a==b==c=="X" or d==e==f=="X" or g==h==i=="X" or a==d==g=="X" or b==e==h=="X" or c==f==i=="X" or a==e==i=="X" or c==e==g=="X"):
        print("congratulations "+nameP1+" you won!!!!!!!!")
        break

    player2 = int(input(str(nameP2) + " please make a move:"))
    if(player2 == 1 and a != "O"):
        a = "O"
    elif(player2 == 2 and b != "X"):
        b = "O"
    elif(player2 == 3 and c != "X"):
        c = "O"
    elif(player2 == 4 and d != "X"):
        d = "O"
    elif(player2 == 5 and e != "X"):
        e = "O"
    elif(player2 == 6 and f != "X"):
        f = "O"
    elif(player2 == 7 and g != "X"):
        g = "O"
    elif(player2 == 8 and h != "X"):
        h = "O"
    elif(player2 == 9 and i != "X"):
        i = "O"
    else:
        print("Invalid move it's a FOUL!!!!!!")
    print("\n",a , b , c , "\n" , d , e , f , "\n" , g , h , i )

    if(a==b==c=="O" or d==e==f=="O" or g==h==i=="O" or a==d==g=="O" or b==e==h=="O" or c==f==i=="O" or a==e==i=="O" or c==e==g=="O"):
        print("congratulations "+nameP2+" you won!!!!!!!!")
        break