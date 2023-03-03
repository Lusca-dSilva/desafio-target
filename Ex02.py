def fibonacci(num):
    x, y = 0, 1
    while y < num:
        x, y = y, x + y
    if y == num:
        return True
    else:
        return False

num = int(input("Digite um número: "))

if fibonacci(num):
    print(f"O número {num} está na sequência de Fibonacci.")
else:
    print(f"O número {num} não está na sequência de Fibonacci.")