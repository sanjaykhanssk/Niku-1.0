


"""

#control linux by voice v.0.0.0.0

functions explained:
----------------------------------------------------------
#open_software -> to open software's(command starts with open)
--------------------------------------------------------------
#window_movement -> to controll window (doing maximum functions here)
----------------------------------------------------------------------
#cpy_pst ->function to copy paste
---------------------------------------------
#browser ->controll browser {[fouced:firefox],[string command with browser]}
-----------------------------------------------------------------------------
#media_controll -> controll vlc (command starts with media)
-------------------------------------------------------------
#scroll_fun -> controll mouse scroll (command starts with scroll)
-------------------------------------------------------------------
#call_correct ->this functions do call and send command to the correct function 
--------------------------------------------------------


"""



#program starts............



import speech_recognition as sr
import pyautogui as auto
import webbrowser as wb
import time
import os
import aiml
from pyddg import ddgs
import pyttsx3
engine = pyttsx3.init()
import subprocess as subp



r = sr.Recognizer()


def speak_loud(data):
    print(data)
    # subp.call("echo '{}' | festival --tts".format(data),shell= True)


# k = aiml.Kernel()
# k.bootstrap(learnFiles="std-startup.aiml", commands="load aiml b")
# def niku(text):
#     ai_output = k.respond(text)
#     print(ai_output)
#     engine.say(ai_output)
#     engine.runAndWait()

"""
----------------------------------------------------------
#open_software -> to open software(command starts with open)
--------------------------------------------------------------
"""

def open_software(text):
    
    if text == 'terminal':
        auto.hotkey('ctrl','alt','t')
        speak_loud("opening terminal ")
        
    elif text == 'browser':
        speak_loud("opening browser ")
        wb.open('https://duckduckgo.com')

    elif text == 'menu':
        auto.hotkey('winleft','a')    

    else:
        auto.press('winleft')
        time.sleep(2)
        auto.typewrite(text)
        time.sleep(1)
        auto.press('enter')
        speak_loud("opening {} ".format(text))



"""
--------------------------------------------------------------
#window_movement -> to controll window (doing maximum functions here)
----------------------------------------------------------------------
"""


def window_movement(text):
    
    notification=['notification','show notification','so notification','close notification','hide notification','show notifications']
    if text == 'minimise' or text == 'minimize':
        auto.hotkey('winleft','down')
        speak_loud('minimising window')
    elif text == 'maximize' or text == 'maximise':
        auto.hotkey('winleft','up')
        speak_loud('maximizing window')

    elif text == 'hide':
        auto.hotkey('alt','space')
        time.sleep(.1)
        auto.hotkey('space')
    elif text == 'page up' or text == 'top':
        auto.hotkey('pageup')
    elif text == 'page down' or text== 'down':
        auto.hotkey('pagedown')
    elif text == 'next window' or text == 'next windows':
        auto.hotkey('alt','tab')
    elif text == 'close window' or text == 'close windows' or text == 'close' or text == 'close it':
        auto.hotkey('alt','f4')
    elif text == 'move left' or text == 'left' or text =='lift' or text=='more right':
        auto.hotkey('winleft','left')
    elif text == 'move right' or text=='right' or text== 'more right':
        auto.hotkey('winleft','right')    
    elif text == 'next workspace':
        auto.hotkey('ctrl','alt','down')
        print('moving to next workspace')
    elif text == 'previous workspace' or text == 'last workspace':
        auto.hotkey('ctrl','alt','up')
    elif text in notification:
        auto.hotkey('winleft','v')
    elif text =='take screenshot':
        auto.screenshot()
    elif text == 'copy':
        auto.hotkey('ctrl','c')
    elif text == 'paste':
        print('paste called')
        auto.keyDown('ctrl')
        auto.press('v')
        auto.keyUp('ctrl')
    else:
        print('unallocated function')
    
    
def sound_fun(text):
    if text == 'mute':
        auto.keyDown('fn')
        auto.press('f10')
        auto.keyUp('fn')
"""
----------------------------------------------------------------------
#cpy_pst ->function to copy paste
---------------------------------------------
"""
def cpy_pst(text):
    if text =='copy this':
        auto.hotkey('ctrl','c')
    if text =='paste here':
        auto.hotkey('ctrl','v')

"""
---------------------------------------------
#browser ->controll browser {[fouced:firefox],[string command with browser]}
-----------------------------------------------------------------------------
"""

