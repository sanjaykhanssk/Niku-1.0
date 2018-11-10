from dateutil import parser

import datetime
import subprocess as subp

def speakit(data):
    subp.call("echo '{}' | festival --tts".format(data),shell= True)

def set_reminder(text):
    entity =None
    value = None
    entity2=None
    value2 = None
    time = ''
    subject =''
    try:
        entity= list(text['entities'])[0]
        value =text['entities'][entity][0]['value']
        entity2 = list(text['entities'])[1]
        value2 =text['entities'][entity2][0]['value']
        # print(entity,value)
        # print(entity2,value2)
        if entity == 'datetime':
            dt = parser.parse('{}'.format(value))
            date,time = dt.date(),dt.time()
            subject = value2
            time = time.strftime('%H:%M')
            
            # datetime = date+time
        elif entity2 == 'datetime':
            dt = parser.parse('{}'.format(value2))
            date,time = dt.date(),dt.time()
            time = time.strftime('%H:%M')
            subject = value
            
            # datetime = date+time
        print('reminder set at {} about {}'.format(time,subject))
        speakit('setting reminder at {}'.format(time))
        check_reminder(time,value2)

        



    except Exception as e:
        print(e)

def check_reminder(time = None,subject=None):
    time_here = time
    subject_here = subject
    # time_here = time_here.append(time)
    # subject_here = subject_here.append(subject)
    print(time_here,subject_here)
    while 1:
        d = datetime.datetime.now()
        d= d.time()
        time_now=d.strftime('%H:%M')
        # for i in len(time_here):
        if time_now == time_here:
            subject_to_send = subject
            # time_here.remove(i)
            # subject_here.remove(i)
            speakit("you have a reminder about {}".format(subject_to_send))
            break
        else:
            pass
        break        

    


    
