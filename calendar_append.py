from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle

# scopes = ['https://www.googleapis.com/auth/calendar.events']
# flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
# credentials = flow.run_console()
#
# pickle.dump(credentials, open("token.pkl", "wb"))

credentials = pickle.load(open("token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)

event = {
  'summary': 'Mock Event',
  'location': 'Logiscool',
  'description': 'Testing 123.',
  'start': {
    'dateTime': '2020-03-5T20:00:00-00:00',
    'timeZone': 'Europe/Bucharest',
  },
  'end': {
    'dateTime': '2020-03-5T23:00:00-00:00',
    'timeZone': 'Europe/Bucharest',
  },
  'colorId': 5,
  'reminders': {
    'useDefault': False,
    'overrides': [
      {'method': 'email', 'minutes': 24 * 60},
      {'method': 'popup', 'minutes': 10},
    ],
  },
}

event = service.events().insert(calendarId='primary', body=event).execute()
print('Event created: %s' % (event.get('htmlLink')))


