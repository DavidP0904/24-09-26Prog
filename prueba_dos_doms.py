from singleton_obs import SingletonObservable


class GestorPrestamos(SingletonObservable):

    def __init__(self):
        if not hasattr(self, "prestamos"):
            self.prestamos = []

    def registrar(self, prestamo):
        self.prestamos.append(prestamo)
        self.notificar(prestamo)


class GestorVentas(SingletonObservable):

    def __init__(self):
        if not hasattr(self, "ventas"):
            self.ventas = []

    def registrar(self, venta):
        self.ventas.append(venta)
        self.notificar(venta)


class GestorAerolinea(SingletonObservable):

    def __init__(self):
        if not hasattr(self, "vuelos"):
            self.vuelos = []

    def registrar_vuelo(self, vuelo):
        self.vuelos.append(vuelo)
        self.notificar(vuelo)


class GestorJoyeria(SingletonObservable):

    def __init__(self):
        if not hasattr(self, "joyas"):
            self.joyas = []

    def registrar_joya(self, joya):
        self.joyas.append(joya)
        self.notificar(joya)


# # Pruebas de verificación de Singleton por clase
gestor_biblioteca = GestorPrestamos()
gestor_jugueteria = GestorVentas()
otro_gestor_biblioteca = GestorPrestamos()

# Corrección de nombres al instanciar (GestorAerolinea sin 's' al final)
gestor_aerolinea = GestorAerolinea()
gestor_joyeria = GestorJoyeria()

print(
    "¿Mismo gestor de biblioteca?",
    gestor_biblioteca is otro_gestor_biblioteca,
)
print(
    "¿Biblioteca y juguetería son gestores distintos?",
    gestor_biblioteca is not gestor_jugueteria,
)
print("¿Mismo gestor de aerolínea?", gestor_aerolinea is GestorAerolinea())
print("¿Mismo gestor de joyería?", gestor_joyeria is GestorJoyeria())