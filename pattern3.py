n=int(input("Enter the number of rows: "))
i=1
for i in range(1,n+1,+1):
    output=""
    for j in range(1,i+1):
        output+=str(j)+" "
    print(output)
    i+=1
    