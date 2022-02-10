from transformers import pipeline, set_seed
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/getStory")
def getStory():
    
    data = request.json['data']
    print(data)
    generator = pipeline('text-generation', model='gpt2')
    set_seed(42)
    story=generator(data, max_length=100, num_return_sequences=1)
    return {'story':story}

if __name__ == '__main__':
   app.run()
   app.run(debug=True)