class SingletonObservable:
    "Base reutilizable: da Singleton + Observer a cualquier clase que herede de ella."

    _instancias = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instancias:
            instancia = super().__new__(cls)
            instancia._observadores = []
            cls._instancias[cls] = instancia
        return cls._instancias[cls]

    def suscribir(self, funcion_observadora):
        "Agrega una función a la lista de observadores."
        self._observadores.append(funcion_observadora)

    def notificar(self, *args, **kwargs):
        "Notifica a todos los observadores registrados enviando cualquier argumento."
        for funcion in self._observadores:
            funcion(*args, **kwargs)