#Construtor de Funções do conversor
def convert_measure(value, unit):

    conversion_forms = {
        'km': 1000,
        'hm': 100,
        'dam': 10,
        'dm': 0.1,
        'cm': 0.01,
        'mm': 0.001,

    }

    form = conversion_forms[unit]
    converted_value = value / form

    return converted_value

#Entrada de dados, O inicio do programa de conversão
print('-'*8, 'Bem -vindo ao conversor de Medidas', '-'*8)
m = float(input('---> Informe a distancia em metros: '))

#Conversão paras as unidades
km = convert_measure(m, 'km') 
hm = convert_measure(m, 'hm')
dam = convert_measure(m, 'dam')
dm = convert_measure(m, 'dm')
cm = convert_measure(m, 'cm')
mm = convert_measure(m, 'mm')
#Exibindo os resultados das Conversões

print( 'A distancia {}m = '.format(m))
print('-'*12)
print('{} km'.format(km))
print('{} hm'.format(hm))
print('{} dam'.format(dam))
print('{:.0f} dm'.format(dm))
print('{:.0f} cm'.format(cm))
print('{:.0f} mm'.format(mm))
print('-'*12)
print('Sua distncia foi convertida com seucesso ✔️\n')


