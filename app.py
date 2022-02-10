from transformers import pipeline, set_seed
from flask import Flask
from flask import request

app = Flask(__name__)


def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        # Encrypt uppercase characters in plain text      
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
        return result


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