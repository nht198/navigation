import os,glob,subprocess
#de lien ket cac ham voi nhau su dung self
class Player(object):
        def __init__(self):
                self.f = glob.glob('*.mp3')
                self.h=len(self.f)
                self.number = 0
                os.system('sudo killall omxplayer.bin')
        def start(self):
                self.player = subprocess.Popen(["omxplayer",self.f[self.number]],stdin=subprocess.PIPE)

        def pause(self):
                status = self.player.poll()
                if (status != 0):
                        self.player.stdin.write("p")

        def stop(self):
                status = self.player.poll()
                if (status != 0):
                        self.player.stdin.write("q")

        def next(self):
                self.player.stdin.write("q")
                self.number = self.number + 1
                if (self.number>self.h -1):
                        self.number = 0
                self.start()

        def previous(self):
                self.player.stdin.write("q")
                self.number = self.number - 1
                if (self.number < 0):
                        self.number = self.h -1
                self.start()
	
	def name_song(self):
		return (self.f[self.number])

