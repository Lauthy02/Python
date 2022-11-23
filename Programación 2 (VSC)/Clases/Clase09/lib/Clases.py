class Persona:
    _nombre = None
    _edad = None
    
    #constructor
    
    #destructor

    #getter y setter
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, value):
        self._nombre = value
    nombre = property(get_nombre, set_nombre)
    
    def calc_edad():
        return 20

class Operador(Persona):
    #constructor
    
    #destructor
    
    def calc_edad():
        super().calc_edad