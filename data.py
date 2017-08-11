import time

class Data(object):
    
    def __init__(self):
        
        self.Velocidade = 0
        self.Incremento = 0
        self.Inclinacao = 0
        self.Pressao = 0
        self.Tempo = 0
        self.ChangedScreen = False
        self.Start = 0
        self.ValueOnly = False
        self.Passo = 8
        self.CurrentFrequency = 1
        self.TargetFrequency = 1
        self.Diametro = 0.35
        self.StartPWM = True;
        self.TempoFinal = time.time()
        self.EstadoTeclado = {'left':False, 'down':False, 'up':False, 'right':False, 'confirm':False}
