class Participante:
    def __init__(self, rut: str, nombre: str, edad: int):
        self._rut: str = rut
        self._nombre: str = nombre
        self._edad: int = edad

    def presentarse(self) -> str:
        return f"Hola mi nombre es {self._nombre} y mi edad es {self._edad}"
    def __str__(self):
        return "Me estas tratando como un string"



participante1 : Participante = Participante("22110005-k", "Cangri", 26)
print (participante1.presentarse())