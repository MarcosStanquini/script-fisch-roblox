import pyautogui
import random
import time

def mover_mouse_erraticamente(duracao=2, amplitude=15):

    x_inicial, y_inicial = pyautogui.position()
    tempo_fim = time.time() + duracao

    while time.time() < tempo_fim:
        x_novo = x_inicial + random.randint(-amplitude, amplitude)
        y_novo = y_inicial + random.randint(-amplitude, amplitude)
        pyautogui.moveTo(x_novo, y_novo, duration=0.1)
        time.sleep(random.uniform(0.05, 0.2))

    print("Movimento errático concluído.")