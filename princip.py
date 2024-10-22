import pyautogui as pg
import actions
import constants
import json
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import time
import math
import time




def get_loot():
    loot = pg.locateAllOnScreen('imgs/monster_dead.PNG', confidence=0.7, region=constants.REGION_LOOT)
    for box in loot:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click(button='right')



def hole_down():
    box = pg.locateOnScreen('imgs/hole_down.png', confidence=0.8)
    if box:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click()
        pg.sleep(5)


def hole_up(img_anchor):
    box = pg.locateOnScreen(img_anchor, confidence=0.8)
    if box:
        x, y = pg.center(box)
        pg.moveTo(x + 130, y + 130, 3)




   #     # Calcula a distância euclidiana entre o jogador e a flag
    #     distance = math.sqrt((player_x - flag_x) ** 2 + (player_y - flag_y) ** 2)
        
    #     print(f"Distância do jogador até a bandeira: {distance}")
        
    #     # Verifica se a distância é menor que a tolerância
    #     if distance <= tolerance:
    #         print("Jogador está próximo o suficiente da bandeira.")
    #         return True
    #     else:
    #         print("Jogador está longe da bandeira.")
    #         return False
    # else:
    #     print("Jogador ou bandeira não encontrados.")
    #     return False



    # def get_loot():
    # last_loot_position = None  # Armazena a última posição de loot clicada
    
    # try:
    #     # Tenta localizar o loot na tela com a confiança especificada
    #     loot = list(pg.locateAllOnScreen('C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/imgs/monster_dead.png', confidence=0.6, region=constants.REGION_LOOT))
        
    #     if loot:
    #         print(f"Monstros mortos encontrados: {len(loot)}")
        
    #     # Itera sobre os itens de loot encontrados
    #     for box in loot:
    #         x, y = pg.center(box)
            
    #         # Verifica se a posição atual está dentro da caixa do último monstro morto
    #         if last_loot_position and is_within_box(last_loot_position[0], last_loot_position[1], x, y):
    #             print(f"Monstro já looteado próximo à posição ({x}, {y}), ignorando clique.")
    #             continue  # Ignora cliques repetidos dentro da área da box
            
    #         if event_th.is_set():
    #             return  # Sai da função se o evento for acionado

    #         print(f"Clicando no monstro morto na posição ({x}, {y})")
    #         pg.moveTo(x, y)
    #         pg.click(button="right")  # Clica com o botão direito para coletar loot
            
    #         last_loot_position = (x, y)  # Armazena a última posição clicada
            
    #         time.sleep(1)  # Aguarda um momento para evitar cliques repetidos
            
    # except pg.ImageNotFoundException:
    #     print("Imagem de loot não encontrada, continuando...")
    
    # except Exception as e:
    #     print(f"Erro inesperado: {e}, continuando...")


# def go_to_flag(path, wait):
#     flag = pg.locateOnScreen(path, confidence=0.9, region=constants.REGION_MAP_BATTLE)
#     if flag:
#         x, y=pg.center(flag)
#         if event_th.is_set():
#             return
#         pg.moveTo(x, y)
#         pg.click()
#         pg.sleep(wait)

# def check_player_position():
#     return pg.locateOnScreen('C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/imgs/point_player.PNG', confidence=0.3, region=constants.REGION_MAP_BATTLE)


#gepeto def run
# def run():
#     base_path = "C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/vasp_ab"
#     num_flags = 3  # Quantidade de bandeiras para seguir
#     wait = 12  # Tempo de espera entre cliques
    
#     # Loop principal de execução
#     while not event_th.is_set():
#         for i in range(num_flags):
#             # Corrigindo o caminho da imagem
#             flag_path = f"{base_path}/flag_{i}.png"
            
#             # 1. Vai para a bandeira atual
#             print(f"Indo para a bandeira {i+1}: {flag_path}")
#             go_to_flags(flag_path, num_flags, wait)  # Passa o caminho correto da bandeira
            
#             # 2. Tenta matar monstros após chegar à bandeira
#             print(f"Jogador chegou à bandeira {i+1}, tentando matar monstros.")
#             start_time = time.time()
            
#             # Limitar o tempo que ele tenta matar monstros (20 segundos, por exemplo)
#             while time.time() - start_time < 20:
#                 kill_monster()  # Tenta matar os monstros
#                 if event_th.is_set():
#                     return
            
#             # Sai do loop de matar monstros e continua
#             print(f"Término do tempo para matar monstros na bandeira {i+1}.")
            
