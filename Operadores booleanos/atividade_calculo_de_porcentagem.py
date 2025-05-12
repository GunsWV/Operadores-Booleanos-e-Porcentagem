#Cálculo de Porcentagem de um Número.
#• O programa deve calcular e exibir o valor que corresponde a essa
# porcentagem do total. Exemplo: se o usuário digitar 200 como
#valor total e 15 como porcentagem, o programa deverá calcular
#que 15% de 200 é 30.
#• Exemplo de fórmula:
#valor_parte = valor_total * (porcentagem / 100)

#1. receber a variavel [float]
#2. receber a porcentagem [float]
#3. calcular a fórmula
#4. imprimir o resultado da fórmula

valor_total = float(input("insíra o valor total:"))

valor_porcentagem = float(input("insíra a porcentagem:"))

resultado = valor_total * (valor_porcentagem / 100)
print(resultado)
