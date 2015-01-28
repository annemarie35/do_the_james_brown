from flask import Flask, url_for, render_template, request
from james import *
from james_dance import *

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
    images = {'Damn right. I am somebody': 'http://33.media.tumblr.com/f1cfc2b4740583156e4a5e6c8514cec6/tumblr_mhqdtm8KCD1qedb29o1_r2_500.gif',\
    'I feel Good !': 'http://liquor.s3.amazonaws.com/wp-content/uploads/2014/06/james-brown-gif-2.gif',
    }
    return images[answer]

@app.route('/dance', methods=['GET','POST'])

def dance():
    dance = Dance()
    if request.method == 'POST':
        dance_style = request.form['dance_style']
        image = james_dance_img(dance.jamesdance(dance_style))
        return render_template("dance_lessons.html", dance_style=dance_style, answer=dance.jamesdance(dance_style), image=image)
    return render_template("dance_lessons.html")

def james_dance_img(dance):
    images = {'Boogaloo': 'http://www.gifwave.com/media/376349/70s-dancing-james-brown-boogaloo-soul-connection.gif',\
    'CamelWalk': '/images/camel_walk.gif',
    }
    return images[dance]

# def contact():
#     if request.method == 'POST':
#         if request.form['submit'] == 'Do Something':
#             pass # do something
#         elif request.form['submit'] == 'Do Something Else':
#             pass # do something else
#         else:
#             pass # unknown
#     elif request.method == 'GET':
#         return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug = True)


