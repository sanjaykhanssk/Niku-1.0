from PyQt5 import QtWidgets,uic
import sys
from threading import Thread
import speech_recognition as sr
from  voicecontrol import *
from textout import startread
import subprocess as subp
from wit import Wit
import time
from weatherinfo import weather_api
from firebase import firebase
from textblob import TextBlob
from baby.notify import notify_msg
from pyddg import ddgs
from dateutil import parser
import datetime
from notification_sound.run import play_sound
from pyddg import ddgs
# from reminder import set_reminder


r = sr.Recognizer()
client = Wit("ZNO6FG754JWMCICDJ3SZXBKB7KERIBT5")
firebaseref = firebase.FirebaseApplication('https://niku-1531031167486.firebaseio.com/')

# def call_of_call_frm_here(data_from_other_fun_to_call_from_here):
#     pass
#     # call_frm_hre_thread = Thread(target=call_from_here(data_from_other_fun_to_call_from_here))
#     # call_frm_hre_thread.start()



def speakit(data):
    subp.call("echo '{}' | festival --tts".format(data),shell= True)



# def recoginze_call(audio):
#     # time.sleep(3)
#     try:
#         print('######...........processsssssinggggggggg...............######')
#         # text = r.recognize_wit(audio,key='ZNO6FG754JWMCICDJ3SZXBKB7KERIBT5')
#         text= r.recognize_google(audio)
#         text= text.lower()
#         print(text)
#         # print(text)
#         if text != '':
#             # call_correct(text)
#             # call_from_here(text)
#             # call_frm_hre_thread = Thread(target=call_from_here(text))
#             # call_frm_hre_thread.start()
#             # call_frm_hre_thread.join()
#             call_from_here(text)
#             niku.box.addItem(text)
            

            
#     except sr.UnknownValueError:
#         print("Could not understand audio ")
#         # notify_msg(message="Could not understand audio ")
#         niku.box.addItem("Could not understand audio")

#         # text = nikubarut('press enter to continue (or) type your query:')
#         # if text == '':
#         #     continue
#         # else:
#         #     call_correct(text)
#     except sr.RequestError as e:
#         print("Could not request results; {0}".format(e))
#         niku.box.addItem("some error  it will noted in below \n {}".format(e))
def set_reminder(text):
    entity =None
    value = None
    entity2=None
    value2 = None

    try:
        entity= list(text['entities'])[0]
        value =text['entities'][entity][0]['value']
        entity2 = list(text['entities'])[1]
        value2 =text['entities'][entity2][0]['value']
        # print(entity,value)
        # print(entity2,value2)
        if entity == 'datetime':
            dt = parser.parse('{}'.format(value))
            date,timeit = dt.date(),dt.time()
            subject = value2
            timeit= timeit.strftime('%H:%M')
            
            # datetime = date+time
        elif entity2 == 'datetime':
            dt = parser.parse('{}'.format(value2))
            date,timeit = dt.date(),dt.time()
            timeit = timeit.strftime('%H:%M')
            subject = value
            
            # datetime = date+time
        speakit('setting reminder at {}'.format(timeit))
        return timeit,subject

    except Exception as e:
        pass
        # print(e)



def from_app():
    while 1:
        text = firebaseref.get('/Text',None)
        if text != '':
            os.system('aplay notification_sound/from_other.wav')
            firebaseref.put('/','Text','')
            print('from app:',text)
            notify_msg(message='Data from App')

            call_from_here(text)
            time.sleep(.01)

def from_web_voice():
    while 1:
        
        text = firebaseref.get('/from_web_speech',None)
        if text != '':
            os.system('aplay notification_sound/from_other.wav')
            firebaseref.put('/','from_web_speech','')
            print('from web voice:',text)
            notify_msg(message='Data from web voice')

            call_from_here(text)
            time.sleep(.01)
def from_web_text():
    while 1:
        text = firebaseref.get('/from_web_app',None)
        if text != '':
            os.system('aplay notification_sound/from_other.wav')
            firebaseref.put('/','from_web_app','')
            print('from web app:',text)
            notify_msg(message='Data from web text')

            call_from_here(text)
            time.sleep(.01)


# def show_print():
#     data = ""

#     while 1:

#         with sr.Microphone() as source:
#                 print("Speak:")
#                 r.adjust_for_ambient_noise(source)
#                 audio = r.listen(source,)
#                 print('voice done')
#                 recoginze_call(audio)
#         # try:
#         #     print('######...........processsssssinggggggggg...............######')
#         #     # text = r.recognize_wit(audio,key='ZNO6FG754JWMCICDJ3SZXBKB7KERIBT5')
#         #     text= r.recognize_google(audio)
#         #     text= text.lower()
#         #     # print(text)
#         #     if text != '':
#         #         # call_correct(text)
#         #         # call_from_here(text)
#         #         # call_frm_hre_thread = Thread(target=call_from_here(text))
#         #         # call_frm_hre_thread.start()
#         #         # call_frm_hre_thread.join()
#         #         call_of_call_frm_here(text)
#         #         niku.box.addItem(text)
            

            
#         # except sr.UnknownValueError:
#         #     print("Could not understand audio ")
#         #     # notify_msg(message="Could not understand audio ")
#         #     niku.box.addItem("Could not understand audio")

