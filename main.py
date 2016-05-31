import mp3
import temp
from flask import *
import led
from time import sleep
app = Flask(__name__)

music = mp3.Player()
led = led.led_control()
temp_class = temp.readtemp()

@app.route("/")
@app.route("/home")
def home():
        return render_template('home.html')

@app.route("/about")
def about():
        return render_template('about.html')

@app.route("/temperature")
def temerature():
	return render_template('temperature.html',temp=temp_class.read_temp())

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
		print music.name_song()
        elif (change == 'previous'):
                music.previous()
		print music.name_song()
	return render_template('mp3.html')

@app.route('/printsongmp3')
def printsongmp3():
        return (music.name_song() + ' is playing')

@app.route("/led")
@app.route("/led/<led_status>",methods = ['POST'])
def led_change(led_status= None):
	if(led_status == 'led1on'):
		led.led1on()
	elif (led_status == 'led1off'):
		led.led1off()	
	if(led_status == 'led2on'):
                led.led2on()
        elif (led_status == 'led2off'):
                led.led2off()
	return render_template('led.html')

@app.route('/printledstatus1')
def printledstatus1():
	status = request.args.get('state')
	if led.readstatusled1()==1:		
		return jsonify(result1='led 1 is on')
	elif  led.readstatusled1()==0:
		return jsonify(result1='led 1 is off')
@app.route('/printledstatus2')
def printledstatus2():
        status = request.args.get('state')
	if  led.readstatusled2()==1:
                return jsonify(result2='led 2 is on')
        elif  led.readstatusled2()==0:
                return jsonify(result2='led 2 is off')

button1=True
button2=True
def readbutton():
	global button1,button2
	input1 = led.readbutton1()
	input2 = led.readbutton2()
	if input1 == 0:
		sleep(0.3)
		button1= not button1
		if(button1==True):
			led.led1on()
		else:
			led.led1off()
	if input2 == 0:
                sleep(0.3)
                button2 = not button2
                if(button2==True):
                        led.led2on()
                else:
                        led.led2off()

if __name__ == "__main__":
        app.run(host = "0.0.0.0",port = 56, debug =True)
	while 1:
		readbutton()
		sleep(0.5)
