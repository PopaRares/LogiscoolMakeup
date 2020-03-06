from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime

# returns google handshake credentials
def handshake():
    scopes = ['https://www.googleapis.com/auth/calendar.events']
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    return flow.run_console()


def make_event(cred, event):
    service = build("calendar", "v3", credentials=cred)
    calendar_event = service.events().insert(calendarId='primary', body=event).execute()
    log = open('logfile.log', 'a')
    log.write('Event [' + event['summary'] + '] created: ' + calendar_event.get('htmlLink') + ' (' + str(datetime.now()) + ')\n')
    log.close()
