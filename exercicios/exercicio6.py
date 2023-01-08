print("Digite uuma sequência de números para realiar a soma,ao digitar zero a soma é finalizada.")

soma = 0
qtidadeNumerosParaSomar = int(input("Informe a quantidade de números a serem somados: "))
i = 0
while i < qtidadeNumerosParaSomar:
    numerosParaSomar = int(input("Digite o valor a ser somado: "))
    i = i + 1
    soma = soma + numerosParaSomar

print("A soma é: ", soma)