from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
from calendar_api.calendar_api import google_calendar_api
m=google_calendar_api()

# If modifying these scopes, delete the file token.j
# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar'

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
    # Refer to the Python quickstart on how to setup the environment:
# https://developers.google.com/calendar/quickstart/python
# Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
# stored credentials.

def check(date,subject):
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    # event = {
    # 'summary': subject,
    # 'location': '',
    # 'description':subject,
    # 'start': {
    #     'dateTime': date,
    #     'timezone':'Indian Standrad Time'
        
    # },
    # 'end': {
    #     'dateTime': date,
    #     'timezone':'Indian Standrad Time'
        
    # },
    # 'recurrence': [
    #     'RRULE:FREQ=DAILY;COUNT=2'
    # ],
    # 'attendees': [
    #     {'email': 'sanjaykhanssk@gmail.com'},
        
    # ],
    # 'reminders': {
    #     'useDefault': False,
    #     'overrides': [
    #     {'method': 'email', 'minutes': 24 * 60},
    #     {'method': 'popup', 'minutes': 10},
    #     ],
    # },
    # }

    # event = service.events().insert(calendarId='primary', body=event).execute()
    m.create_event(calendar_id='primary',
    start=date,
    end=date,
    desc=subject
    )
    print ('Event created: %s' % (event.get('htmlLink')))

