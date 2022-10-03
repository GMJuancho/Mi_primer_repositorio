#grupo a = marvel + nombre < m
#        = capcon + nombre > m
#grupo b = el resto

nombre = input('Ingresa tu nombre: ')
preferencia = input('Ingresa tu preferencia: Capcom o Marvel? (utiliza C para Capcom y M para Marvel): ')

if (preferencia == 'M' and nombre < 'M') or (preferencia == 'C' and nombre > 'N'):
    print('Sos grupo A')
else:
    print('Sos grupo B')