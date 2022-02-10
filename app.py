from transformers import pipeline, set_seed
from flask import Flask
from flask import request

app = Flask(__name__)


def encrypt(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

@app.route("/getStory")
def getStory():
    
    data  = request.json['data']
    seed = request.json['seed'] 

    # print(data)
    # generator = pipeline('text-generation', model='gpt2')
    # set_seed(42)
    # story=generator(data, max_length=100, num_return_sequences=1)

    story = encrypt(data,seed)
    return {'story':story}

if __name__ == '__main__':
   app.run()
   app.run(debug=True)