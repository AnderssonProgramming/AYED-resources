from uuid import uuid1
from random import randint, choice

class BasketballT_shirts:
    def __init__(self, nombre, idProducto):
        self.nombre = ""
        self.idProducto = None
        self.talla = choice(["6", "8", "10", "12", "14", "16", "18",  "S", "M", "L", "XL", "XXL", "XXXL"])
        self.categoria = "infantil" if self.talla in ["6", "8", "10", "12", "14", "16"] else "juvenil"
        self.genero = choice(["masculino", "femenino"])
        self.tipoManga = choice(["corta", "larga"])
        self.tipoCamisa = choice([ "solo con el logo del equipo", "solo con el jugador en específico"])
        self.tipoPersonalizacion = choice(["con estampado","sin estampado"])
        self.uso = choice(["entrenamiento", "partidos"])
        self.tipoMaterial = choice(["algodón", "licra"])
        self.precio = randint(10, 100)
        self.cantidad = randint(1, 10)
        self.totalDescuento = 0.0

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        if not isinstance (nombre, str):
            raise Exception ("El nombre no corresponde al tipo de dato esperado")
        self.nombre = nombre

    def getId(self):
        return self.idProducto

    def setId(self, idProducto):
        if not (isinstance (id, int) or int is None):
            raise Exception ("El id no corresponde al tipo de dato esperado")
        self.idProducto = idProducto

    def calcularDescuento(self):
        if self.cantidad >= 3:
            self.totalDescuento = self.precio * self.cantidad-(self.precio * self.cantidad * 0.2)
        if self.cantidad < 3:
            self.totalDescuento = self.precio * self.cantidad

        return self.totalDescuento

    def __str__(self):
        return "Basketball T_shirts({}, {}, {}, {},{}, {}, {}, {},{}, {}, {})".format(self.nombre, self.idProducto, self.talla, self.categoria, self.genero, self.tipoManga, self.tipoPersonalizacion, self.uso, self.tipoMaterial, self.precio, self.cantidad)

def main():
    camisetas = [BasketballT_shirts(str(uuid1()), randint(0,int(1e6))) for i in range(10)]
    for camiseta in camisetas:
        camiseta.nombre = str(uuid1 ())
        camiseta.idProducto = randint(0, int (1e6))
        print(camiseta)
        print("Descuento:",camiseta.calcularDescuento())

main()

camiseta_especifica = BasketballT_shirts("Camiseta Lakers", 123)
camiseta_especifica.talla = "M"
camiseta_especifica.categoria = "juvenil"
camiseta_especifica.genero = "masculino"
camiseta_especifica.tipoManga = "corta"
camiseta_especifica.tipoPersonalizacion = "con estampado"
camiseta_especifica.uso = "partidos"
camiseta_especifica.tipoMaterial = "algodón"
camiseta_especifica.precio = 50
camiseta_especifica.cantidad = 5

print(f"Descuento: {camiseta_especifica.calcularDescuento()}")
