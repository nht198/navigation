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

led1_status = ''
led2_status = ''
status1 = ''
status2 = ''
@app.route("/led")
def led_main(): 
	global led1_status
	global led2_status
	global status1
	global status2
	if led1_status == True :
		status1 = 'ON'
	else: 	status = 'OFF'
	if led2_status == True :
                status2 = 'ON'
        else: status2 = 'OFF'
	return render_template('led.html',led1_value=status1,led2_value=status2)

@app.route("/led/<led_status>",methods = ['POST'])
def led_change(led_status):
	if(led_status == 'led1'):
#		global led1_status
		led1_status = led.changeled1()
	if (led_status == 'led2'):
#		global led2_status
		led2_status = led.changeled2()
	return ''

if __name__ == "__main__":
        app.run(host = "0.0.0.0",port = 5000, debug =True)

