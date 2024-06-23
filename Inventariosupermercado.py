class Product:
    """
    Clase para representar un producto.

    Atributos:
    ----------
    codigo : int
        Código del producto.
    nombre : str
        Nombre del producto.
    precio : float
        Precio del producto.
    cantidad : int
        Cantidad disponible del producto.
    """
    def __init__(self, codigo, nombre, precio, cantidad):
        """
        Inicializa una nueva instancia de la clase Product.

        Parámetros:
        -----------
        codigo : int
            Código del producto.
        nombre : str
            Nombre del producto.
        precio : float
            Precio del producto.
        cantidad : int
            Cantidad disponible del producto.
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_producto(self, producto):
        """
        Muestra los detalles de un producto.

        Parámetros:
        -----------
        producto : Product
            Instancia del producto a mostrar.
        """
        print("--------------------")
        print(f"Código: {producto.codigo}")
        print(f"Nombre: {producto.nombre}")
        print(f"Precio: {producto.precio}")
        print(f"Cantidad: {producto.cantidad}")
        print("--------------------")

class InventarioSuper:
    """
    Clase para gestionar el inventario de un supermercado.

    Atributos:
    ----------
    lista : list
        Lista que almacena los productos registrados en el inventario.
    """
    def __init__(self):
        """
        Inicializa una nueva instancia de la clase InventarioSuper.
        """
        self.lista = []

    def validar_numero(self, mensaje):
        """
        Valida que la entrada del usuario sea un número.

        Parámetros:
        -----------
        mensaje : str
            Mensaje a mostrar al usuario.

        Retorna:
        --------
        int
            El número validado.
        """
        cantidad = input(mensaje)
        if not cantidad.isnumeric():
            print("ERROR!: Número no válido, por favor intente de nuevo")
            print("--------------------\n")
            return self.validar_numero(mensaje)
    
        return int(cantidad)

    def registrar_producto(self):
        """
        Registra un nuevo producto en el inventario.
        """
        mensaje = "Para $ digite el número"
        menu = "----------MENÚ AGREGAR----------"
        regis = f"{mensaje.replace('$', 'registrar')} 1."
        reg = f"{mensaje.replace('$', 'regresar')} 2."
        print(f"\n{menu}\n{regis}\n{reg}")
        opcion = self.validar_numero("Ingrese el número: ")

        if opcion == 1:
            codigo = self.validar_numero("Escriba el código del producto: ")
            nombre = input("Escribe el nombre del producto: ")
            precio = self.validar_numero("Escriba el precio del producto: ")
            cantidad = self.validar_numero("Escriba la cantidad del producto: ")

            producto = Product(
                cantidad=int(cantidad),
                codigo=int(codigo),
                nombre=nombre.lower().capitalize(),
                precio=int(precio))

            for prod in self.lista:
                if prod.codigo == int(codigo):
                    print(f"\nProducto con código {codigo} ya se encuentra registrado, por favor intente de nuevo.")
                    print("--------------------")
                    return self.registrar_producto()
                elif prod.nombre == nombre.lower().capitalize():
                    print(f"\nProducto \"{nombre.lower().capitalize():}\" ya se encuentra registrado, por favor intente de nuevo.")
                    print("--------------------")
                    return self.registrar_producto()

            self.actualizar_lista(producto)
            print(f"\nProducto \"{nombre}\" con código {codigo} registrado correctamente.")
            print("--------------------")

            return self.registrar_producto()
        elif opcion == 2:
            print("--------------------\n")
            return self.inventario()
        else:
            print("ERROR!: Valor ingresado no válido, por favor intente de nuevo.")
            print("--------------------")
            return self.registrar_producto()

    def actualizar_lista(self, producto):
        """
        Añade un producto a la lista de inventario.

        Parámetros:
        -----------
        producto : Product
            El producto a añadir.
        """
        self.lista.append(producto)

    def buscar_producto(self):
        """
        Busca un producto en el inventario.
        """
        mensaje = "Para $ digite el número"
        menu = "----------MENÚ BUSCAR----------"
        cod = f"{mensaje.replace('$', 'buscar por código')} 1."
        nom = f"{mensaje.replace('$', 'buscar por nombre')} 2."
        tod = f"{mensaje.replace('$', 'todos los productos')} 3."
        reg = f"{mensaje.replace('$', 'regresar')} 4."
        print(f"\n{menu}\n{cod}\n{nom}\n{tod}\n{reg}")
        opcion = self.validar_numero("Ingrese el número: ")
        self.busqueda(opcion, 1)
        return self.buscar_producto()

    def busqueda(self, opcion, val):
        """
        Realiza la búsqueda de un producto.

        Parámetros:
        -----------
        opcion : int
            Opción seleccionada para la búsqueda.
        val : int
            Valor que indica el tipo de operación (1 para mostrar, 2 para devolver).
        """
        if opcion == 1:
            codigo = self.validar_numero("Escriba el código del producto: ")
        elif opcion == 2:
            codigo = input("Escriba el nombre del producto: ").lower().capitalize().replace(" ","")
        elif opcion == 3 and val == 1:
            if len(self.lista) > 0:
                for producto in self.lista:
                    Product.mostrar_producto(self, producto)
            else:
                print("No hay productos registrados, por favor intente de nuevo.")
                print("--------------------")
        elif opcion == 4:
            print("--------------------\n")
            return self.inventario()
        else:
            print("ERROR!: Valor ingresado no válido, por favor intente de nuevo.")
            print("--------------------")
        if opcion == 1:
            existe = False
            for producto in self.lista:
                if producto.codigo == codigo:
                    existe = True
                    if val == 1:
                        Product.mostrar_producto(self, producto)
                    else:
                        return producto

        if opcion == 2:
            existe = False
            for producto in self.lista:
                if producto.nombre == codigo:
                    existe = True
                    if val == 1:
                        Product.mostrar_producto(self, producto)
                    else:
                        return producto

            if not existe:
                print("El producto no se encuentra registrado, por favor intente de nuevo.")
                print("--------------------")

    def actualizar_producto(self):
        """
        Actualiza los detalles de un producto en el inventario.
        """
        mensaje = "Para $ digite el número"
        menu = "----------MENÚ ACTUALIZAR----------"
        cod = f"{mensaje.replace('$', 'buscar el producto a atualizar por código')} 1."
        nom = f"{mensaje.replace('$', 'buscar el producto a atualizar por nombre')} 2."
        reg = f"{mensaje.replace('$', 'regresar')} 3."
        print(f"\n{menu}\n{cod}\n{nom}\n{reg}")
        opcion = self.validar_numero("Ingrese el número: ")
        if opcion == 3:
            opcion = 4
        elif opcion >= 4:
            opcion = 5
        producto = self.busqueda(opcion, 2)
        if producto != None:
            indice = self.lista.index(producto)
            producto.precio = self.validar_numero("Escriba el precio del producto: ")
            producto.cantidad = self.validar_numero("Escriba la cantidad del producto: ")
            self.lista[indice] = producto
            print(f"\nProducto \"{producto.nombre}\" con código {producto.codigo} actualizado correctamente.")
            Product.mostrar_producto(self, producto)
        return self.actualizar_producto()

    def eliminar_producto(self):
        """
        Elimina un producto del inventario.
        """
        mensaje = "Para $ digite el número"
        menu = "----------MENÚ ELIMINAR----------"
        cod = f"{mensaje.replace('$', 'buscar el producto a eliminar por código')} 1."
        nom = f"{mensaje.replace('$', 'buscar el producto a eliminar por nombre')} 2."
        reg = f"{mensaje.replace('$', 'regresar')} 3."
        print(f"\n{menu}\n{cod}\n{nom}\n{reg}")
        opcion = self.validar_numero("Ingrese el número: ")
        if opcion == 3:
            opcion = 4
        elif opcion >= 4:
            opcion = 5
        producto = self.busqueda(opcion, 2)
        if producto != None:
            indice = self.lista.index(producto)
            del self.lista[indice]
            print(f"\nProducto \"{producto.nombre}\" con código {producto.codigo} elminado correctamente.")
            print("--------------------")
        return self.eliminar_producto()

    def inventario(self):
        """
        Muestra el menú principal de opciones para gestionar el inventario.
        """
        lista = {
            "agregar": self.registrar_producto,
            "buscar": self.buscar_producto,
            "actualizar": self.actualizar_producto,
            "eliminar": self.eliminar_producto,
            "salir": "Salir"
        }
        list_dic = list(lista.keys())
        print("Lista de procesos que se pueden realizar.")
        for clave in lista:
            print(f"{list_dic.index(clave) + 1}. {clave.capitalize()}")
        opcion = input("De la lista anterior escriba la opción que desea utilizar: ").lower().replace(" ","")

        if opcion == "salir":
            exit()

        if opcion not in lista:
            print("ERROR!!: La opción ingresada no es válida, por favor por favor intente de nuevo.")
            print("--------------------\n")
            return self.inventario()
    
        operacion = lista.get(opcion)
        operacion()
        return self.inventario()

# Ejemplo de uso del sistema de inventario

# Crear instancia de InventarioSuper
metodos = InventarioSuper()

# Crear y añadir un producto al inventario
producto = Product(
    cantidad=4,
    codigo=1,
    nombre="Arroz",
    precio=500
)
metodos.actualizar_lista(producto)

# Iniciar el menú de inventario
metodos.inventario()
