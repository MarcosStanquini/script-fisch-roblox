import pyautogui
import cv2
import numpy as np
import time
from mover_erraticamente import mover_mouse_erraticamente  


caminho_template_agitar = "template_agitar.png"

def mover_mouse_para_botao_e_clicar(caminho_template, confianca=0.8):
    screenshot = pyautogui.screenshot()
    tela = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(caminho_template, cv2.IMREAD_UNCHANGED)
    resultado = cv2.matchTemplate(tela, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= confianca:
        template_altura, template_largura, _ = template.shape
        posicao_x, posicao_y = max_loc
        centro_x = posicao_x + template_largura // 2
        centro_y = posicao_y + template_altura // 2

 
        pyautogui.moveTo(centro_x, centro_y, duration=0.2)
        time.sleep(0.2)

  
        mover_mouse_erraticamente(duracao=1, amplitude=10)  

    
        pyautogui.click()
        print(f"Botão 'Agitar' encontrado e clicado em ({centro_x}, {centro_y})!")
        return True
    else:
        print("Botão 'Agitar' não encontrado na tela.")
        return False

def main():
    print("Iniciando a busca pelo botão 'Agitar'...")
    while True:
        encontrado = mover_mouse_para_botao_e_clicar(caminho_template_agitar)
        if encontrado:
            time.sleep(0.5)
        else:
            time.sleep(1)

if __name__ == "__main__":
    main()