def browser(text):
    splited_text = text.split()
    if text == 'back':
        auto.hotkey('alt','left')
    elif text == 'next':
        auto.hotkey('alt','right')
    elif text == 'open':
        auto.hotkey('ctrl','o')
    elif text == 'reload':
        auto.hotkey('ctrl','r')
    elif text == 'reload cache':
        auto.hotkey('ctrl','f5')
    elif text == 'stop':
        auto.press('esc')
    elif text == 'bottom':
        auto.press('end')
    elif text == 'reload':
        auto.press('home')
    elif text == 'print':
        auto.hotkey('ctrl','p')
    elif text == 'find':
        auto.hotkey('ctrl','f')
    elif text == 'find again':
        auto.hotkey('ctrl','g')
    elif text == 'close tab':
        auto.hotkey('ctrl','w')
    elif text == 'reload':
        auto.hotkey('ctrl','r')
    elif text == 'new tab':
        auto.hotkey('ctrl','t')
    elif text == 'private window':
        auto.hotkey('ctrl','shift','p')
    elif text == 'private tab':
        auto.hotkey('ctrl','shift','t')
    
    elif text == 'first tab':
        auto.hotkey('alt','1')
    elif text == 'last tab':
        auto.hotkey('alt','9')
    elif text == 'history':
        auto.hotkey('ctrl','h')
    elif splited_text[0] == 'bookmark':
        auto.hotkey('ctrl','d')
    elif text == 'show bookmark' or text == 'show bookmarks':
        auto.hotkey('ctrl','b')
    elif text == 'open downloads':
        auto.hotkey('ctrl','shift','y')
    elif text == 'url':
        auto.hotkey('ctrl','k')
    elif text == 'inspect element':
        auto.hotkey('ctrl','shift','i')
    elif text == 'next tab':
        auto.hotkey('ctrl','tab')
    elif text == 'previous tab':
        auto.hotkey('ctrl','tab')
    elif text == 'undo tab':
        auto.hotkey('ctrl','shift','t')
    elif text == 'close' or text == 'exit':
        auto.hotkey('alt','f4')
    elif splited_text[0] == 'tab':
        auto.hotkey('alt',splited_text[1])

    else:
        print('browser has no function like that;')
        media_controll(text)
    
    
"""
-----------------------------------------------------------------------------
#media_controll -> controll vlc (command starts with media)
-------------------------------------------------------------
"""
    
def media_controll(text):
    if text == 'pause' or text =='play' or text =='pass'or text == 'player':
        auto.press('space')
    elif text=='full screen':
        auto.press('f')
    elif text == 'leave full screen':
        auto.press('esc')
    elif text == 'next':
        auto.press('n')
    elif text == 'previous':
        auto.press('p')
    elif text == 'stop':
        auto.press('s')
    elif text == 'volume up':
        auto.hotkey('ctrl','up')
    elif text == 'volume down':
        auto.hotkey('ctrl','down')
    elif text =='mute':
        auto.press('m')
    elif text == 'open':
        auto.hotkey('ctrl','o')
    else:
        print('media has no function like that;')
        scroll_fun(text)

"""
-------------------------------------------------------------
#scroll_fun -> controll mouse scroll (command starts with scroll)
-------------------------------------------------------------------
"""
def scroll_fun(text):
    if text == 'down':
        auto.scroll(-6)
    elif text == 'up':
        auto.scroll(6)
    elif text =='right':
        auto.hscroll(6)
    elif text == 'left':
        auto.hscroll(-6)
    else:
        print('scroll has no function like that')
        office(text)



"""
--------------------------------------------------------------
#office -> function controll wps office
--------------------------------------------------------------

"""
def office(text):
    splited_text = text.split()
    print(splited_text)
    if splited_text[0] == 'next':
        auto.press('right')
    elif splited_text[0] == 'back' or splited_text[0] == 'bag':
        auto.press('left')
    elif text=='start' or text == 'start slideshow' or text == 'slideshow' or text == 'start' or text == 'start the presentation':
        auto.press('f5')
    elif splited_text[0] == 'end' or splited_text[0] == 'exit':
        auto.press('esc')
    elif splited_text[0] =='close' or splited_text[0] == 'exit':
        auto.hotkey('alt','f4')
    elif splited_text[0] == 'move':
        auto.typewrite(splited_text[1])
        auto.press('enter')
    else:
        print('non office function called')
        window_movement(text)


def find(text):
    os.system('find -iname {}'.format(text))
    speak_loud('results are here')




