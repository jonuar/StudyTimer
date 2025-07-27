from datetime import datetime, timedelta
from colorama import Fore, init
import os
import csv

init(autoreset=True)


class StudySession:
    def __init__(self):
        self.start_time = datetime.now()
        self.time_cache = []

    def add_time(self, elapsed):
        self.time_cache.append(elapsed)

    def get_total_time(self):
        return sum(self.time_cache, timedelta())

    def get_start_time(self):
        return self.start_time

    def get_end_time(self):
        return datetime.now()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_title():
    clear_screen()
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
    session = StudySession()
    print(Fore.BLUE + f'<CONTADOR EN MARCHA> {session.start_time.strftime("%H:%M:%S")}')
    
    while True:
        option = get_input('Presiona 2 para detener o 3 para pausar:', ['2', '3'])
        if option == '2':
            stop_timer(session)
            break
        elif option == '3':
            pause_timer(session)
            break


def pause_timer(session):
    pause_time = datetime.now()
    elapsed = pause_time - session.get_start_time()
    session.add_time(elapsed)

    print(Fore.MAGENTA + '<CONTADOR PAUSADO>')
    option = get_input('Presiona 4 para continuar o 5 para detener:', ['4', '5'])
    if option == '4':
        resume_timer(session)
    else:
        show_total_time(session)


def resume_timer(session):
    resume_start = datetime.now()
    print(Fore.BLUE + '<CONTADOR EN MARCHA>')

    while True:
        option = get_input('Presiona 6 para pausar o 7 para detener:', ['6', '7'])
        if option == '6':
            pause_time = datetime.now()
            session.add_time(pause_time - resume_start)
            pause_timer(session)
            break
        elif option == '7':
            session.add_time(datetime.now() - resume_start)
            show_total_time(session)
            break


def stop_timer(session):
    end_time = session.get_end_time()
    elapsed = end_time - session.get_start_time()
    print(Fore.GREEN + f"_____DURACIÓN TOTAL: {format_duration(elapsed)}_____")
    confirmar_guardado(session.get_start_time(), end_time, elapsed)


def show_total_time(session):
    total = session.get_total_time()
    end_time = session.get_end_time()
    print(Fore.GREEN + f"_____DURACIÓN TOTAL: {format_duration(total)}_____")
    confirmar_guardado(session.get_start_time(), end_time, total)


def confirmar_guardado(start, end, duration):
    opcion = get_input(
        f"¿Deseas guardar esta sesión de estudio? Duración: {format_duration(duration)} (s/n):", ['s', 'n'])
    if opcion == 's':
        guardar_log(start, end, duration)
    else:
        print(Fore.YELLOW + '⏭ Sesión no guardada.')


def guardar_log(start, end, duration):
    carpeta = 'logs'
    archivo = os.path.join(carpeta, 'estudio_log.csv')
    os.makedirs(carpeta, exist_ok=True)

    try:
        nuevo = not os.path.exists(archivo)
        with open(archivo, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if nuevo:
                writer.writerow(['Fecha', 'Inicio', 'Fin', 'Duración'])
            writer.writerow([
                start.date(),
                start.strftime('%H:%M:%S'),
                end.strftime('%H:%M:%S'),
                format_duration(duration)
            ])
        print(Fore.CYAN + 'Sesión guardada en logs/estudio_log.csv')
    except Exception as e:
        print(Fore.RED + f"Error al guardar la sesión: {e}")


def mostrar_historial():
    archivo = 'logs/estudio_log.csv'
    if not os.path.exists(archivo):
        print(Fore.YELLOW + "No hay registros aún.")
        return

    print(Fore.CYAN + '\n=== HISTORIAL DE ESTUDIO ===')
    try:
        with open(archivo, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                print(' | '.join(row))
    except Exception as e:
        print(Fore.RED + f"Error al leer el historial: {e}")


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    return str(timedelta(seconds=total_seconds))


def main():
    print_title()
    while True:
        option = get_input(
            '1: Empezar  |  2: Ver historial  |  3: Salir  →', ['1', '2', '3'])
        if option == '1':
            start_timer()
        elif option == '2':
            mostrar_historial()
        elif option == '3':
            print(Fore.GREEN + "¡Hasta pronto!")
            break


if __name__ == "__main__":
    main()
