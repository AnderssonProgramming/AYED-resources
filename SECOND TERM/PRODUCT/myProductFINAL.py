from uuid import uuid1

class BasketballT_shirts:
    def __init__(self,cantidad):
        self.cantidadCamisetas = cantidad
        self.cantidadCadaUna = None
        self.nombre = None
        self.idProducto = None
        self.talla = None
        self.categoria = None
        self.genero = None
        self.tipoManga = None
        self.tipoCamisa = None
        self.tipoPersonalizacion = None
        self.tipoEstampado = None
        self.uso = None
        self.tipoMaterial = None
        self.precio = None
        self.descuento = None
        self.precio_con_descuento = None
        self.precioTotal = None
        self.atributosProducto()
        self.validar_atributos()

    def atributosProducto(self):
        print ("NOMBRE --> {},{},{},{},{}".format (
            "Estándar", "MangaL", "MaterialL", "EstampadoNu", "EstampadoNo"))

        print ("TALLA --> {},{},{},{},{},{},{},{},{},{},{},{},{}".format (
            "6", "8", "10", "12", "14", "16", "18", "S", "M", "L", "XL", "XXL", "XXXL"))

        print ("GÉNERO --> {},{}".format ("masculino", "femenino"))

        print ("TIPO DE MANGA --> {},{}".format ("corta", "larga"))

        print ("TIPO DE CAMISA --> {},{}".format (
            "solo con el logo del equipo", "solo con el jugador en específico"))

        print ("TIPO DE PERSONALIZACIÓN --> {},{}".format ("con estampado", "sin estampado"))

        print ("USO --> {},{}".format ("entrenamiento", "partidos"))

        print ("TIPO DE MATERIAL --> {},{}".format ("algodón", "licra"))

    def validar_atributos(self):

        self.nombre = input("Digite el nombre de la camiseta que quiere: ")
        while self.nombre not in ("Estándar", "MangaL", "MaterialL", "EstampadoNu", "EstampadoNo"):
            print("El nombre de camiseta que ingresó no es válido")
            self.nombre = input("Digite el nombre de la camiseta que quiere: ")

        self.idProducto = str(uuid1())

        self.cantidadCadaUna = int(input("Digite la cantidad de camisetas que quiere de esta: "))

        self.talla = input("Digite la talla que necesita: ")
        while self.talla not in (
                "6", "8", "10", "12", "14", "16", "18",  "S", "M", "L", "XL", "XXL", "XXXL"):
            print("La talla que ingresó no es válida")
            self.talla = input("Digite la talla que necesita: ")

        self.categoria = "infantil" if self.talla in ["6", "8", "10", "12"] else (
            "juvenil" if self.talla in ["14", "16", "18"] else "mayores")

        self.genero = input("Masculino o femenino?: ")
        while self.genero not in ("masculino", "femenino"):
            print("El género que ingresó no es válido")
            self.genero = input("Masculino o femenino?: ")

        self.tipoManga = input("Digite el tipo de manga que desea: ")
        while self.tipoManga not in ("corta", "larga"):
            print("El tipo de manga que ingresó no es válido")
            self.tipoManga = input("Digite el tipo de manga que desea: ")

        self.tipoCamisa = input("Digite el tipo de camisa que desea: ")
        while self.tipoCamisa not in (
                "solo con el logo del equipo", "solo con el jugador en específico"):
            print("El tipo de camisa que ingresó no es válido")
            self.tipoCamisa = input("Digite el tipo de camisa que desea: ")

        self.tipoPersonalizacion = input("Digite el tipo de personalización que desea: ")
        while self.tipoPersonalizacion not in (
                "con estampado", "sin estampado"):
            print("El tipo de personalización que ingresó no es válido")
            self.tipoPersonalizacion = input("Digite el tipo de personalización que desea: ")

        if self.tipoPersonalizacion == "con estampado":
            self.tipoEstampado = input("Digite el tipo de estampado (con número, con nombre o ambos): ")
            while self.tipoEstampado not in ("con número", "con nombre", "ambos"):
                print("El tipo de estampado que ingresó no es válido")
                self.tipoEstampado = input("Digite el tipo de estampado (con número, con nombre o ambos): ")

        self.uso = input("Digite el uso de la camiseta: ")
        while self.uso not in ("entrenamiento", "partidos"):
            print("El uso de la camiseta que ingresó no es válido")
            self.uso = input("Digite el uso de la camiseta: ")

        self.tipoMaterial = input("Digite el tipo de material: ")
        while self.tipoMaterial not in ("algodón", "licra"):
            print("El tipo de material que ingresó no es válido")
            self.tipoMaterial = input("Digite el tipo de material: ")

        self.precio = self.calcular_precio_estandar()
        self.descuento = self.calcularDescuento()
        self.precio_con_descuento = self.calcular_precio_con_descuento()
        self.precioTotal = self.calcular_precio_Total()

    def calcular_precio_estandar(self):
        precio_base = 0
        if self.categoria == "infantil" and (self.tipoCamisa == "solo con el logo del equipo" or self.tipoCamisa == "solo con el jugador en específico"):
            precio_base = 60000
        elif self.categoria == "juvenil" and (self.tipoCamisa == "solo con el logo del equipo" or self.tipoCamisa == "solo con el jugador en específico"):
            precio_base = 70000
        elif self.categoria == "mayores" and (self.tipoCamisa == "solo con el logo del equipo" or self.tipoCamisa == "solo con el jugador en específico"):
            precio_base = 75000

        if self.tipoManga == "larga":
            precio_base += 5000

        if self.tipoPersonalizacion == "con estampado" and (self.tipoEstampado == "con número" or self.tipoEstampado == "con nombre" ):
            precio_base += 5000

        if self.tipoPersonalizacion == "con estampado" and (self.tipoEstampado == "ambos"):
            precio_base += 10000

        if self.tipoMaterial == "licra":
            precio_base += 10000

        return precio_base

    def calcularDescuento(self):
        descuento = 0.0
        if self.cantidadCamisetas >= 3:
            descuento = self.precio * self.cantidadCadaUna * 0.2
        return descuento

    def calcular_precio_con_descuento(self):
        precio_con_descuento = self.precio * self.cantidadCadaUna - self.calcularDescuento()
        return precio_con_descuento

    def calcular_precio_Total(self):
        precioTotal = self.precio_con_descuento
        return precioTotal

    def __str__(self):
        return "BasketballT_shirts({}, {}, {}, {},{}, {}, {}, {},{}, {}, {})".format(
            self.nombre, self.idProducto, self.talla, self.categoria, self.genero, self.tipoManga,
            self.tipoPersonalizacion, self.uso, self.tipoMaterial, self.precio, self.cantidadCamisetas
        )

