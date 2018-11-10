from duckduckgo import get_zci as ddg
import validators as val
import webbrowser as wb
import os
def ddgs(Query):
    userQuery = Query
    try:
        os.system('aplay notification_sound/search.wav')
        link=ddg(userQuery)        
        print(link)
        if val.url(link):
            wb.open(link)
            # sug = input('can i open link with web browser(Y/N)')
            # sug=sug.lower()
            # if sug == 'y' or sug == 'yes':

            #     wb.open(link)
    except Exception as e:
        print(e)

