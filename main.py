import pyautogui as pg
import actions
import constants
import json
from pynput.keyboard import Listener
from pynput import keyboard
import threading
import time
import os
import time
pg.useImageNotFoundException(False)



def kill_monster(event_th):
    start_time = time.time()
    while actions.check_battle() == None:
            print('entrei no kill monster')
            if time.time() - start_time > constants.MAX_TIME_TO_IGNORE_MONSTER:
                print("Tempo limite atingido para matar monstros, seguindo em frente.")
                break
            if event_th.is_set():
                return
            print('Matando monstros')
            pg.press('space')
            pg.sleep(1)
            while pg.pixelMatchesColor(*constants.POSITION_TARGET, constants.POSITION_TARGET_COLOR, tolerance=10) or pg.pixelMatchesColor(*constants.POSITION_TARGET, constants.TARGET_COLOR_WHITE, tolerance=30):
                print('esperando monstro morrer')
                if event_th.is_set():
                    return
            print ('procurando outro monstro')  
            pg.sleep(0.7)
        # try:
                
                # while pg.pixelMatchesColor(*constants.POSITION_TARGET, expectedRGBColor=constants.POSITION_TARGET_COLOR, tolerance=0.75) or pg.pixelMatchesColor(*constants.POSITION_TARGET, expectedRGBColor=constants.TARGET_COLOR_WHITE, tolerance=0.75):
           #este estava comentado antes # while pg.locateOnScreen('C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/imgs/red_target.png', confidence=0.7, region=constants.REGION_BATTLE) != None:
            
                    # print('esperando o monstro morrer')
        # except pg.ImageNotFoundException:
        #     print("Imagem não encontrada, continuando...")

        # print('procurando outro monstro')
        # time.sleep(0.5)


# def get_loot():
#     drop = [constants.hatchet, constants.dwarven_shield, constants.steel_helmet, constants.soldier_helmet, constants.crossbow, constants.chain_armor, constants.axe, constants.studded_armor, constants.battle_axe]
#     loot = pg.locateAllOnScreen('./imgs/monster_dead.png', confidence =0.9, region=constants.REGION_LOOT)
#     for box in loot:
#         x, y = pg.center(box)
#         pg.moveTo(x, y)
#         pg.click(button="right", clicks=1)
#         pg.sleep(1)
#         bag = pg.locateOnScreen('./imgs/bag.png', confidence=0.9, region=(179, 424, 175, 612))
#         if bag:
#             x, y = pg.center(bag)
#             pg.moveTo(x, y)
#             pg.keyDown('shift')  # Segura a tecla Shift
#             pg.click(button="right")  # Clique com botão direito
#             pg.keyUp('shift')  # Solta a tecla Shift
#             pg.sleep(0.5)
#         for item in drop:
#             found_item = pg.locateOnScreen(item, confidence=0.8, region=(179, 424, 175, 612))
#             if found_item:
#                 drop_center = pg.center(found_item)
#                 pg.moveTo(drop_center)
#                 pg.dragTo(963, 478, duration=0.9)






def go_to_flags(path, wait):
    # try:
        # Corrige o uso do caminho 'path' para garantir que está correto
        flag = pg.locateOnScreen(path, confidence=0.8, region=constants.REGION_MAP_BATTLE)
        
        if flag:
            x, y = pg.center(flag)
            print(f"Movendo-se para a bandeira: {path}")
            pg.moveTo(x, y)
            pg.click(button="left")
            pg.moveTo(100, 100)
            while not check_player_position(path):
                print('esperando chegar na posição')
                if event_th.is_set():
                    return
                time.sleep(1)
            print('cheguei na posição')  
            return True  
            # time.sleep(wait)
        else:
            print(f"Bandeira {path} não encontrada com a confiança especificada.")
            


def check_player_position(target_flag_path, tolerance=20):
    # Localiza o jogador e a flag no mapa
    # player = pg.locateOnScreen('C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/imgs/point_player.PNG', confidence=0.6, region=constants.REGION_MAP_BATTLE)
    flag = pg.locateOnScreen(target_flag_path, confidence=0.8, region=constants.REGION_MAP_BATTLE)
    print(flag, 'path', target_flag_path)
    if flag:
        return False
    return True
        
 




def run():
    while True:
        with open(f'{constants.FOLDER_NAME}/infos.json', 'r') as file:
            data = json.loads(file.read())
        for item in data:
            if event_th.is_set():
                return
            kill_monster(event_th)
            if event_th.is_set():
                return
            pg.sleep(0.5)
            actions.get_loot(event_th)
            # if event_th.is_set():
            #     return
            # pg.sleep(1)
            # go_to_flags(item['path'], item['wait'])
            # if event_th.is_set():
            #     return
            # pg.sleep(1)
            # kill_monster()
            # if event_th.is_set():
            #         return
            # pg.sleep(1)
            # actions.get_loot()
            # if event_th.is_set():
            #         return
            # pg.sleep(1)
            # if check_player_position(target_flag_path=0):
            #     if event_th.is_set():
            #         return
            #     pg.sleep(1)    
            #     kill_monster()
            #     if event_th.is_set():
            #         return
            #     pg.sleep(1)
            #     actions.get_loot()
            #     pg.sleep(1)
            #     if event_th.is_set():
            #         return
            #     go_to_flags(item['path'], item['wait'])
            #     pg.sleep(1)
            #     if event_th.is_set():
            #         return

            # if go_to_flags(item['path'], item['wait']):
            #     pg.sleep(0.5)
            #     print('iniciando função kill monster')
            #     kill_monster()
            #     if event_th.is_set():
            #         return
            #     pg.sleep(1)
            #     actions.get_loot()
            #     if event_th.is_set():
            #         return
            #     go_to_flags(item['path'], item['wait'])
            #     if event_th.is_set():
            #         return
            # actions.eat_food()
            # actions.hole_down(item['down_hole'])
            # actions.hole_up(item['up_hole'], f'{constants.FOLDER_NAME}/anchor_floor_2.png', 430, 0)


def key_code(key):
    print('key ->', key)
    if key == keyboard.Key.esc:
        event_th.set()
        return False
    if key ==keyboard.Key.delete:
        th_run.start()
    


global event_th
event_th = threading.Event()
th_run = threading.Thread(target=run)

with Listener(on_press=key_code) as listener:
    listener.join()