class Carrito:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)
        print(f"Camiseta {item.nombre} agregada al carrito.")

    def eliminar_item(self, nombre):
        for item in self.items:
            if item.nombre == nombre:
                self.items.remove(item)
                print(f"Camiseta {nombre} eliminada del carrito.")
                return
        print("Camiseta no encontrada en el carrito.")

    def editar_item(self, nombre):
        for item in self.items:
            if item.nombre == nombre:
                nuevo_nombre = input("Ingrese el nuevo nombre del item: ")
                item.nombre = nuevo_nombre
                print(f"Camiseta {nombre} editada a {nuevo_nombre}.")
                return
        print("Camiseta no encontrada en el carrito.")

    def mostrar_carrito(self):
        for item in self.items:
            print(f"\nCamiseta: {item.nombre}, ID: {item.idProducto}, Talla: {item.talla}, Categoría: {item.categoria}")
            print(f"Género: {item.genero}, Tipo de manga: {item.tipoManga}")
            print(f"Tipo de camisa: {item.tipoCamisa}, Tipo de personalización: {item.tipoPersonalizacion}")
            print(f"Uso: {item.uso}, Tipo de material: {item.tipoMaterial}")
            print(f"Precio: {item.precio}, Cantidad: {item.cantidadCadaUna}, Descuento: {item.descuento}")
            print(f"Precio con descuento: {item.precio_con_descuento}")

    def mostrar_precio_total(self):
        precio_total_definitivo = 0
        for item in self.items:
            precio_total_definitivo += item.calcular_precio_Total()  # Sumar el precio total de cada camiseta
        print(f"Precio total definitivo: {precio_total_definitivo}")

def main():
    carrito = Carrito()

    while True:
        print("\n1. Agregar camiseta al carrito")
        print("2. Eliminar camiseta del carrito")
        print("3. Editar camiseta en el carrito")
        print("4. Mostrar carrito")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            cantidad = int(input("Digite la cantidad de productos que necesita: "))
            for j in range(cantidad):
                camiseta = BasketballT_shirts(cantidad)
                carrito.agregar_item(camiseta)

        elif opcion == "2":
            nombre = input("Ingrese el nombre de la camiseta que quiere eliminar: ")
            carrito.eliminar_item(nombre)

        elif opcion == "3":
            nombre = input("Ingrese el nombre de la camiseta que quiere editar: ")
            carrito.editar_item(nombre)

        elif opcion == "4":
            carrito.mostrar_carrito()
            carrito.mostrar_precio_total()

        elif opcion == "5":
            break

if __name__ == "__main__":
    main()