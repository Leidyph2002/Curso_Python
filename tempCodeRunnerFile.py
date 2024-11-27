print("------------------------------------------")
print("Dame un numero, no letras")
my_condition = int(input())

my_condition = 5 * 5

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")

print("Fin de programa")