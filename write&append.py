user_input= input("Enetr the content of the file : ")
with open("output.txt","w") as file:
    file.write(user_input + "\n")
    print("Content added successfully in output.txt file ")


more_input= input("Enter more content in files :")
with open("output.txt","a") as file:
    file.write(more_input + "\n")
    print("content appended successfully in file")

print("The final content of the file is : ")
with open("output.txt","r") as file:
    final= file.read()
    print(final)
    file.close()


