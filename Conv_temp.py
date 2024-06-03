class Weather_Machine:
# Adicionei o construtor e atributo
    def __init__(self, temperature):
        self.temperature = temperature

# Adicionei também o metodo de temperatura
    def get_weather(self, temperature):
        self.temperature = temperature

# Agora criei o Conversor de temperatura
def prog_conversion():
    print('-'*12, 'Programa de Conversão das Temperaturas', '-'*12,'\n')
    print('1) Converter de Celsius para Fahreinheit')
    print('2) Converter de Fahreinheit para Celsius\n')

def cel_fahr():
    C = int(input('Informe a Temperatura em Graus Celsius: '))
    F = C * (9/5) + 32
    print('Valor em Fahreinheit: {:.0f}°F\n'.format(F))
def fahr_cel():
    F = int(input('Informe a Temperatura em Graus Fahreinheit: '))
    C = (F - 32) * (5/9) 
    print('Valor em Celsius: {:.0f}°C\n'.format(C))

if __name__ == '__main__':
    prog_conversion()
    choice = input('Escolha o tipo de conversão: ')

if choice == '1':
        cel_fahr()

if choice == '2':        
        fahr_cel()
    

'''
    #Agora coloquei um Input para que o Usuario informe a temperatura
temperature = int(input('Informe em Celsius, Quantos graus está hoje?:  '))

#Utilizei o if para ele coordenar se estiver maior que 18 ou menor
if temperature >= 18 and temperature < 26:
  print("Será um dia de clima fresco, aproveite para ir ao parque 🌳")

#Fiz uma interação do programa com o Usuario, lhe dandos sugestões 
elif temperature >= 28 and temperature < 42:
  print("O clima ta perfeito para uma praia, mas não esqueça o protetor solar 🏖️")

elif temperature >= 42:
  print("!Danger! 😱, Não se esqueça de se hidratar bem e tome cuidado ao sair de casa 🔥")

else:
  print("Está frio lá fora, é bom levar um casaco 🥶")



weather_machine = Weather_Machine(temperature)
weather_machine.get_weather(23)
'''
