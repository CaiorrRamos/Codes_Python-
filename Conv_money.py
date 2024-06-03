class Money_machine:
#Adicionei o Construtor e o atributo
    def __init__(self, money):
        self.money = money

#adicionei o metodo para que o usuario possa inserir o valor
    def get_money(self, money):
        self.money = money 

#Criei o Programa de Conversão Para o Usuario poder escolher
def money_conversion():
    print('-'*12,'Programa de Convesão de Moedas','-'*12,'\n')
    print('1) Conversão de Real(R$) para Dolar(US$)')
    print('2) Conversão de Dolar(US$) para Real(R$)')
    print('3) Conversão de Real(R$) para Yuan(¥)')
    print('4) Conversão de Yuan(¥) para Real(R$)\n')

#Criei a função para que o usuário escolha a opção desejada, já com os calculos das coonversões
def R_D():
    R = float(input('Quantos Reais deseja converter: R$'))
    D = R / 5.20
    print('Com R${} você pode comprar US${:.2f} '.format(R, D)) 

def D_R():
    D = float(input('Quantos Dolares deseja converter: US$'))
    R = D * 5.20
    print('Com US${} você pode comprar R${:.2f} '.format(D, R))

def R_Y():
    R = float(input('Quantos Reais deseja converter: R$'))
    Y = R / 0.71
    print('Com R${} você pode comprar ¥{:.2F} '.format(R, Y))

def Y_R():
    Y = float(input('Quantos Yuans deseja converter: ¥'))
    R = Y * 0.71
    print('Com ¥{} você pode comprar R${:.2f} '.format(Y, R))

#Aqui adicionei o padrão de escolha para que o Usuario selecione a conversão desejada
if __name__ == '__main__':
    money_conversion()
    choice = input(' Qual conversão deseja realizar: ')

if choice == '1':
    R_D()

if choice == '2':
    D_R()

if choice == '3':
    R_Y()

if choice == '4':
    Y_R()



