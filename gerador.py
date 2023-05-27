import random



nove_digitos = ''

for i in range(9):
    nove_digitos += str(random.randint(0,9))

contador_regressivo_1 = 10

# Converte o digito para int e faz uma conta multiplicando cada digito por 10 e depois soma todos os resultados
resultado_1 = 0
for digito in nove_digitos:
    resultado_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -=1

''' Multiplica o resultado por 10 e pega o resto da divisão por 11.
    O resultado será o primeiro digito do CPF, caso o resultado seja maior ou igual a 9 o número será 0.
'''
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

# Obter o 2º digito do CPF #
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

# Converte o digito para int e faz uma conta multiplicando cada digito por 11 e depois soma todos os resultados
resultado_2 = 0
for digito in dez_digitos:
    resultado_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -=1

''' Multiplica o resultado por 10 e pega o resto da divisão por 11.
    O resultado será o primeiro digito do CPF, caso o resultado seja maior ou igual a 9 o número será 0.
'''
digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

print(f'{nove_digitos}{digito_1}{digito_2}')
