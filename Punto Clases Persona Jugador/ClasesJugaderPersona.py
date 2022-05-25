from datetime import date


class Persona:
    nombre : str
    nif : str
    fechaNac : date
#========================================

class Jugador(Persona):
    numFed: int