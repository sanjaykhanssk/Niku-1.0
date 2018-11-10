from  voicecontrol import call_correct

from firebase import firebase

firebaseref = firebase.FirebaseApplication('https://niku-1531031167486.firebaseio.com/')

while 1:   

    text = firebaseref.get('/Text',None)
    if text != '':
        firebaseref.put('/','Text','')
        print(text)
        call_correct(text)
    else:
        print("waiting for function")


# print(result)