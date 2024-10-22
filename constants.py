import pyautogui as pg
import os

FOLDER_NAME = 'test'
REGION_BATTLE = (1570, 26, 155, 37) # 1742, 542, 172, 86
REGION_LOOT = (680, 342, 205, 202) # 825, 341, 265, 254
REGION_BAG = (1747, 689, 169, 95)
REGION_MAP_BATTLE = (1751, 25, 108, 111) # 1578, 54, 285, 215
POSITION_TARGET = (1575, 38) # 1746, 591
POSITION_TARGET_COLOR = (255, 0, 0)
TARGET_COLOR_WHITE = (255, 128, 128) # 255, 136, 136
POSITION_MANA_FULL = (1848, 198)
COLOR_MANA = (67, 64, 192)

POSITION_LIFE = (1809, 287)
COLOR_YELLOW_LIFE = (45, 72, 133)

BACKPACK_LOOT_POSITION_END = (1869, 496, 28, 28)
BACKPACK_LOOT_POSITION = (1753, 345, 149, 186)
DRAGG_POSITION_LOOT = (1770, 364)
POSITION_CORPS_DEAD = (1770, 576)
POSITION_SQM_CHECK_LOOT = (1755, 560, 31, 32)
CLOSE_LOOT = (1912, 546)
MONTER_IMG_PATH = os.path.join(FOLDER_NAME, 'dead_monsters')
LOOT_IMG_PATH = os.path.join(FOLDER_NAME, 'loot')
LOST_LOOT = (1740, 537, 48, 35) # regiao para caso sumir a bp de loot ele sair do loop
CHAR_POSITION_CENTER = (789, 449)

MAX_TIME_TO_IGNORE_MONSTER = 60




hatchet = './imgs/loot/hatchet.png'
crossbow = './imgs/loot/crossbow.png'
dwarven_shield = './imgs/loot/dwarven_shield.png'
chain_armor = './imgs/loot/chain_armor.png'
soldier_helmet = './imgs/loot/soldier_helmet.png'
axe = './imgs/loot/axe.png'
scale_armor = './imgs/loot/scale_armor.png'
battle_axe = './imgs/loot/battle_axe.png'
battle_shield = './imgs/loot/battle_shield.png'
double_axe = './imgs/loot/double_axe.png'
steel_helmet = './imgs/loot/steel_helmet.png'
studded_armor = './imgs/loot/studded_armor.png'

