try:
    with open("simples.text", "r") as file:
        content= file.read()
        print("File content : ")
        print(content)
        file.close()

except FileExistsError:
    print("File not found please check the path")

