kahani = ""
while True:
    data= input("Enter the Story:")
    if len(data)==0:
        print("The end!")
        break
    kahani += data +"\n"

print("The real story:")
print(kahani)

with open("file.txt","w")as file:
    file.write(kahani)