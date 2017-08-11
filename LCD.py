
import time
import Adafruit_CharLCD as LCD
import netifaces as ni

# Define LCD column and row size for 16x2 or 20x4 LCD .
lcd_columns = 20
lcd_rows = 4

class lcd(object):
    
    def __init__(self, g_data):
        self.data = g_data
        #BeagleBone Black configuration for LCD:
        self.lcd_rs = 'P8_8'
        self.lcd_en = 'P8_10'
        self.lcd_d4 = 'P8_18' 
        self.lcd_d5 = 'P8_16' 
        self.lcd_d6 = 'P8_14' 
        self.lcd_d7 = 'P8_12'
        self.lcd = LCD.Adafruit_CharLCD(self.lcd_rs, self.lcd_en, self.lcd_d4, self.lcd_d5, self.lcd_d6, self.lcd_d7, lcd_columns, lcd_rows)
        self.SetupLCD()
        self.TelaInicial()
        time.sleep(2)
        self.DisplayAll()
        
    def SetupLCD(self):
        self.lcd.clear()
        self.lcd.set_cursor(0,0)
        self.lcd.message("Inicializando...")

    def TelaInicial(self):
        self.lcd.clear()
        self.lcd.set_cursor(0,0)
        self.lcd.message("        IFSC        ")
        self.lcd.set_cursor(0,1)
        self.lcd.message("     Engenharia     ")
        self.lcd.set_cursor(0,2)
        self.lcd.message("     Mecatronica    ")
        self.lcd.set_cursor(0,3)
        #ni.ifaddresses('eth0')
        #ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
        #self.lcd.message(ip)
        #print ip
        time.sleep(5)

    def DisplayCurrent(self):
        #global self.data.CurrentFrequency, self.data.Pressao, self.data.Passo, self.data.ValueOnly, self.data.Diametro, self.data.TempoFinal
        if(self.data.ValueOnly == True):
            self.lcd.set_cursor(11,0)
            self.lcd.message(format((self.data.CurrentFrequency*3.14*self.data.Diametro*3600)/(1000*200*self.data.Passo*10)*1.0, '.1f') + " Km/h ")
            self.lcd.set_cursor(8,1)
            self.lcd.message(str(self.data.Pressao/10.0) + " cm H2O ")
            self.lcd.set_cursor(15,2)
            self.lcd.message(format((self.data.TempoFinal - time.time())/60, '.0f') + " ")
        elif(self.data.ValueOnly == False):
            self.lcd.clear()
            self.lcd.set_cursor(0,0)    
            self.lcd.message("Velocidade=" + format((self.data.CurrentFrequency*3.14*self.data.Diametro*3600)/(1000*200*self.data.Passo*10)*1.0, '.1f') + " Km/h ")
            self.lcd.set_cursor(0,1)
            self.lcd.message("Pressao=" + str(self.data.Pressao/10.0) + " cm H2O ")
            self.lcd.set_cursor(0,2)
            self.lcd.message("Tempo restante:" + format((self.data.TempoFinal - time.time())/60, '.0f'))
        self.data.ValueOnly = True

    def DisplayAll(self):
        #global self.data.Velocidade, self.data.Incremento, self.data.Pressao, self.data.Inclinacao
        self.lcd.clear()
        self.lcd.set_cursor(0,0)    
        self.lcd.message("Velocidade=" + str(self.data.Velocidade/10.0) + " Km/h ") 
        self.lcd.set_cursor(0,1)
        self.lcd.message("Incremento=" + str(self.data.Incremento/10.0) + " Km/h ")
        self.lcd.set_cursor(0,2)
        self.lcd.message("Pressao=" + str(self.data.Pressao/10.0) + " cm H2O ")
        self.lcd.set_cursor(0,3)
        self.lcd.message("Inclinacao=" + str(self.data.Inclinacao) + " % ")

    def ConfigTempo(self,Value = False):
        #global self.data.Tempo
        if(Value == False):
            self.lcd.clear()
            self.lcd.set_cursor(0,0)
            self.lcd.message("Tempo=" + str(self.data.Tempo) + " min")
            self.lcd.set_cursor(0,1)
            self.lcd.message("Tempo de exercicio")
            self.lcd.set_cursor(0,2)
            self.lcd.message("Altere o valor com")
            self.lcd.set_cursor(0,3)
            self.lcd.message("as setas cima/baixo")
          
        elif(Value == True):
            self.lcd.set_cursor(6,0)
            self.lcd.message(str(self.data.Tempo) + " min ")

    def ConfigVelocidade(self,Value = False):
        #global self.data.Velocidade
        if(Value == False):
            self.lcd.clear()
            self.lcd.set_cursor(0,0)
            self.lcd.message("Velocidade=" + str(self.data.Velocidade/10.0) + " Km/h ")
            self.lcd.set_cursor(0,1)
            self.lcd.message("Velocidade final")
            self.lcd.set_cursor(0,2)
            self.lcd.message("Altere o valor com")
            self.lcd.set_cursor(0,3)
            self.lcd.message("as setas cima/baixo")
        elif(Value == True):
            self.lcd.set_cursor(11,0)
            self.lcd.message(str(self.data.Velocidade/10.0) + " Km/h ")

    def ConfigIncremento(self,Value = False):
        #global self.data.Incremento
        if(Value == False):
            self.lcd.clear()
            self.lcd.set_cursor(0,0)
            self.lcd.message("Incremento=" + str(self.data.Incremento/10.0) + " Km/h ")
            self.lcd.set_cursor(0,1)
            self.lcd.message("Velocidade inicial")
            self.lcd.set_cursor(0,2)
            self.lcd.message("Altere o valor com")
            self.lcd.set_cursor(0,3)
            self.lcd.message("as setas cima/baixo")
        elif(Value == True):
            self.lcd.set_cursor(11,0)
            self.lcd.message(str(self.data.Incremento/10.0) + " Km/h ")

    def ConfigPressao(self,Value = False):
        #global self.data.Pressao
        if(Value == False):
            self.lcd.clear()
            self.lcd.set_cursor(0,0)
            self.lcd.message("Pressao=" + str(self.data.Pressao/10.0) + " cm H2O ")
            self.lcd.set_cursor(0,1)
            self.lcd.message("Pressao da camara")
            self.lcd.set_cursor(0,2)
            self.lcd.message("Altere o valor com")
            self.lcd.set_cursor(0,3)
            self.lcd.message("as setas cima/baixo")
        elif(Value == True):
            self.lcd.set_cursor(8,0)
            self.lcd.message(str(self.data.Pressao/10.0) + " cm H2O ")
          
    def ConfigInclinacao(self,Value = False):
        #global self.data.Inclinacao
        if(Value == False):
            self.lcd.clear()
            self.lcd.set_cursor(0,0)
            self.lcd.message("Inclinacao=" + str(self.data.Inclinacao) + " % ")
            self.lcd.set_cursor(0,1)
            self.lcd.message("Inclinacao da camara")
            self.lcd.set_cursor(0,2)
            self.lcd.message("Altere o valor com")
            self.lcd.set_cursor(0,3)
            self.lcd.message("as setas cima/baixo")
        elif(Value == True):
            self.lcd.set_cursor(11,0)
            self.lcd.message(str(self.data.Inclinacao) + " % ")


    # EstadoTeclado = {'left':False, 'down':False, 'up':False, 'right':False, 'confirm':False}			
    def UpdateLCD(self):
        
        MenuIndex = 0
        while True:

            if (self.data.EstadoTeclado['left'] == True):
                self.data.EstadoTeclado['left'] =  False
                MenuIndex -=1
            
            elif (self.data.EstadoTeclado['right'] == True):
                self.data.EstadoTeclado['right'] =  False
                MenuIndex +=1
            
            if(MenuIndex > 5):
                MenuIndex = 0
            elif(MenuIndex < 0):
                MenuIndex = 5
            
            if (MenuIndex == 0):
                if (self.data.ChangedScreen == True):
                    self.DisplayAll()
                    self.data.ChangedScreen = False
                    
            elif (MenuIndex == 1):
                
                if (self.data.ChangedScreen == True):
                    self.ConfigTempo(False)
                    self.data.ChangedScreen = False
                
                
                if (self.data.EstadoTeclado['up'] == True):
                    self.data.EstadoTeclado['up'] =  False
                    self.data.Tempo +=1
                    if (self.data.Tempo >30):
                        self.data.Tempo = 30
                    elif (self.data.Tempo <0):
                        self.data.Tempo = 0
                    self.ConfigTempo(True)
                    
                if (self.data.EstadoTeclado['down'] == True):
                    self.data.EstadoTeclado['down'] =  False
                    self.data.Tempo -=1
                    if (self.data.Tempo >30):
                        self.data.Tempo = 30
                    elif (self.data.Tempo <0):
                        self.data.Tempo = 0
                    self.ConfigTempo(True)

                    
            elif (MenuIndex == 2):
                
                if (self.data.ChangedScreen == True):
                    self.ConfigVelocidade(False)
                    self.data.ChangedScreen = False
                
                if (self.data.EstadoTeclado['up'] == True):
                    self.data.EstadoTeclado['up'] =  False
                    self.data.Velocidade +=1
                    if (self.data.Velocidade >30):
                        self.data.Velocidade = 30
                    elif (self.data.Velocidade <0):
                        self.data.Velocidade = 0
                    self.ConfigVelocidade(True)
                
                if (self.data.EstadoTeclado['down'] == True):
                    self.data.EstadoTeclado['down'] =  False
                    self.data.Velocidade -=1
                    if (self.data.Velocidade >30):
                        self.data.Velocidade = 30
                    elif (self.data.Velocidade <0):
                        self.data.Velocidade = 0
                    self.ConfigVelocidade(True)
            
            elif (MenuIndex == 3):
                
                if (self.data.ChangedScreen == True):
                    self.ConfigIncremento(False)
                    self.data.ChangedScreen = False
                
                if (self.data.EstadoTeclado['up'] == True):
                    self.data.EstadoTeclado['up'] =  False
                    self.data.Incremento +=0.1
                    if (self.data.Incremento >3):
                        self.data.Incremento = 3
                    elif (self.data.Incremento <0):
                        self.data.Incremento = 0
                    self.ConfigIncremento(True)
                
                if (self.data.EstadoTeclado['up'] == True):
                    self.data.EstadoTeclado['up'] =  False
                    self.data.Incremento -=0.1
                    if (self.data.Incremento >3):
                        self.data.Incremento = 3
                    elif (self.data.Incremento <0):
                        self.data.Incremento = 0
                    self.ConfigIncremento(True)
            
            elif (MenuIndex == 4):
                
                if (self.data.ChangedScreen == True):
                    self.ConfigPressao(False)
                    self.data.ChangedScreen = False
                    
                
                if (self.data.EstadoTeclado['up'] == True):
                    self.data.EstadoTeclado['up'] =  False
                    self.data.Pressao +=0.1
                    if (self.data.Pressao >20):
                        self.data.Pressao = 20
                    elif (self.data.Pressao <0):
                        self.data.Pressao = 0
                    self.ConfigPressao(True)
                    
                if (self.data.EstadoTeclado['down'] == True):
                    self.data.EstadoTeclado['dpwn'] =  False
                    self.data.Pressao -=0.1
                    if (self.data.Pressao >20):
                        self.data.Pressao = 20
                    elif (self.data.Pressao <0):
                        self.data.Pressao = 0
                    self.ConfigPressao(True)
            
            elif (MenuIndex == 5):
                
                if (self.data.ChangedScreen == True):
                    self.ConfigInclinacao(False)
                    self.data.ChangedScreen = False

                if (self.data.EstadoTeclado['up'] == True):
                    self.data.EstadoTeclado['up'] =  False
                    self.data.Inclinacao +=1
                    if (self.data.Inclinacao >30):
                        self.data.Inclinacao = 30
                    elif (self.data.Inclinacao <0):
                        self.data.Inclinacao = 0
                    self.ConfigInclinacao(True)
                
                if (self.data.EstadoTeclado['down'] == True):
                    self.data.EstadoTeclado['down'] =  False
                    self.data.Inclinacao -=1
                    if (self.data.Inclinacao >30):
                        self.data.Inclinacao = 30
                    elif (self.data.Inclinacao <0):
                        self.data.Inclinacao = 0
                    self.ConfigInclinacao(True)
                
        
            if (self.data.EstadoTeclado['confirm'] == True):
                self.data.EstadoTeclado['confirm'] =  False
  