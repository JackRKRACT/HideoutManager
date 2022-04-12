import cv2 as cv
import numpy as np
import time
import pyautogui
import win32api, win32con
import os
from PIL import ImageGrab as imgr
from modules import modules
from game_menus import game_menus

def findImageScreen(template):
    curr_screen = np.asarray(imgr.grab())
    img_gray = cv.cvtColor(curr_screen, cv.COLOR_BGR2GRAY)
    if (type(template) != type(None)):
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        loc = np.where( res >= 0.9)
        return list(zip(*loc[::-1]))
    else:
        print("Unable to setup template image, returning an empty array on image check." )
        return []

def findImageScreenVarRes(template, accept):
    curr_screen = np.asarray(imgr.grab())
    img_gray = cv.cvtColor(curr_screen, cv.COLOR_BGR2GRAY)
    if (type(template) != type(None)):
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        loc = np.where( res >= accept)
        return list(zip(*loc[::-1]))
    else:
        print("Unable to setup template image, returning an empty array on image check." )
        return []

def loadHideoutModules():
    module_dir = r"resources\hideout_modules\\"
    mods = os.listdir(module_dir)
    module_list = []
    for mod in mods:
        image = cv.imread(module_dir + mod, 0)
        temp = modules(mod, image, module_dir)
        module_list.append(temp)
    return module_list

def cleanMenus(list, purged):
    for item in list:
        if item.startswith(purged):
            list.remove(item)
    return list

def loadModules():
    module_dir = r"resources\hideout_modules\\"
    mods = os.listdir(module_dir)
    module_list = []
    for mod in mods:
        title = mod.split('_')[0]
        mods = cleanMenus(mods, title)
        temp = game_menus(title, module_dir)
        module_list.append(temp)
    return module_list

def getModule(module_name, module_list):
    for module in module_list:
        if module.name == module_name:
            return module

def loadMenus():
    menu_dir = r"resources\menu_icons\\"
    trader_dir = r"resources\traders\\"
    menus = os.listdir(menu_dir)
    menus.remove("global_identifier.png")
    trader_menus = os.listdir(trader_dir)
    menu_list = []
    for menu in menus:
        title = menu.split('_')[0]
        menus = cleanMenus(menus, title)
        temp = game_menus(title, menu_dir)
        menu_list.append(temp)
    for trader in trader_menus:
        title = trader.split('_')[0]
        trader_menus = cleanMenus(trader_menus, title)
        temp = game_menus(title, trader_dir)
        menu_list.append(temp)
    return menu_list
    
def moveMouse(coordinates):
    if len(coordinates) != 0:
        # Will always try first option found in array, taking x & y coords for click.
        x = coordinates[0][0]
        y = coordinates[0][1]
        pyautogui.moveTo(x, y)
    else:
        print("Unable to perform move, no selection coordinates.")

def performClick(coordinates):
    if len(coordinates) != 0:
        # Will always try first option found in array, taking x & y coords for click.
        x = coordinates[0][0]
        y = coordinates[0][1]
        pyautogui.moveTo(x, y)
        pyautogui.click()
    else:
        print("Unable to perform click, no selection coordinates. (" + str(coordinates) + ")")

def inGame():
    while(1):
        ident = cv.imread("resources\menu_icons\global_identifier.png", 0)
        if (len(findImageScreen(ident)) != 0):
            return True
        else:
            print("Currently not in game. Checking again in 3 seconds.")
            time.sleep(3)

def enterMenu(target_img, response_img):
    inGame()
    img_loc = findImageScreen(target_img)
    if (len(img_loc) != 0):
            performClick(img_loc)
            while(len(findImageScreen(response_img)) == 0):
                time.sleep(1)
    else:
        return True

def enterHideout():
    inGame()
    hideout_inactive = cv.imread(r"resources\menu_icons\hideout_inactive.png",0)
    hideout_active = cv.imread(r"resources\menu_icons\hideout_active.png", 0)
    print("Entering Hideout.")
    enterMenu(hideout_inactive, hideout_active)

def currentMenu(menu_list):
    inGame()
    print("Checking current menu")
    for menu in menu_list:
        ident = cv.imread(menu.dir + menu.active_image, 0)
        if (len(findImageScreen(ident)) != 0):
            print("Currently at " + menu.name)
            return menu

