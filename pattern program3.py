n=int(input("enter the number of rows:"))

for i in range (1,n+1,2):
    spaces=(n-i)//2
    print("  " * spaces , end="")
    for j in range(1,i+1):
        print(i,end="")
    print()

for i in range (n-2,0,-2):
    spaces=(n-i)//2
    print(" " * spaces,end="")
    
    for j in range(1,i+1):
        print(j,end="")
    print()