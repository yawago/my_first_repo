Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================================ RESTART: Shell ================================
>>> print('Game "rock, paper, scissors"')
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