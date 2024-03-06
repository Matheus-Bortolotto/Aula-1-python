# nome = input("Diga o seu nome:")
# primeiro_numero = int(input(f"{nome}, diga o primeiro número:"))
# segundo_numero = int(input(f"{nome}, diga outro número:"))
# soma = primeiro_numero+segundo_numero
# print(f"A soma entre {primeiro_numero} e {segundo_numero} é {soma}")
# mult = primeiro_numero*segundo_numero
# print(f"A multiplicação entre {primeiro_numero} e {segundo_numero} é {mult}")
# sub = primeiro_numero-segundo_numero
# print(f"A subtração entre {primeiro_numero} e {segundo_numero} é{sub}")
# div = primeiro_numero/segundo_numero
# print(f"A divisão entre {primeiro_numero} e {segundo_numero} é{div}")

# frase = " 0"
# print(frase)
# frase = frase + " São Paulo"
# print(frase)
# frase = frase + " foi"
# print(frase)

# primeiro_numero = 2
# segundo_numero = 3
# a = primeiro_numero==segundo_numero
# print(f"A comparação {primeiro_numero}=={segundo_numero} da {a}")
# a = primeiro_numero>segundo_numero
# print(f"A comparação {primeiro_numero}>{segundo_numero} da {a}")
# a = primeiro_numero<segundo_numero
# print(f"A comparação {primeiro_numero}<{segundo_numero} da {a}")
# a = primeiro_numero!=segundo_numero
# print(f"A comparação {primeiro_numero}!={segundo_numero} da {a}")
# a = primeiro_numero>=segundo_numero
# print(f"A comparação {primeiro_numero}>={segundo_numero} da {a}")
# a = primeiro_numero<=segundo_numero
# print(f"A comparação {primeiro_numero}<={segundo_numero} da {a}")

# a = 2
# b = 3
# c = 4
# d = 5
# print(f"{a} > {b} or {c} > {d}, ou seja, {a>b} or {c>d} dá {a>b or c>d}")
# print(f"{a} > {b} or {c} < {d}, ou seja, {a>b} or {c<d} dá {a>b or c<d}")
# print(f"{a} != {b} or {c} == {d}, ou seja, {a!=b} or {c==d} dá {a!=b or c==d}")
# print(f"{a} < {b} or {c} < {d}, ou seja, {a<b} or {c<d} dá {a<b or c<d}")
# print()
# print(f"{a} > {b} and {c} > {d}, ou seja, {a>b} and {c>d} dá {a>b and c>d}")
# print(f"{a} > {b} and {c} < {d}, ou seja, {a>b} and {c<d} dá {a>b and c<d}")
# print(f"{a} !={b} and {c} == {d}, ou seja, {a!=b} and {c==d} dá {a!=b and c==d}")
# print(f"{a} < {b} and {c} < {d}, ou seja, {a<b} and {c<d} dá {a<b and c<d}")

# senha = input("Diga sua senha:")
# senha_correta = '1234'
# if senha == senha_correta:
#     print("Acertô Mizerávi")

# idoso = input("Você é idoso? ")
# cadeirante = input("Você é cadeirante ? ")
# if idoso == 'sim' or cadeirante == 'sim':
#     print("Pode estacionar")

# idade = int(input("Diga sua idade: "))
# if idade < 18:
#     print("Não pode beber, que feio !! Vou contar para sua mãe")
# else:
#     print("Pode beber")

# letra = input("Digite uma letra:")
# if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
#     print("isso é uma vogal")
# else:
#     print("Não é vogal")

salario = float(input("Digite o seu salario :"))
if salario <= 1903.98:
    aliquota = 0
elif salario <= 2826.65:
    aliquota = 7.5/100
elif salario <= 3751.05:
    aliquota = 15/100
elif salario <= 4664.68:
    aliquota = 22.5/100
else:
    aliquota = 27.5/100
desconto = aliquota*salario
salario = salario - desconto
print(f"Seu salário será de {salario}")
