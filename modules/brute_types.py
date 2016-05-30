# coding: utf8
import json
from colorama import Fore
import os
import output




# Config Variables #

TIME_SLEEP = 0
SHOW_GOODS = 1
# ---------------- #

def load_scripts ():
    RETR = dict ()
    for i in os.listdir ('scripts/'):
        print
        RETR [i.replace ('.py', '')] = __import__ ('scripts.' + i.replace ('.py', ''))
    return RETR

def parse_json_config (config_path):

    global TIME_SLEEP, SHOW_GOODS
    
    JSON_CODE = ''
    
    try:
        for i in open (config_path, 'r').readlines ():
            JSON_CODE += i
    except IOError:
        print output.ERR + 'Can\'t open config-file!'
    
    parser = json.loads (JSON_CODE)
    
    TIME_SLEEP = parser ['timeSleep']
    SHOW_GOODS = parser ['showGoods']

def runmodule (module, login, pass_list):

    from importlib import import_module
    
    IS_ARRAY = False
    GOOD = list ()

    brute = getattr(import_module ('scripts.{0}'.format (module)), 'Brute') ()
    
    try:
        login.append ('!')
        login.remove ('!')
        IS_ARRAY = True
    except:
        IS_ARRAY = False
    
    try:    
        f = pass_list
    except:
        print output.ERR + 'Can\'t open file with passwords!'
        exit ()
        
    for i in f.readlines ():
        pwd_full = i.strip ('\n')
        if IS_ARRAY:
            for j in login:
                brute.run (current_login=j.strip ('\n'), current_password=pwd_full, is_loginlist=True)
        else:
            brute.run(current_login=login, current_password=pwd_full, is_loginlist=False)
    
    if SHOW_GOODS == 1: show_goods(GOOD)

def show_goods (goods):
    if len (goods) > 0:
        print Fore.GREEN + 'GOOD'
        print '#'*70
        for i in goods: print i
        print '#'*70 + Fore.RESET
    
