import pyautogui as pg
import keyboard
import constants
import time
import actions
import os

def get_position_and_color():
    print('pressione h para pegar a posição + cor do pixel')
    keyboard.wait('h')
    x, y = pg.position()
    rgb = pg.screenshot().getpixel((x, y))
    print(f'x, y: ({x}, {y}) - rgb: {rgb}')



def get_loot():
    drop = [constants.hatchet, constants.dwarven_shield, constants.steel_helmet, constants.soldier_helmet, constants.crossbow, constants.chain_armor, constants.axe, constants.studded_armor, constants.battle_axe]
    loot = pg.locateAllOnScreen('./imgs/monster_dead.png', confidence =0.8, region=constants.REGION_LOOT)
    for box in loot:
        x, y = pg.center(box)
        pg.moveTo(x, y)
        pg.click(button="right")
        pg.sleep(0.5)
        bag = pg.locateOnScreen('./imgs/bag.png', confidence=0.8, region=(179, 424, 175, 612))
        if bag:
            x, y = pg.center(bag)
            pg.moveTo(x, y)
            pg.keyDown('shift')  # Segura a tecla Shift
            pg.click(button="right")  # Clique com botão direito
            pg.keyUp('shift')  # Solta a tecla Shift
            pg.sleep(0.5)
        for item in drop:
            found_item = pg.locateOnScreen(item, confidence=0.8, region=(179, 424, 175, 612))
            if found_item:
                drop_center = pg.center(found_item)
                pg.moveTo(drop_center)
                pg.dragTo(963, 478, duration=0.9)
        # item_hatchet = pg.locateOnScreen(constants.hatchet, confidence=0.8, region=(179, 424, 175, 612))
        # if item_hatchet:
        #     item_hatchet_center = pg.center(item_hatchet)
        #     pg.moveTo(item_hatchet_center)
        #     pg.dragTo(963, 478, duration=1)




def kill_monster():
    start_time = time.time()
    max_duration = 60  # Limite de 60 segundos, por exemplo
    
    while actions.check_battle() == None:
        print('entrei no kill monster')
        if time.time() - start_time > max_duration:
            print("Tempo limite atingido para matar monstros, seguindo em frente.")
            break
        print('Matando monstros')
        pg.press('space')  
        pg.sleep(0.3)
        try:
                
                while pg.pixelMatchesColor(*constants.POSITION_TARGET, expectedRGBColor=constants.POSITION_TARGET_COLOR, tolerance=0.75) or pg.pixelMatchesColor(*constants.POSITION_TARGET, expectedRGBColor=constants.TARGET_COLOR_WHITE, tolerance=0.75):
            # while pg.locateOnScreen('C:/Users/FGTEC/Desktop/Arquivos Python/bt_tb/imgs/red_target.png', confidence=0.7, region=constants.REGION_BATTLE) != None:
            
                    print('esperando o monstro morrer')
        except pg.ImageNotFoundException:
            print("Imagem não encontrada, continuando...")

        print('procurando outro monstro')
        time.sleep(0.5)


def click():
    pg.click(button='middle')

def get_loot_1():
    try:
        path = os.path.join(constants.FOLDER_NAME, 'dead_monsters')
        if not os.path.exists(path) or not os.listdir(path):
            return 
        for directory, _, files in os.walk(path):
            for file in files:
                box = pg.locateOnScreen(os.path.join(directory, file), confidence=0.9, region=constants.REGION_LOOT)
                if box:
                    x, y = pg.center(box)
                    pg.moveTo(x, y)
                    with pg.hold('ctrl'):
                        pg.click(button='right')


    except Exception as err:
        print(f'Não foi encotrado o diretório {path}', err)

keyboard.wait('h')
print(pg.locateOnScreen('imgs/sqm_empty.png', confidence=0.95, region=constants.POSITION_SQM_CHECK_LOOT))