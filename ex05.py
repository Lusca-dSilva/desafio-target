string = input("Informe uma string: ")

inverso = ""
for i in range(len(string)-1, -1, -1):
    inverso += string[i]

print(f"A string invertida é: {inverso}")