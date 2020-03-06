from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# returns google handshake credentials
def handshake():
    scopes = ['https://www.googleapis.com/auth/calendar.events']
    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    return flow.run_console()


def make_event(cred, event):
    service = build("calendar", "v3", credentials=cred)
    event = service.events().insert(calendarId='primary', body=event).execute()
    print('Event created: %s' % (event.get('htmlLink')))
