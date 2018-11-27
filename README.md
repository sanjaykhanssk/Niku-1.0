# NIKU 1.0 <br /> 
Implemented in python3 <br /> 
### A next vesion of voice control desktop(niku0.0) <br /> 
>niku is mainly fouced on linux <br /> 
[niku 1.0 demo video](https://youtu.be/r5rgD769N0s)<br />

---------------------
>[Read in Blog](sanjaykhanssk.wixsite.com/aboutme/blog) <br />
>[About me](sanjaykhanssk.wixsite.com/resume)
------------------------------------------------------
![alt text](logo.png "Logo")


Its about the 

    1.natural language processing(textblob),

    2.multi threading

    3.Notifications(notifi2)

    4.named entity recognition (wit.ai) 

    5.Google firebase

    6.Html /js 

    7.kotlin(Android app) 

    8.pyaudio

Yes now you can send commands from your app on android (or) a page from chrome with voice recognition or with other browser  you can type in the Input field and click niku do 

![alt text](https://static.wixstatic.com/media/ee92ff_3ed02c59964349b680850f93d17bacc8~mv2.png/v1/fill/w_740,h_416,al_c,usm_0.66_1.00_0.01/ee92ff_3ed02c59964349b680850f93d17bacc8~mv2.png "niku web")

>Niku Android also available where you can send data or command from your app to desktop client of the niku

# HOW TO RUN IT
There are two main file in niku1.0 folder namely
>main.py
>mainfire.py
>index.html

### main.py
1.It's based on google speech synthesis,you change that to wit speech synthesis also
2.Optinal GUI PYQT5 in main.py at end of program some lines or commanded for hiding the gui,If you want you can enable that
3.This Accept all the data from App,Web input filed and 
>if your using chrome you can just speek and it will send data to the Niku desktop client
# mainfire.py

#### why mainfire.py
>According to me or in my expreince The chrome speech synthesis is better than google speech synthesis API for python 

1.If your using chrome as your browser,you can speek and it will recogonise it and sent to the client version of niku
2.If you'r non-chrome user, it's like a chat app type it and send-it.That's it will start control your system

## Examples:
>user:hey niku open inkscape

>niku:opening inkscape
-----------------------------
>user:hey baby read the selected text

>niku:started reading the selected text
----------------------------
>user:hey niku translate this to tamil

>niku:translating text to tamil<br /> 
>niku:Translated text saved in translated.txt
----------------------------

etc 
etc...
