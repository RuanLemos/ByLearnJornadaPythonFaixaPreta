#esse código é a resolução do nível 1 do projecteuler.net. Considero o site como uma boa forma de afiar a lógica nas linguagens de programação, bem como um desafio que me auxilia a aprender mais

#declarando variáveis de valor máximo e mínimo
valor_minimo = int(input("Manda o valor mínimo aí: "))
valor_maximo = int(input("Manda o valor máximo aí: "))

#criação da função
def verificacao(valor_minimo, valor_maximo):
    #declarando variável soma
    soma = 0
    for numero in range(valor_minimo, valor_maximo + 1):
        #verificando se os números são divisíveis por 3 e 5 ou não
        if numero % 3 == 0 or numero % 5 == 0:
            #somando múltiplos de 3 e 5
            soma += numero
    return soma

print('A soma dos múltiplos de 3 e 5 entre', valor_minimo, 'e', valor_maximo, 'é de', verificacao(valor_minimo, valor_maximo))
