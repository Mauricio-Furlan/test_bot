import pyautogui as pg
import constants
import os
pg.useImageNotFoundException(False)


def hold_click():
    with pg.hold('ctrl'):
        pg.click(button='right')

def check_bp():
    box = pg.locateOnScreen('imgs/backpack_loot.png', confidence=0.9, region=constants.BACKPACK_LOOT_POSITION_END)
    if box:
        pg.moveTo(*pg.center(box))
        hold_click()


def  collect_loot(event_th):
    for directory, _, files in os.walk(constants.LOOT_IMG_PATH):
        for file in files:
            path_img = os.path.join(directory, file)
            print('procurando pela imagem:', path_img)
            check_bp()
            if event_th.is_set():
                return
            box = pg.locateOnScreen(path_img, confidence=0.90, region=constants.POSITION_SQM_CHECK_LOOT)
            if box:
                pg.moveTo(*pg.center(box))
                pg.dragTo(*constants.CHAR_POSITION_CENTER)
                pg.sleep(0.5)
        check_bp()
        pg.sleep(0.5)
        if event_th.is_set():
            return
        pg.moveTo(*constants.POSITION_CORPS_DEAD)
        pg.dragTo(*constants.DRAGG_POSITION_LOOT)
        pg.sleep(0.5)


def close_loot():
    pg.moveTo(*constants.CLOSE_LOOT)
    pg.click()


def remove_corps(dead_x, dead_y):
    pg.moveTo(dead_x, dead_y)
    pg.dragTo(constants.CHAR_POSITION_CENTER)

def get_loot(event_th):
    try:
        if not os.path.exists(constants.MONTER_IMG_PATH) or not os.listdir(constants.MONTER_IMG_PATH):
            print('Loot não configurado')
            return 
        print('Iniciando coleta de loot')
        for directory, _, files in os.walk(constants.MONTER_IMG_PATH):
            for file in files:
                while pg.locateOnScreen(os.path.join(directory, file), confidence=0.85, region=constants.REGION_LOOT):
                    box = pg.locateOnScreen(os.path.join(directory, file), confidence=0.85, region=constants.REGION_LOOT)
                    print('Loot encontrado', box)
                    if box:
                        x, y = pg.center(box)
                        pg.moveTo(x, y)
                        if event_th.is_set():
                            return
                        print('Abrindo loot', box)
                        hold_click()
                        while not pg.locateOnScreen('imgs/sqm_empty.png', confidence=0.95, region=constants.POSITION_SQM_CHECK_LOOT):
                            print('Coletando Loot...')
                            if pg.locateOnScreen('imgs/lost_loot.png', confidence=0.8, region=constants.LOST_LOOT):
                                print('Sumiu o loot')
                                break
                            if event_th.is_set():
                                return
                            collect_loot(event_th)
                        print('Fechando Loot...')
                        close_loot()
                        remove_corps(x, y)
    except Exception as err:
        print(f'Não foi encotrado o diretório {constants.MONTER_IMG_PATH}', err)



def check_battle():
    # Tenta localizar a imagem com 80% de confiança
    print("checkando battle", pg.locateOnScreen('./imgs/region_battle.PNG',  confidence=0.9, region=constants.REGION_BATTLE,))
    return pg.locateOnScreen('./imgs/region_battle.PNG',  confidence=0.9, region=constants.REGION_BATTLE)
  


def eat_food():
     food = pg.locateAllOnScreen('./imgs/brown.png', confidence =0.8, region=constants.REGION_BAG)
     for bag in food:
         x, y = pg.center(bag)
         pg.moveTo(x, y)
         pg.click(button="right")



#hole_up('imgs/anchor_floor_3.png', 130, 130)
#def hole_down(should_down):
    #if should_down:
        # box = pg.locateOnScreen('C:/Users/FGTEC/Desktop/bt_tb/imgs/hole_down.png', confidence=0.6)
        # if box:
        #     x, y = pg.center(box)
        #     pg.moveTo(x,  y)
        #     pg.click()
        #     pg.sleep(5)


# def hole_up(should_up, img_anchor, plus_x, plus_y):
      #if should_up:
    #     box = pg.locateOnScreen(img_anchor, confidence=0.8)
    #     if box:
    #         x, y = pg.center(box)
    #         pg.moveTo(x +plus_x, y + plus_y)
    #         pg.click()
    #         pg.press('hk para usar exani tera')
# 130,130 é o equivalente a 1sqm


#def check_status(name, delay, x, y, rgb, button_name):
    # print(f'checando {name}...')
    # pg.sleep(delay)
    # if pg.pixelMatchesColor(x, y, rgb):
    #    pg.press(button_name)


#check_status('mana', 5, *POSITION_MANA_FULL, COLOR_MANA, 'F3' )
#check_status('life', 1, *constants.POSITION_LIFE, constants.COLOR_YELLOW_LIFE, pg.middleClick)








