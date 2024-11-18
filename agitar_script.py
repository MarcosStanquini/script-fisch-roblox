import pyautogui
import cv2
import numpy as np
import time
from mover_erraticamente import mover_mouse_erraticamente  

caminho_template_agitar = "template_agitar.png"
caminho_template_varinha_selecionada = "selecionada_varinha.png"

def verificar_varinha_selecionada(caminho_template, confianca=0.8):
    screenshot = pyautogui.screenshot()
    tela = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    tela_gray = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(caminho_template, cv2.IMREAD_GRAYSCALE)

    resultado = cv2.matchTemplate(tela_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= confianca:
        print("Varinha selecionada detectada na tela.")
        return True
    else:
        print("Varinha não está selecionada.")
        return False

def segurar_e_soltar_monitorando_brilho(limite_topo=100, margem_erro=5, tempo_max=10):
    print("Iniciando detecção dinâmica da barra...")

    pyautogui.mouseDown()
    tempo_inicio = time.time()

    try:
        while True:
            screenshot = pyautogui.screenshot()
            tela = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

            tela_gray = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)

            _, threshold = cv2.threshold(tela_gray, 200, 255, cv2.THRESH_BINARY)

            contornos, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            barra_detectada = False

            for contorno in contornos:
                x, y, largura, altura = cv2.boundingRect(contorno)

                if largura > 50 and 10 < altura < 100:
                    barra_detectada = True
                    print(f"Barra detectada em ({x}, {y}) com largura {largura} e altura {altura}.")

                    if abs(y - limite_topo) <= margem_erro:
                        print(f"Topo atingiu o limite em {y}. Soltando o botão do mouse...")
                        pyautogui.mouseUp()
                        return True
                    else:
                        print(f"Topo atual: {y}. Ainda não atingiu o limite ({limite_topo}).")
            
            if not barra_detectada:
                print("Nenhuma barra detectada na tela. Verificando novamente...")

            if time.time() - tempo_inicio > tempo_max:
                print("Tempo limite atingido. Soltando o botão e encerrando a função.")
                pyautogui.mouseUp()
                return False

            time.sleep(0.1)

    finally:
        pyautogui.mouseUp()

def mover_mouse_para_botao_e_clicar(caminho_template, confianca=0.8):
    screenshot = pyautogui.screenshot()
    tela = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    tela_gray = cv2.cvtColor(tela, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(caminho_template, cv2.IMREAD_GRAYSCALE)

    resultado = cv2.matchTemplate(tela_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resultado)

    if max_val >= confianca:
        template_altura, template_largura = template.shape
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
    try:
        print("Iniciando o script...")

        print("Verificando se a varinha está selecionada...")
        while not verificar_varinha_selecionada(caminho_template_varinha_selecionada):
            print("Aguardando a seleção da varinha...")
            time.sleep(1)

        print("Varinha selecionada! Passando para o carregamento.")

        carregamento_concluido = segurar_e_soltar_monitorando_brilho(
            limite_topo=100, margem_erro=5
        )
        if carregamento_concluido:
            print("Carregamento completo! Buscando o botão 'Agitar'...")

        tempo_inicio = time.time()
        while time.time() - tempo_inicio <= 3:
            encontrado = mover_mouse_para_botao_e_clicar(caminho_template_agitar)
            if encontrado:
                print("Botão 'Agitar' encontrado e clicado. Continuando busca...")
                time.sleep(0.5)
            else:
                print("Botão 'Agitar' não encontrado durante busca inicial. Tentando novamente...")

        while True:
            encontrado = mover_mouse_para_botao_e_clicar(caminho_template_agitar)
            if encontrado:
                print("Botão 'Agitar' encontrado e clicado. Aguardando para verificar novamente...")
                time.sleep(0.5)
            else:
                print("Botão 'Agitar' não encontrado. Aguardando 20 segundos antes de reiniciar...")
                time.sleep(20)
                print("Reiniciando o script para buscar o botão 'Agitar' novamente...")
                break

    except KeyboardInterrupt:
        print("\nScript interrompido pelo usuário. Saindo...")
    except Exception as e:
        print(f"Erro inesperado: {e}")
    finally:
        print("Encerrando o script.")

if __name__ == "__main__":
    while True:
        main()