#         #     # text = nikubarut('press enter to continue (or) type your query:')
#         #     # if text == '':
#         #     #     continue
#         #     # else:
#         #     #     call_correct(text)
#         # except sr.RequestError as e:
#         #     print("Could not request results; {0}".format(e))
#         #     niku.box.addItem("some error  it will noted in below \n {}".format(e))
#         # # text= nikubarut('enter query to work:')
#         # # call_correct(text)
#         time.sleep(0.02)






def call_from_here(text):
    # blob = TextBlob(text)
    # blob = blob.correct()
    # text = blob
    resp = client.message(text)
    print(resp)
    # print('entity value is {}'.format(list(resp['entities'])[0]))
    entity =None
    value = None
    try:
        entity= list(resp['entities'])[0]
        value =resp['entities'][entity][0]['value']
        # print(entity,value)
        # time.sleep(.10)
        if entity != None and value != None:
            if entity == 'niku':
                # print('in niku')
                if value == 'read':
                    print('reading')
                    data = startread()
                    speakit(data)
            if entity == 'translate':
                       # print(entity,value)
       
                if value == 'tamil':
                    data = startread()
                    if data == '':
                        speakit('sorry,no data selected')
                    else:
                        speakit('trying to translate selected text in tamil')
                        translate = TextBlob(data)
                        try:
                            translate_lang = translate.detect_language()
                            # print('deteced language is ',translate_lang)
                            if translate_lang == 'ta':
                                speakit('the selected language is already in tamil')
                            else:
                                speakit('translating data from {}'.format(translate_lang))
                                translated_data = translate.translate(from_lang=translate_lang,to='ta')
                                translated_data = str(translated_data)
                                # print(translated_data)
                                with open('translated.txt','w') as result_file:
                                    result_file.write(translated_data)
                                    os.system('aplay notification_sound/translating.wav') 
                                    speakit('the data was translated sucessfully')
                                    print('the data was translated and saved in translated.txt sucessfully')
                            # niku.trans_text.setText(translated_data)
                        except Exception as e:
                            os.system('aplay notification_sound/error.wav')
                            speakit('sorry some error happend while translating')
                            print ('sorry some error happend while translating the error is',e)
            
            
            
            elif entity == 'datetime' or entity =='subject':
                timeit,subject = set_reminder(resp)
                

                        

                        
            elif entity == 'open':
                open_software(value)
            elif entity == 'show':
                window_movement(value)

            elif entity == 'weather':
                data  = weather_api(value)
                speakit('the weather in {} is {}'.format(value,data))
                print('the weather in {} is {}'.format(value,data))
            elif entity == 'search_niku':
                ddgs(value)
                # 
        # else:
        #     print(text)
        #     call_correct(text)
    
    except IndexError:
        # print(resp)
        # print(text)
        call_correct(text)
        # print(e)




# def from_desktop():
#     if niku.nikubar.text() == '':
#         pass
#     else:
#         text = niku.nikubar.text()
#         niku.box.addItem(niku.nikubar.text())
#         niku.box.scrollToBottom()
#         # print(niku.nikubar.text())
#         niku.nikubar.setText("")
            
#         # call_frm_hre_thread = Thread(target=call_from_here(text))
#         # call_frm_hre_thread.start()
#         # call_frm_hre_thread.join()
#         call_of_call_frm_here(text)


#         # call_from_here(text)
        






# def thr():
#     from_desktop_thread  = Thread(target=from_desktop)
#     from_desktop_thread.start()
#     from_desktop_thread.join()





if __name__ == "__main__":
    
    speakit('hello sanjay welcome back')
    
    # speech_recon_thread = Thread(target=show_print)
    # speech_recon_thread.start()

    # recoginze_call_thread = Thread(target=recoginze_call)
    # recoginze_call_thread.start()
    
    # call_of_call_frm_here()
    call_frm_hre_thread = Thread(target=call_from_here)
    call_frm_hre_thread.start()

    from_app_thread = Thread(target=from_app)
    from_app_thread.start()
    
    from_web_voice_thread = Thread(target=from_web_voice)
    from_web_voice_thread.start()
    
    from_web_app_thread = Thread(target=from_web_text)
    from_web_app_thread.start()
    

    from_app_thread.join()
    call_frm_hre_thread.join()
    from_web_app_thread.join()
    from_web_voice_thread.join()
    # recoginze_call_thread.join()
    # speech_recon_thread.join()

    # niku.nikubar.returnPressed.connect(thr)



    
    # niku.show()
    # app.exec()
    # sys.exit()
