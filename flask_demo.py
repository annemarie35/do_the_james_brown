from flask import Flask, url_for, render_template, request
from james import *

app = Flask(__name__)

@app.route('/')
def accueil():
   return render_template('index.html')


@app.route('/', methods=['GET','POST'])
def api_root():
    james = James()
    if request.method == 'POST':
        sentence = request.form['sentence']
        image = james_image_answer(james.ask(sentence))
        return render_template("index.html", sentence=sentence, answer=james.ask(sentence), image=image)
    return render_template("index.html")

def james_image_answer(answer):
    images = {'Sure': 'http://www.relativelydigital.com/wp-content/uploads/2011/03/SpongeBob-SquarePants.jpeg',\
    'Woah': 'https://year5birgu.files.wordpress.com/2011/04/sponge_bob.jpg',\
    'Damn right. I am somebody': 'http://33.media.tumblr.com/f1cfc2b4740583156e4a5e6c8514cec6/tumblr_mhqdtm8KCD1qedb29o1_r2_500.gif',\
    'Fine': 'http://www.pycomall.com/images/P1/Sponge_Bob_Square_Pants_1.jpg',\
    'Weird': 'http://38.media.tumblr.com/2a2abf3896b514125e56b5dcaab099cb/tumblr_n8u606TKhq1qedb29o1_400.gif',\
    'Whatever':'http://mypartyshirt.com/media/catalog/product/cache/1/image/9df78eab33525d08d6e5fb8d27136e95/s/p/sponge-bob-shirt_1_3.png'\
    }
    return images[answer]

@app.route('/dance', methods=['GET','POST'])
def dance():
    return render_template("dance_lessons.html")

def james_dance(dance):
    images = {'Boogaloo' : 'http://www.gifwave.com/media/376349/70s-dancing-james-brown-boogaloo-soul-connection.gif'}
    return images[dance]

if __name__ == '__main__':
    app.run(debug = True)


