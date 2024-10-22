import pyautogui as pg
import constants
import keyboard


def get_loot():
    try:
        # Tenta localizar o loot na tela com a confiança especificada
        loot = pg.locateAllOnScreen('C:\\Users\\FGTEC\\Desktop\\Arquivos python\\bt_tb\\imgs\\monster_dead.PNG', confidence=0.6, region=constants.REGION_LOOT)
        
        # Itera sobre os itens de loot encontrados
        for box in loot:
            x, y = pg.center(box)
            #if event_th.is_set():
            #    return  # Sai da função se o evento for acionado
            pg.moveTo(x, y)
            pg.click(button="right")
    
    # Tratamento de exceção para evitar que o código pare ao não encontrar a imagem
    except pg.ImageNotFoundException:
        print("Imagem de loot não encontrada, continuando...")
    
    except Exception as e:
        print(f"Erro inesperado: {e}, continuando...")




while True:
    print(pg.locateOnScreen('C:\\Users\\FGTEC\\Desktop\\Arquivos python\\bt_tb\\imgs\\well.PNG', confidence=0.8))
