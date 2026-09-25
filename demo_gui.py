import ttkbootstrap as ttk
from singleton_obs import SingletonObservable
from ttkbootstrap.constants import *


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

class GestorAerolineas(SingletonObservable):

    def __init__(self):
        if not hasattr(self, "vuelos"):
            self.vuelos = []

    def registrar(self, vuelo):
        self.vuelos.append(vuelo)
        self.notificar(vuelo)

class GestorJoyeria(SingletonObservable):

    def __init__(self):
        if not hasattr(self, "ventas"):
            self.ventas = []

    def registrar(self, venta):
        self.ventas.append(venta)
        self.notificar(venta)

app = ttk.Window(
    title="Demo Librería SingletonObservable", themename="flatly"
)
app.geometry("640x420")

notebook = ttk.Notebook(app)
notebook.pack(fill=BOTH, expand=True, padx=10, pady=10)


tab_biblioteca = ttk.Frame(notebook)
notebook.add(tab_biblioteca, text="Biblioteca DEPB")

tabla_prestamos = ttk.Treeview(
    tab_biblioteca, columns=("libro", "multa"), show="headings"
)
tabla_prestamos.heading("libro", text="Libro")
tabla_prestamos.heading("multa", text="Multa ($)")
tabla_prestamos.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_biblioteca = GestorPrestamos()


def refrescar_prestamos(_=None):
    tabla_prestamos.delete(*tabla_prestamos.get_children())
    for p in gestor_biblioteca.prestamos:
        tabla_prestamos.insert("", "end", values=(p["libro"], p["multa"]))


gestor_biblioteca.suscribir(refrescar_prestamos)

ttk.Button(
    tab_biblioteca,
    text="Agregar préstamo de prueba",
    bootstyle="success",
    command=lambda: gestor_biblioteca.registrar(
        {"libro": "1984", "multa": 5.0}
    ),
).pack(pady=8)


tab_jugueteria = ttk.Frame(notebook)
notebook.add(tab_jugueteria, text="Juguetería DEPB")

tabla_ventas = ttk.Treeview(
    tab_jugueteria, columns=("juguete", "total"), show="headings"
)
tabla_ventas.heading("juguete", text="Juguete")
tabla_ventas.heading("total", text="Total ($)")
tabla_ventas.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_jugueteria = GestorVentas()


def refrescar_ventas(_=None):
    tabla_ventas.delete(*tabla_ventas.get_children())
    for v in gestor_jugueteria.ventas:
        tabla_ventas.insert("", "end", values=(v["juguete"], v["total"]))


gestor_jugueteria.suscribir(refrescar_ventas)

ttk.Button(
    tab_jugueteria,
    text="Agregar venta de prueba",
    bootstyle="success",
    command=lambda: gestor_jugueteria.registrar(
        {"juguete": "Robot", "total": 150.0}
    ),
).pack(pady=8)

tab_aerolinea = ttk.Frame(notebook)
notebook.add(tab_aerolinea, text="Aerolínea DEPB")

tabla_vuelos = ttk.Treeview(
    tab_aerolinea, columns=("vuelo", "destino"), show="headings"
)
tabla_vuelos.heading("vuelo", text="Código de Vuelo")
tabla_vuelos.heading("destino", text="Destino")
tabla_vuelos.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_aerolinea = GestorAerolineas()


def refrescar_vuelos(_=None):
    tabla_vuelos.delete(*tabla_vuelos.get_children())
    for v in gestor_aerolinea.vuelos:
        tabla_vuelos.insert("", "end", values=(v["vuelo"], v["destino"]))


gestor_aerolinea.suscribir(refrescar_vuelos)

ttk.Button(
    tab_aerolinea,
    text="Agregar vuelo de prueba",
    bootstyle="info",
    command=lambda: gestor_aerolinea.registrar(
        {"vuelo": "LA-2401", "destino": "Santiago"}
    ),
).pack(pady=8)

tab_joyeria = ttk.Frame(notebook)
notebook.add(tab_joyeria, text="Joyería DEPB")

tabla_joyas = ttk.Treeview(
    tab_joyeria, columns=("joya", "precio"), show="headings"
)
tabla_joyas.heading("joya", text="Joya / Artículo")
tabla_joyas.heading("precio", text="Precio ($)")
tabla_joyas.pack(fill=BOTH, expand=True, padx=10, pady=10)

gestor_joyeria = GestorJoyeria()


def refrescar_joyas(_=None):
    tabla_joyas.delete(*tabla_joyas.get_children())
    for j in gestor_joyeria.ventas:
        tabla_joyas.insert("", "end", values=(j["joya"], j["precio"]))


gestor_joyeria.suscribir(refrescar_joyas)

ttk.Button(
    tab_joyeria,
    text="Agregar joya de prueba",
    bootstyle="warning",
    command=lambda: gestor_joyeria.registrar(
        {"joya": "Anillo de Oro", "precio": 450.0}
    ),
).pack(pady=8)

if __name__ == "__main__":
    app.mainloop()