from datetime import datetime, timedelta

# TO DO:
# Mejorar la presentación de las opciones.
# Ponerle colores al texto.
# Ejecutable.

# Variable global
time_cache = []


# FUNCIONES:
# Inicia al programa
def inicio():
    entrada = input('Presiona 1 para empezar el contador: ')
    while (entrada != '1'):
        entrada = input('Intenta de nuevo, (presiona 1): ')
    if entrada == '1':
        start_timer()


# Inicia el contador
def start_timer():
    start_time = datetime.now().strftime('%H:%M:%S')
    entrada2 = input(
        '<CONTADOR EN MARCHA> \nPresiona 2 para detener el contador o 3 para pausar: ')
    while (entrada2 != '2' and entrada2 != '3'):
        entrada2 = input('Intenta de nuevo, (presiona 2 o 3): ')
    if entrada2 == '2':
        stop(start_time)
    elif entrada2 == '3':
        pause(start_time)


# Pausa el contador y da opciones para detener o continuar el contador.
def pause(s_time):
    pause_time = datetime.now().strftime('%H:%M:%S')
    elapsed_time = (datetime.strptime(pause_time, '%H:%M:%S')) - \
        (datetime.strptime(s_time, '%H:%M:%S'))
    entrada3 = input(
        '<CONTADOR PAUSADO> \nPresiona 4 para continuar el contador o 5 para detenerlo: ')
    while (entrada3 != '4' and entrada3 != '5'):
        entrada3 = input(
            'Presiona 4 para continuar el contador o 5 para detenerlo: ')
    if entrada3 == '4':
        resume(elapsed_time)
    elif entrada3 == '5':
        return print(f"DURACIÓN TOTAL: {elapsed_time}")


# Suma el e_time y empieza otro tiempo para sumar al tiempo final
# Guardar los fragmentos de tiempo en una lista para luego ser calculados en el tiempo final.
def resume(e_time):
    global time_cache
    resume_time = datetime.now().strftime('%H:%M:%S')
    time_cache.append(e_time)
    entrada4 = input(
        '<CONTADOR EN MARCHA> \nPresiona 6 para pausar el contador o 7 para detenerlo: ')
    while (entrada4 != '6' and entrada4 != '7'):
        entrada4 = input(
            'Presiona 6 para pausar el contador o 7 para detenerlo: ')
    if entrada4 == '6':
        pause(resume_time)
    elif entrada4 == '7':
        end_time = datetime.now().strftime('%H:%M:%S')
        elapsed_time2 = (datetime.strptime(end_time, '%H:%M:%S')
                         ) - (datetime.strptime(resume_time, '%H:%M:%S'))
        time_cache.append(elapsed_time2)
        # Suma las fracciones que se guardan en la lista time_cache mediante un forloop.
        t_time = timedelta()
        for i in time_cache:
            t_time += i
        return print(f"DURACIÓN TOTAL: {t_time}")


# Detiene el contador e imprime el tiempo
def stop(s_time):
    final_time = datetime.now().strftime('%H:%M:%S')
    duracion = (datetime.strptime(final_time, '%H:%M:%S')) - \
        (datetime.strptime(s_time, '%H:%M:%S'))
    return print(f"DURACIÓN TOTAL: {duracion}")


# Empieza aquí
inicio()