"""
-------------------------------------------------------------------
#call_correct ->this functions do call and send command to the correct function 
-------------------------------------------------------------------


"""

def call_correct(text):
    text = text.lower()
    print('in call correct with',text)
    try:
        splited_text = text.split()
        listed_splited_text_for_maximum = ['minimise','maximise','minimize','maximize','hide']
        if splited_text[0] is None:
            exit
        if splited_text[0] == 'kill':
            os.system('pkill {}'.format(splited_text[1]))
        if splited_text[0] == 'open':
            splited_text.remove(splited_text[0])
            text = ' '.join(splited_text)
            open_software(text)
        elif splited_text[0] in listed_splited_text_for_maximum:
            window_movement(splited_text[0])
        # elif text.isalnum():
        #     auto.hotkey('winleft',text)
        elif text == 'focus window' or text == 'focus windows':
            auto.hotkey('winleft','s')
        elif splited_text[0] == 'sound':
            splited_text.remove(splited_text[0])
            text = ' '.join(splited_text)
            sound_fun(text)
        elif splited_text[0] =='copy' or splited_text[0] == 'paste': 
            cpy_pst(text)
        elif text == 'lock screen':
            auto.hotkey('winleft','l')
        elif splited_text[0] == 'browser':
            splited_text.remove(splited_text[0])
            text = ' '.join(splited_text)
            browser(text)
        elif splited_text[0] == 'media':
            splited_text.remove(splited_text[0])
            text = ' '.join(splited_text)
            media_controll(text)
        elif splited_text[0] == 'scroll':
            splited_text.remove(splited_text[0])
            text = ' '.join(splited_text)
            scroll_fun(text)
        elif splited_text[0] == 'office':
            splited_text.remove(splited_text[0])
            text =' '.join(splited_text)
            office(text)
        elif text == 'click':
            auto.click()
        elif splited_text[0] == 'type':
            splited_text.remove(splited_text[0])
            text =' '.join(splited_text)
            auto.typewrite(text)
        elif text == 'press enter' or text == 'enter':
            auto.press('enter')
        elif text == 'select all':
            auto.hotkey('ctrl','a')
        elif text == 'delete':
            auto.press('delete')
        elif text == 'backspace' or text == 'back space':
            auto.press('backspace')
        elif text == 'save':
            auto.hotkey('ctrl','s')
        elif text== 'save as':
            auto.hotkey('ctrl','shift','s')
        elif text == 'down':
            auto.press('down')
        elif text == 'up':
            auto.press('up')
        elif text == 'left':
            auto.press('left')
        elif text == 'right':
            auto.press('right')
        elif splited_text[0] == 'find':
            splited_text.remove(splited_text[0])
            text =' '.join(splited_text)
            find(text)
        elif splited_text[0] == 'search' or splited_text[0] =='duck':
            splited_text.remove(splited_text[0])
            text =' '.join(splited_text)
            if text != '':
                ddgs(text)
                engine.say("your results are here")
                engine.runAndWait()
            else:
                print('no query to search')

        elif text == 'file open' or text == 'find open':
            auto.hotkey('ctrl','o')
        elif text == 'escape':
            auto.press('esc')
        elif text == 'close tab':
            auto.hotkey('ctrl','w')
        elif splited_text[1] == 'window' or splited_text[1] == 'windows':
            window_movement(text)
        else:
            browser(text)

    

    
    # elif text == ' activate':
    #     from simplegesture import activate
    #     activate()  
    # elif splited_text[0] == 'niku' or splited_text[0] == 'nikku' or splited_text[0] == 'miku':
    #     splited_text.remove(splited_text[0])
    #     niku(text)
    
    except IndexError:
        
        browser(text)
        # window_movement(text)
    
      

# while 1:
#     with sr.Microphone() as source:
#             print("Speak:")
#             r.adjust_for_ambient_noise(source)
#             audio = r.listen(source,timeout=10)
#     try:
#         print('######...........processsssssinggggggggg...............######')
#         text = r.recognize_google(audio)
#         text= text.lower()
#         print(text)
#         if text != '':
#             call_correct(text)

        
#     except sr.UnknownValueError:
#         print("Could not understand audio ")

#         # text = input('press enter to continue (or) type your query:')
#         # if text == '':
#         #     continue
#         # else:
#         #     call_correct(text)
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#     # text= input('enter query to work:')
#     # call_correct(text)


       
