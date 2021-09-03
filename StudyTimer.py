from datetime import datetime
import time
import tkinter

entrada = input('Presiona 1 para empezar el contador: ')
while (entrada != '1'):
    entrada = input('Intenta de nuevo, (presiona 1): ')
if entrada == '1':
    start_time = datetime.now().strftime('%H:%M:%S')

entrada2 = input(
    '<CONTADOR EN MARCHA> \nPresiona 2 para detener el contador: ')
while (entrada2 != '2'):
    entrada2 = input('Para detener el contador presiona 2: ')
if entrada2 == '2':
    final_time = datetime.now().strftime('%H:%M:%S')


duracion = (datetime.strptime(final_time, '%H:%M:%S')) - \
    (datetime.strptime(start_time, '%H:%M:%S'))

print(f"Duración total: {duracion}")
