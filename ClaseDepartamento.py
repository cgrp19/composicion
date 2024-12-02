class Departamento:
    __id: int
    __dueño: int
    __nombre: str
    __piso: int
    __departamento: int
    __habitaciones: int
    __baños: int
    __superficie: float

    def __init__(self, id: int, dueño ,nombre: str, piso: int, departamento: int, habitaciones, baños: int, superficie: float) -> None:
        self.__id = id
        self.__dueño = dueño
        self.__nombre = nombre
        self.__piso = piso
        self.__departamento = departamento
        self.__habitaciones = habitaciones
        self.__baños = baños
        self.__superficie = superficie

    def getId(self):
        return self.__id
    
    def getDueño(self):
        return self.__dueño

    def getNombre(self):
        return self.__nombre
    
    def getPiso(self):
        return self.__piso
    
    def getDepartamento(self):
        return self.__departamento
    
    def getHabitaciones(self):
        return self.__habitaciones
    
    def getBaños(self):
        return self.__baños
    
    def getSuperficie(self):
        return self.__superficie