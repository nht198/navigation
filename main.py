import mp3
from flask import *
import led
app = Flask(__name__)

music = mp3.Player()
led = led.led_control()

@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html')

@app.route("/about")
def about():
        return render_template('about.html')

mp3_player = False
@app.route("/mp3")
@app.route("/mp3/<change>",methods = ['POST'])
def mp3(change=None):
	global mp3_player
	if (change == None and mp3_player == False):
		mp3_player = True
		music.start()
	if (change == 'pause'):
                music.pause()
        if (change == 'stop'):
                music.stop()
		mp3_player = False
        if (change == 'next'):
                music.next()
        elif (change == 'previous'):
                music.previous()
	return render_template('mp3.html')


@app.route("/led")
@app.route("/led/<led_status>",methods = ['POST'])
def led_change(led_status= None):
#        led1_status = None
#        led2_status = None
	if(led_status == 'led1on'):
#		global led1_status
		led.changeled1()
	if (led_status == 'led1off'):
#		global led2_status
		led.changeled1()	
	return render_template('led.html')

@app.route('/printledstatus')
def printledstatus():
	status = request.args.get('state')
	if status == 'led1on':		
		return jsonify(result='led 1 is on')
	if status == 'led1off':
		return jsonify(result='led 1 is off')

if __name__ == "__main__":
        app.run(host = "0.0.0.0",port = 5000, debug =True)

