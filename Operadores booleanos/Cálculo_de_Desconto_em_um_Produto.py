#Se o usuário informar que o preço original é 100 e o desconto é
#de 20%, o programa deverá calcular que o valor do desconto é 20
#e, consequentemente, o preço final será 80.

#Exemplo de fórmula:
#valor_desconto = preco_original * (porcentagem_desconto / 100)
#preco_final = preco_original - valor_desconto

Porcentagem_desconto = float(input("Insira o valor de desconto:"))

Preco_Original = float(input("Insira o preco original:"))

Resultado = Porcentagem_desconto = Preco_Original * (Porcentagem_desconto / 100)
print(f"O desconto foi de {Resultado}")
Preco_final = Preco_Original - Porcentagem_desconto
print(f"O preco final é {Preco_final}")
