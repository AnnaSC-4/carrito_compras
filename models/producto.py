class Producto:
    def __init__(self, nombre: str, precio: float, stock: int):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f} (Stock: {self.stock})"
    
    def __repr__(self):
        return f"Producto('{self.nombre}', {self.precio}, {self.stock})"
    
    def actualizar_stock(self, cantidad: int):
        """Actualiza el stock del producto"""
        if self.stock + cantidad >= 0:
            self.stock += cantidad
            return True
        return False
