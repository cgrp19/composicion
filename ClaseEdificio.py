from ClaseDepartamento import Departamento

class Edificio:
    __id: int
    __nombre: str
    __direccion: str
    __empconstrutora: str
    __cantpisos: int
    __cantdeptos: int
    __departamentos: list

    def __init__(self, id: int, nombre: str, dir: str, emp: str, pisos: int, deptos: int) -> None:
        self.__id = id
        self.__nombre = nombre
        self.__direccion = dir
        self.__empconstrutora = emp
        self.__cantpisos = pisos
        self.__cantdeptos = deptos
        self.__departamentos = []

    def getId(self):
        return self.__id
    
    def getNombre(self):
        return self.__nombre
    
    def getDireccion(self):
        return self.__direccion
    
    def getEmpconstrutora(self):
        return self.__empconstrutora
    
    def getCantpisos(self):
        return self.__cantpisos
    
    def getCantdeptos(self):
        return self.__cantdeptos
    
    def AgregarDepartamento(self, id, due, nom, piso, depto, hab, baños, sup):
        undepartamento = Departamento(id, due, nom, piso, depto, hab, baños, sup)
        self.__departamentos.append(undepartamento)