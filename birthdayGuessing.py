d=0
print("Is your birthday in set 1")
print("1 3 5 7\n9 11 13 15\n17 19 21 23\n25 27 29 31\n PRESS 1 FOR YES AND 0 FOR NO")
n=input("?")
if(int(n)==1):
    d+=1
print("Is your birthday in set 2")
print("2 3 6 7\n10 11 14 15\n18 19 22 23\n26 27 30 31\n PRESS 1 FOR YES AND 0 FOR NO")
n=input("?")
if(int(n)==1):
    d+=2
print("Is your birthday in set 3")
print("4 5 6 7\n12 13 14 15\n20 21 22 23\n28 29 30 31\n PRESS 1 FOR YES AND 0 FOR NO")
n=input("?")
if(int(n)==1):
    d+=4
print("Is your birthday in set 4")
print("8 9 10 11\n12 13 14 15\n24 25 26 27\n28 29 30 31\n PRESS 1 FOR YES AND 0 FOR NO")
n=input("?")
if(int(n)==1):
    d+=8
print("Is your birthday in set 5")
print("16 17 18 19\n20 21 22 23\n24 25 26 27\n28 29 30 31\n PRESS 1 FOR YES AND 0 FOR NO")
n=input("?")
if(int(n)==1):
    d+=16
print("Your birthday is:")
print(d)