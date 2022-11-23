class Banco:
    _nombre = None
    _listaClientes = []
    _listaCuentas = []

    def mostrarClientes():
        pass
    def mostrarCuentas():
        pass

class Cuenta:
    _saldo = None

    #getter y setter
    def getSaldo(self):
        return self._saldo

    def setSaldo(self, value):
        self._saldo = value

    saldo = property(getSaldo,setSaldo)
    ###############

    def retirarDinero(self, importe):
        self._saldo -= importe

    def ingresarDinero(self, importe):
        self._saldo += importe


class CtaCorriente(Cuenta):
    def retirarDinero(self, importe):
        importe += importe * 1.005
        if(self._saldo - importe > -2000):
            super().retirarDinero()

class CtaCajaAhorro(Cuenta):
    def retirarDinero(self, importe):
        if(self._saldo - importe > 0):
            super().retirarDinero(importe)

class Cliente:
    _nombre = None
    _CC = None
    _CA = None

    def getCC(self):
        return self._CC
    def setCC(self, value):
        self._CC = value
    cc = property(getCC,setCC)

    def getCA(self):
        return self._CA
    def setCA(self, value):
        self._CA = value
    ca = property(getCA,setCA)
