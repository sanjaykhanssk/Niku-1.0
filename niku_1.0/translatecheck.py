from wit import Wit
from textblob import TextBlob
from textout import startread

# text = list(resp['entities'])[0]
# value = resp['entities'][text][0]['value']
# print(text,value)

def call_from_here(text):
    entity =None
    value = None
    try:
        entity= list(text['entities'])[0]
        value =resp['entities'][entity][0]['value']
        # print(entity,value)
        if entity == 'translate':
            if value == 'tamil':
                data = startread()
                if data == '':
                    print('no data selected')
                else:
                    translate = TextBlob(data)
                    translate_lang = translate.detect_language()
                if translate_lang == 'ta':
                    print('the selected language is already in tamil')
                else:
                    translated_data = translate.translate(from_lang=translate_lang,to='ta')
                    print(translated_data)

        # if entity != None and value != None:
        #     if entity == 'niku':
        #         # print('in niku')
        #         if value == 'read':
        #             print('reading')
        #             # data = startread()
        #     elif entity == 'open':
        #         pass
        #     elif entity == 'weather':
        #         pass
        #         # print(data)
        #         # if data !='':
        #         #     subp.call("echo '{}' | festival --tts".format(data),shell= True)
        # else:
        #     pass
        #     # call_correct(text)
    except Exception as e:
        print(e)

client = Wit("ZNO6FG754JWMCICDJ3SZXBKB7KERIBT5")
text = None
value = None
resp = client.message('translate this to tamil ')
# print(resp)
call_from_here(resp)            