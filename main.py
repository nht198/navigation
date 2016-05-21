import mp3
from flask import *
app = Flask(__name__)

music = mp3.Player()

@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html')

@app.route("/about")
def about():
        return render_template('about.html')

@app.route("/mp3")
def player():
        music.start()
	return render_template('mp3.html')

@app.route("/mp3/<change>",methods = ['POST'])
def mp3(change):
#	music.start()
	if (change == 'pause'):
                music.pause()
        if (change == 'stop'):
                music.stop()
        if (change == 'next'):
                music.next()
        elif (change == 'previous'):
                music.previous()
	return ''
if __name__ == "__main__":
        app.run(host = "0.0.0.0",port = 80, debug =True)

