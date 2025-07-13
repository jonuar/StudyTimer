from datetime import datetime, timedelta
from colorama import Fore, Style, init
import os
import csv

# TO DO:
# GUI
# Ejecutable.

# Variable global
time_cache = []
start_global = None

# Inicializa colorama
init(autoreset=True)


def print_title():
    print(Fore.CYAN + '^' * 70)
    print(Fore.GREEN + 'HOLA, TE AYUDARÉ A REGISTRAR TU TIEMPO DE ESTUDIO.')
    print(Fore.CYAN + '^' * 70)

def get_input(prompt, valid_options):
    while True:
        choice = input(Fore.YELLOW + prompt + ' ')
        if choice in valid_options:
            return choice
        print(Fore.RED + 'Opción no válida. Intenta de nuevo.')

def start_timer():
    global start_global
    start_global = datetime.now()
    print(Fore.BLUE + '<CONTADOR EN MARCHA>')
    
    while True:
        option = get_input('Presiona 2 para detener o 3 para pausar:', ['2', '3'])
        if option == '2':
            stop_timer(start_global)
            break
        elif option == '3':
            pause_timer(start_global)
            break

def pause_timer(start_time):
    pause_time = datetime.now()
    elapsed = pause_time - start_time
    time_cache.append(elapsed)

    print(Fore.MAGENTA + '<CONTADOR PAUSADO>')

    option = get_input('Presiona 4 para continuar o 5 para detener:', ['4', '5'])
    if option == '4':
        resume_timer()
    else:
        show_total_time()

def resume_timer():
    resume_start = datetime.now()
    print(Fore.BLUE + '<CONTADOR EN MARCHA>')

    while True:
        option = get_input('Presiona 6 para pausar o 7 para detener:', ['6', '7'])
        if option == '6':
            pause_timer(resume_start)
            break
        elif option == '7':
            end_time = datetime.now()
            elapsed = end_time - resume_start
            time_cache.append(elapsed)
            show_total_time()
            break

def stop_timer(start_time):
    end_time = datetime.now()
    elapsed = end_time - start_time
    print(Fore.GREEN + f"_____DURACIÓN TOTAL: {elapsed}_____")
    confirmar_guardado(start_time, end_time, elapsed)

def show_total_time():
    global start_global
    end_time = datetime.now()
    total = sum(time_cache, timedelta())
    print(Fore.GREEN + f"_____DURACIÓN TOTAL: {total}_____")
    confirmar_guardado(start_global, end_time, total)

def guardar_log(start, end, duration):
    carpeta = 'logs'
    archivo = os.path.join(carpeta, 'estudio_log.csv')
    os.makedirs(carpeta, exist_ok=True)

    nuevo = not os.path.exists(archivo)
    with open(archivo, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if nuevo:
            writer.writerow(['Fecha', 'Inicio', 'Fin', 'Duración'])
        writer.writerow([
            start.date(),
            start.strftime('%H:%M:%S'),
            end.strftime('%H:%M:%S'),
            str(duration)
        ])
    print(Fore.CYAN + '✅ Sesión guardada en logs/estudio_log.csv')

def confirmar_guardado(start, end, duration):
    opcion = get_input(
        f"¿Deseas guardar esta sesión de estudio? Duración: {duration} (s/n):", ['s', 'n'])
    while True:
        if opcion == 's':
            guardar_log(start, end, duration)
            break
        elif opcion == 'n':
            print(Fore.YELLOW + '⏭ Sesión no guardada.')
            break
        else:
            opcion = input(Fore.YELLOW + '¿Deseas guardar esta sesión de estudio? (s/n): ').lower()


def main():
    print_title()
    get_input('Presiona 1 para empezar el contador:', ['1'])
    start_timer()

if __name__ == "__main__":
    main()