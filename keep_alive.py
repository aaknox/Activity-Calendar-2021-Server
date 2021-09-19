import logging
import json
from flask import Flask
from threading import Thread
from flask import jsonify
from flask import request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)
#prettify json turned on
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# logging configs
log_filename = "ac.log"
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%d-%m-%Y:%H:%M:%S',
    level=logging.DEBUG,
    filename=log_filename, 
    filemode='w')

@app.route('/')
def home():
    logging.info('Admin is checking if system is online...')
    return "Hello. I am alive!"

@app.route('/settings')
def settings():
    d = getSettings()
    return jsonify(d)

@app.route('/save', methods=['POST'])
@cross_origin(supports_credentials=True)
def saveSettings():
    logging.info('User is sending some new settings to server...');
    sentData = request.get_json(force=True)
    print('Sent data: \n')
    print(sentData)
    changeSettings(sentData)
    return jsonify(sentData)

def run():
  if __name__ == "keep_alive":
    logging.info('Server is online...')
    app.run(host='0.0.0.0',port=9001)
  else:
    logging.info("Sorry, but Server " + __name__ + ".py is offline. Server Error.")

#read from json upon receiving GET request
def getSettings():
  logging.info('GET request received! Reading from JSON file...')
  with open('settings.json') as json_file:
    data = json.load(json_file)
    return data  

# write to settings.json based on sent json
def changeSettings(sent):
  print(sent)
  with open('settings.json', 'w') as outfile:
      json.dump(sent, outfile, sort_keys=True, indent=4)


# keeps constant ping on server to stay online
def keep_alive():
    logging.info('Keep_Alive FlaskServer: Auto-survival mode is now on')
    t = Thread(target=run)
    t.start()