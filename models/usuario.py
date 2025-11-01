from .carrito_compras import CarritoCompras

class Usuario:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.carrito_actual = CarritoCompras()
        self.historial_compras = []
    
    def agregar_al_carrito(self, producto, cantidad: int = 1):
        """Agrega un producto al carrito actual"""
        return self.carrito_actual.agregar_producto(producto, cantidad)
    
    def eliminar_del_carrito(self, nombre_producto: str, cantidad: int = None):
        """Elimina un producto del carrito actual"""
        return self.carrito_actual.eliminar_producto(nombre_producto, cantidad)
    
    def realizar_compra(self):
        """Realiza la compra y la agrega al historial"""
        total = self.carrito_actual.calcular_total()
        if total > 0 and self.carrito_actual.realizar_compra():
            self.historial_compras.append({
                'fecha': '2024-01-01',  # En una app real usarías datetime.now()
                'total': total
            })
            return True
        return False
    
    def mostrar_historial(self):
        """Muestra el historial de compras del usuario"""
        if not self.historial_compras:
            print("No hay compras en el historial")
            return
        
        print(f"--- Historial de Compras de {self.nombre} ---")
        for i, compra in enumerate(self.historial_compras, 1):
            print(f"{i}. Fecha: {compra['fecha']} - Total: ${compra['total']:.2f}")
