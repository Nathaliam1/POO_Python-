
class Automovil:

    def __init__(self, modelo, marca, color, trasmision):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en_reposo'
        self._motor = Motor(cilindros=4)
        self.trasmision = Transmision (mecanica=True, automatica=False)

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
            self.trasmision.hibridar(1)
        else:
            self._motor.inyecta_gasolina(3)
            self.trasmision.hibridar(0)
    
        self._estado ='en_movimiento'


class Motor:

    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0

    def inyecta_gasolina(self, cantidad):
        pass

class Transmision:
    def __init__(self, mecanica, automatica):
        self.mecanica = mecanica
        self.automatica = automatica
    def hibridar(self,cambio):
        if cambio == 1:
            self.transmision (atomatica=True)
            self.transmision (mecanica=True)