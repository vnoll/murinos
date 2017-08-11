import time
from subprocess import call
import Adafruit_BBIO.GPIO as GPIO

def SetPullUp(pin):
    pud = "pullup"
    mux = 7
    script = "var b = require('bonescript'); b.pinMode('%s',b.INPUT,%i,'%s');" % (pin, mux, pud)
    command = ["node", "-e", script]
    call(command)

class Teclado(object):

    def __init__(self, g_data):
        #Pins
		self.data = g_data
		self.ButtonLeft = "P8_7"
		self.ButtonDown = "P8_9"
		self.ButtonUp = "P8_11"
		self.ButtonRight = "P8_15"
		self.ButtonConfirm = "P8_17"
		self.SetupTeclado()
		
  
    def SetupTeclado(self):  
		#BotoesMenu
        print "Inicializando Botoes teclado..."
        """SetPullUp(self.ButtonUp)
        SetPullUp(self.ButtonDown)
        SetPullUp(self.ButtonLeft)
        SetPullUp(self.ButtonRight)
        SetPullUp(self.ButtonConfirm)"""
        GPIO.setup(self.ButtonUp, GPIO.IN)
        GPIO.setup(self.ButtonDown, GPIO.IN)
        GPIO.setup(self.ButtonLeft, GPIO.IN)
        GPIO.setup(self.ButtonRight, GPIO.IN)
        GPIO.setup(self.ButtonConfirm, GPIO.IN)


# self.EstadoTeclado = {'left':False, 'down':False, 'up':False, 'right':False, 'confirm':False}

    def ReadTeclado(self):
		""" Funcao que le o teclado e atualiza as variaveis globais
			que serao atualizados pela classe display de acordo com o estado. 
			na classe display, apos atualizacao, variavel ChangedScreen eh trocada para False """
		
		UpdateButtonsTime = 0.4
		UpdateTime = time.time()
		
		while True:
			if ((time.time() - UpdateTime) > UpdateButtonsTime):

				if(GPIO.input(self.ButtonRight) == 0):
					self.data.EstadoTeclado['right'] = True
					UpdateTime = time.time()
					self.data.ChangedScreen = True
				
				if(GPIO.input(self.ButtonLeft) == 0):
					self.data.EstadoTeclado['left'] = True
					UpdateTime = time.time()
					self.data.ChangedScreen = True
				
				if(GPIO.input(self.ButtonDown) == 0):
					self.data.EstadoTeclado['down'] = True
					UpdateTime = time.time()

				
				if(GPIO.input(self.ButtonUp) == 0):
					self.data.EstadoTeclado['up'] = True
					UpdateTime = time.time()

				
				if(GPIO.input(self.ButtonConfirm) == 0):
					self.data.EstadoTeclado['confirm'] = True
					UpdateTime = time.time()
					
					