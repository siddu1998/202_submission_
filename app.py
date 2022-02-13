from transformers import pipeline, set_seed
from flask import Flask
from flask import request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


#ideally should have been a read from a database 
#(had little time to do it so just did a global variable)
# Not the most ideal way to do it, since it resets everytime the app crashes or heroku dyno goes down

violation = 0 

@app.route('/add_violation', methods = ['POST'])
def add_violation():
    global violation
    data = json.loads(str(request.data, encoding='utf-8'))
    violation+=data['violations']
    return {"violations":violation}


if __name__ == '__main__':
   app.run(debug=True)
   app.run()
