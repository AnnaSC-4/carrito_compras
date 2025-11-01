from .item_carrito import ItemCarrito
from .producto import Producto

class CarritoCompras:
    def __init__(self):
        self.items = []
    
    def agregar_producto(self, producto: Producto, cantidad: int = 1) -> bool:
        """Agrega un producto al carrito"""
        if cantidad <= 0:
            return False
        
        if producto.stock < cantidad:
            print(f"Stock insuficiente. Solo hay {producto.stock} unidades de {producto.nombre}")
            return False
        
        # Verificar si el producto ya está en el carrito
        for item in self.items:
            if item.producto.nombre == producto.nombre:
                item.cantidad += cantidad
                return True
        
        # Si no está, agregar nuevo item
        self.items.append(ItemCarrito(producto, cantidad))
        return True
    
    def eliminar_producto(self, nombre_producto: str, cantidad: int = None) -> bool:
        """Elimina un producto del carrito o reduce su cantidad"""
        for i, item in enumerate(self.items):
            if item.producto.nombre == nombre_producto:
                if cantidad is None or cantidad >= item.cantidad:
                    # Eliminar completamente el item
                    self.items.pop(i)
                    return True
                else:
                    # Reducir cantidad
                    item.cantidad -= cantidad
                    if item.cantidad <= 0:
                        self.items.pop(i)
                    return True
        return False
    
    def calcular_total(self) -> float:
        """Calcula el total de la compra"""
        return sum(item.subtotal for item in self.items)
    
    def vaciar_carrito(self):
        """Vacía todo el carrito"""
        self.items.clear()
    
    def mostrar_carrito(self):
        """Muestra el contenido del carrito"""
        if not self.items:
            print("El carrito está vacío")
            return
        
        print("--- Carrito de Compras ---")
        for i, item in enumerate(self.items, 1):
            print(f"{i}. {item}")
        print(f"Total: ${self.calcular_total():.2f}")
        print("-" * 25)
    
    def realizar_compra(self) -> bool:
        """Realiza la compra, actualizando el stock de productos"""
        if not self.items:
            print("El carrito está vacío")
            return False
        
        # Verificar stock antes de realizar la compra
        for item in self.items:
            if item.producto.stock < item.cantidad:
                print(f"Stock insuficiente para {item.producto.nombre}")
                return False
        
        # Actualizar stock
        for item in self.items:
            item.producto.actualizar_stock(-item.cantidad)
        
        print("¡Compra realizada exitosamente!")
        self.vaciar_carrito()
        return True
