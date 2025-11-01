from .producto import Producto

class ItemCarrito:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad
    
    @property
    def subtotal(self) -> float:
        """Calcula el subtotal del item"""
        return self.producto.precio * self.cantidad
    
    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad} = ${self.subtotal:.2f}"
    
    def __repr__(self):
        return f"ItemCarrito({repr(self.producto)}, {self.cantidad})"
