import speech_recognition as sr
from  voicecontrol import call_correct

r = sr.Recognizer()




while 1:
    with sr.Microphone() as source:
            print("Speak:")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source,)
            print('done')
    try:
        print('######...........processsssssinggggggggg...............######')
        #text = r.recognize_wit(audio,key='ZNO6FG754JWMCICDJ3SZXBKB7KERIBT5')
        text= r.recognize_google(audio)
        text= text.lower()
        print(text)
        if text != '':
            call_correct(text)

        
    except sr.UnknownValueError:
        print("Could not understand audio ")

        # text = input('press enter to continue (or) type your query:')
        # if text == '':
        #     continue
        # else:
        #     call_correct(text)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
    # text= input('enter query to work:')
    # call_correct(text)


       