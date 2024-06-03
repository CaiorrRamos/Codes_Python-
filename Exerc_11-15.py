
#Exercicio 11 Guanabara Mundo 01 Python 
# Declarei as Variaveis
'''
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt 
print('Sua parede tem {}x{} e sua area mede {}m².\n'.format(larg, alt, area))

# Agora colocareis as variaveis para solucionar o problema 
tinta = area / 2
print('Para pintar esta parede, você preciará de {}l de tinta.\n'.format(tinta))

'''

# Exercicios 12 Guanabara Mundo 01 Python
'''
preço = float(input ('Informe o preço do produto: R$'))
desconto = int(input('Informe o Desconto recebido (Apenas numeros): '))
print('\n')
novo = preço - (preço * desconto/100)
print('O custo informado do produto é R${}, com o desconto de {}%, custará R${}.'.format(preço, desconto, novo))

'''
# Exercicio 13 Guanabara Mundo 01 Python
'''
salario = float(input('Informe o salário do funcionario: R$'))
aumento = int(input('Informe a porcentagem do aumento salarial (apenas numeros): '))

novo = salario + (salario * aumento/100)
print('Um funcionario que ganhava R${}, com o aumento de {}%, ganhará agora R${}'.format(salario, aumento, novo))

'''
# Exercicio 15 Guanabara Mundo 01 Python

dias = int(input('Quantos dias alugados?: ')) 
km = float(input('Quantos Kms foram rodados?:'))
pago = dias * km 
print('O total a pagar é R${}'.format(pago))