def enterModule(module):
    # Check if user is in game
    inGame()
    # Check if user is in Hideout
    enterHideout()
    # Check if user is already in a module
    exit = cv.imread(r"resources\scroll_resource\module_exit.png",0)
    exit_loc = findImageScreen(exit)
    if (len(exit_loc) != 0):
        performClick(exit_loc)
        time.sleep(1)
    # Look for module
    module_loc = findModule(module)
    if (len(module_loc) != 0):
        # Enter module and confirm once inside
        module_img = cv.imread(module.dir + module.inactive_image, 0)
        print("Entering " + module.name)
        enterMenu(module_img, exit)
    else:
        # Unable to find module (?), skipping.
        print("Unable to locate " + module.name)

# Finds Hideout module and returns location on screen
def findModule(module):
    inGame()
    print("Finding module " + module.name)
    img = cv.imread(r"resources\menu_icons\global_identifier.png",0)
    left_bound = cv.imread(r"resources\scroll_resource\hideout_left.png", 0)
    right_bound = cv.imread(r"resources\scroll_resource\hideout_right.png", 0)
    module_img = cv.imread(module.dir + module.inactive_image, 0)
    is_left = True
    scroll_area = findImageScreen(img)
    moveMouse(scroll_area)
    pyautogui.move(0, -20)

    while(True):
        module_loc = findImageScreen(module_img)
        if (len(module_loc) != 0) :
            # Found module
            return module_loc
        elif (len(findImageScreen(right_bound)) != 0 or len(findImageScreen(left_bound)) != 0):
            # Found a bound. Changing directions!
            is_left = not is_left
        if (is_left):
            for x in range(10):
                pyautogui.scroll(-1)
        else:
            for x in range(10):
                pyautogui.scroll(1)
    

def findCraft(craft):
    inGame()
    img = cv.imread(r"resources\menu_icons\global_identifier.png",0)
    #top_bound = cv.imread(r"resources\scroll_resource\module_top.png", 0)
    #bottom_bound = cv.imread(r"resources\scroll_resource\module_bottom.png", 0)
    craft_img = cv.imread(craft.image_location, 0)
    is_top = True
    scroll_area = findImageScreen(img)
    moveMouse(scroll_area)
    pyautogui.move(0, -300)

    while(True):
        craft_loc = findImageScreen(craft_img)
        if (len(craft_loc) != 0) :
            # Found craft, have to check for requirements now too.
            print("Current craft location : " + str(craft_loc))
            print("Starting craft height : " + str(craft_img.shape[0]))
            craft_height = craft_img.shape[0]
            craft_top = craft_loc[0][1] - 30
            craft_bottom = craft_top + craft_height + 30
            req_loc_list = []
            for req in craft.req_list:
                req_img = cv.imread(req.image_location, 0)
                req_loc = findImageScreen(req_img)
                if len(req_loc) != 0:
                    req_y = req_loc[0][1]
                    print("Current requirement location : " + str(req_loc))
                    if req_y > craft_top and req_y < craft_bottom:
                        req_loc_list.append(req_loc)
            if len(req_loc_list) == len(craft.req_list):
                # Found craft + requirements, time to get 'START' button.
                start_img = cv.imread("crafts/craft1/start_valid.png", 0)
                start_locs = findImageScreen(start_img)
                for loc in start_locs:
                    print(str(loc))
                    loc_y = loc[1]
                    print("Checking first active start at y : " + str(loc_y))
                    if loc_y > craft_top and loc_y < craft_bottom:
                        print("Found active start location")
                        return loc
                    else:
                        print("Start button currently inactive, either needs requirements or fuel.")
                        return
            else:
                print("Not all requirements found, moving on.")      
        pyautogui.scroll(-1)

def performCraft(craft, module):
    print("Starting craft : " + craft.craft_name)
    enterModule(module)
    start_loc = findCraft(craft)
    print("Found craft location at : " + str(start_loc))
    x = start_loc[0]
    y = start_loc[1]
    pyautogui.moveTo(x, y)

def purchaseItemTrader(item, trader):
    print("Attempting to purchase item")

def purchaseItemFlea(item):
    print("Attempting to purchase item")