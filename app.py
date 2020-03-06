import yaml
import pickle
import calendar_handle as calendar

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile, Loader=yaml.FullLoader)

try:
    credentials = pickle.load(open("token.pkl", "rb"))
except:
    credentials = calendar.handshake()
    pickle.dump(credentials, open("token.pkl", "wb"))