#             # 3. Pega o loot após matar os monstros
#             print(f"Pegando loot na bandeira {i+1}.")
#             time.sleep(1)  # Aguarda antes de pegar loot
#             get_loot()
#             if event_th.is_set():
#                 return
            
#             # 4. Espera antes de ir para a próxima bandeira
#             print(f"Esperando {wait} segundos antes de ir para a próxima bandeira.")
#             time.sleep(wait)
            
#             if event_th.is_set():
#                 return

#         # 5. Quando chegar à última bandeira, volta para a primeira e reinicia o ciclo
#         print("Ciclo completo, voltando para a primeira bandeira.")




#def run nova feita com a ajuda do gepeto e funcionando o clique
# def run():
#     base_path = "C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/vasp_ab"
#     num_flags = 3  # Quantidade de bandeiras para seguir
#     wait = 12  # Tempo de espera entre cliques
    
#     # Loop principal de execução
#     while not event_th.is_set():
#         for i in range(num_flags):
#             # Corrigindo o caminho da imagem
#             flag_path = f"{base_path}/flag_{i}.png"
            
#             # 1. Vai para a bandeira atual
#             print(f"Indo para a bandeira {i+1}: {flag_path}")
#             go_to_flags(flag_path, num_flags, wait)  # Passa o caminho correto da bandeira
            
#             # 2. Tenta matar monstros após chegar à bandeira
#             print(f"Jogador chegou à bandeira {i+1}, tentando matar monstros.")
#             start_time = time.time()
#             while time.time() - start_time < 20:
#                 kill_monster()  # Tenta matar os monstros
#                 if event_th.is_set():
#                     return
            
#             # 3. Pega o loot após matar os monstros
#             print(f"Pegando loot na bandeira {i+1}.")
#             time.sleep(1)  # Aguarda antes de pegar loot
#             get_loot()
#             if event_th.is_set():
#                 return
            
#             # 4. Espera antes de ir para a próxima bandeira
#             print(f"Esperando {wait} segundos antes de ir para a próxima bandeira.")
#             time.sleep(wait)
            
#             if event_th.is_set():
#                 return

#         # 5. Quando chegar à última bandeira, volta para a primeira e reinicia o ciclo
#         print("Ciclo completo, voltando para a primeira bandeira.")



# def is_within_box(x1, y1, x2, y2, box_width=78, box_height=81):
#     """Verifica se duas posições estão dentro da área da caixa do monstro morto"""
#     return abs(x2 - x1) <= box_width / 2 and abs(y2 - y1) <= box_height / 2


#codigo gepeto def loot
# def get_loot():
#     loot = pg.locateAllOnScreen('C:/Users/FGTEC/Desktop/bt_tb/imgs/monster_dead.png', confidence=0.7, region=constants.REGION_LOOT)
#     for box in loot:
#         x, y = pg.center(box)
#         if event_th.is_set():
#             return
#         pg.moveTo(x, y)
#         pg.click(button="right")
        
#         # Verificando e arrastando o item X
#         item_x = pg.locateOnScreen('C:/Users/FGTEC/Desktop/bt_tb/imgs/item_x.png', confidence=0.7, region=(179, 424, 175, 612))
#         if item_x:
#             item_x_center = pg.center(item_x)
#             pg.moveTo(item_x_center)
#             pg.dragTo(963, 478, duration=0.5)
        
#         # Verificando e arrastando o item Y
#         item_y = pg.locateOnScreen('C:/Users/FGTEC/Desktop/bt_tb/imgs/item_y.png', confidence=0.7, region=(179, 424, 175, 612))
#         if item_y:
#             item_y_center = pg.center(item_y)
#             pg.moveTo(item_y_center)
#             pg.dragTo(963, 478, duration=0.5)
        
#         # Verificando e arrastando o item Z
#         item_z = pg.locateOnScreen('C:/Users/FGTEC/Desktop/bt_tb/imgs/item_z.png', confidence=0.7, region=(179, 424, 175, 612))
#         if item_z:
#             item_z_center = pg.center(item_z)
#             pg.moveTo(item_z_center)
#             pg.dragTo(963, 478, duration=0.5)
        
#         # Verificando e arrastando o item G
#         item_g = pg.locateOnScreen('C:/Users/FGTEC/Desktop/bt_tb/imgs/item_g.png', confidence=0.7, region=(179, 424, 175, 612))
#         if item_g:
#             item_g_center = pg.center(item_g)
#             pg.moveTo(item_g_center)
#             pg.dragTo(1841, 381, duration=0.5)

