import yaml
import pickle
import calendar_handle as calendar

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

credentials = pickle.load(open("token.pkl", "rb"))
if not credentials:
    credentials = calendar.handshake()
    pickle.dump(credentials, open("token.pkl", "wb"))
