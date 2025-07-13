# Temporizador de Estudio

Este proyecto es un **cronómetro de estudio** hecho con Python. Su propósito es ayudar a registrar cuánto tiempo dedicas al estudio, incluyendo pausas y reanudaciones.

## ¿Qué hace?

- Inicia un cronómetro.
- Permite pausar y reanudar el tiempo.
- Muestra la duración total al detenerse.
- Guarda los intervalos pausados.
- Usa colores en la consola para una mejor experiencia visual.
- Guarda cada sesión de estudio en un archivo CSV (`logs/estudio_log.csv`)
- Registra fecha, hora de inicio, fin y duración total

## Requisitos

Necesitas tener Python 3 instalado. Además, instala el paquete `colorama`:

```bash
pip install colorama
```

## ¿Cómo se usa?
```bash
python timer.py
```

###  Instrucciones:

- Presiona 1 para comenzar.

- Durante el conteo:
-- Presiona 2 para detener.
-- Presiona 3 para pausar.

- Si pausas:
-- Presiona 4 para continuar.
-- Presiona 5 para detener.

- Si reanudas:
-- Presiona 6 para pausar.
-- Presiona 7 para detener.