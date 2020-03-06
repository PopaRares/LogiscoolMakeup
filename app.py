import email
import imaplib
import pickle
import re
import yaml

import calendar_handle as calendar


def get_body(msg):
    if msg.is_multipart():
        return get_body(msg.get_payload(0))
    else:
        return msg.get_payload(None, True).decode("utf-8")


def get_emails(res, connection):
    msgs = []
    for num in res[0].split():
        type, data = connection.fetch(num, '(RFC822)')
        msgs.append(data)
    return msgs


def build_event(email):
    timeZone = 'Europe/Bucharest'
    event = {}
    event['colorId'] = 5
    event['location'] = re.findall(r'(?<=School:\s).*', email)[0][:-1]
    event['summary'] = 'Recuperare - ' + re.findall(r'(?<=Course Type:\s).*', email)[0][:-1]
    event['start'] = {'dateTime': '2020-03-5T20:00:00-00:00',
                      'timeZone': timeZone}
    event['end'] = {'dateTime': '2020-03-5T23:00:00-00:00',
                    'timeZone': timeZone}
    return event


def main():
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

    # accessing Logiscool inbox folder
    con = imaplib.IMAP4_SSL(cfg['server']['address'])
    login_info = cfg['server']['login']
    print(login_info['email'])
    con.login(login_info['email'], login_info['password'])
    con.select('Logiscool')

    (ret, messages) = con.search(None, '(UNSEEN)')

    emails = get_emails(messages, con)
    if emails:
        # loading google calendar credentials
        try:
            credentials = pickle.load(open("token.pkl", "rb"))
        except:
            credentials = calendar.handshake()
            pickle.dump(credentials, open("token.pkl", "wb"))

    for em in emails:
        email_text = get_body(email.message_from_bytes(em[0][1]))
        calendar.make_event(credentials, build_event(email_text))


if __name__ == "__main__":
    main()
