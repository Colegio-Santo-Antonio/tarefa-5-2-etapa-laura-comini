numero = input().strip()
digitos = [int(x) for x in numero]
soma_impares = sum(digitos[-1::-2])
pares = digitos[-2::-2]
soma_pares = 0
for d in pares:
    dobro = d * 2
    if dobro > 9:
        dobro -= 9
    soma_pares += dobro
soma_total = soma_impares + soma_pares
if soma_total % 10 == 0:
    print("Cartão válido")
else:
    print("Cartão inválido")
