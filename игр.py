print('Game "rock, paper, scissors"')
print('enter weapon')
x="rock"
y="paper"
z="scissors"
p1=(input("player1= "))
p2=(input("player2= "))
s1=0
s2=0
if p1==x:
    if p2==x:
        print("Draw!")
    elif p2==y:
        print("player1 loss","player2 win!")
        s2+=1
    elif p2==z:
        print("player1 win!","player2 loss")
        s1+=1
elif p1==y:
    if p2==x:
        print("player1 win!","player2 loss")
        s1+=1
    elif p2==y:
        print("Draw!")
    elif p2==z:
        print("player1 loss","player2 win!")
        s2+=1
elif p1==z:
    if p2==x:
        print("player1 loss","player2 win!")
        s2+=1
    elif p2==y:
        print("player1 win!","player2 loss")
        s1+=1
    elif p2==z:
        print("Draw!")
print("Continue?")
answer=input()
while answer=="yes":
    print('enter weapon')
    p1=(input("player1= "))
    p2=(input("player2= "))
    if p1==x:
        if p2==x:
            print("Draw!")
        elif p2==y:
            print("player1 loss","player2 win!")
            s2+=1
        elif p2==z:
            print("player1 win!","player2 loss")
            s1+=1
    elif p1==y:
        if p2==x:
            print("player1 win!","player2 loss")
            s1+=1
        elif p2==y:
            print("Draw!")
        elif p2==z:
            print("player1 loss","player2 win!")
            s2+=1
    elif p1==z:
        if p2==x:
            print("player1 loss","player2 win!")
            s2+=1
        elif p2==y:
            print("player1 win!","player2 loss")
            s1+=1
        elif p2==z:
            print("Draw!")
    print("Continue?")
    answer=input()
print("i give up!")
print("player1= ",s1)
print("player2= ",s2)
