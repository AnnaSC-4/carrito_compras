from models import Producto, Usuario

def main():
    # Crear algunos productos de ejemplo
    productos = [
        Producto("Laptop", 1200.00, 10),
        Producto("Mouse", 25.50, 50),
        Producto("Teclado", 75.00, 30),
        Producto("Monitor", 300.00, 15),
        Producto("Auriculares", 45.00, 25)
    ]
    
    # Crear usuario
    usuario = Usuario("Juan Pérez")
    
    while True:
        print("\n=== SISTEMA DE CARRITO DE COMPRAS ===")
        print("1. Ver productos disponibles")
        print("2. Agregar producto al carrito")
        print("3. Ver carrito")
        print("4. Eliminar producto del carrito")
        print("5. Realizar compra")
        print("6. Ver historial de compras")
        print("7. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            print("\n--- Productos Disponibles ---")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")
        
        elif opcion == "2":
            print("\n--- Agregar al Carrito ---")
            for i, producto in enumerate(productos, 1):
                print(f"{i}. {producto}")
            
            try:
                idx = int(input("Seleccione el número del producto: ")) - 1
                if 0 <= idx < len(productos):
                    cantidad = int(input("Cantidad: "))
                    if usuario.agregar_al_carrito(productos[idx], cantidad):
                        print("Producto agregado al carrito")
                    else:
                        print("Error al agregar producto")
                else:
                    print("Número de producto inválido")
            except ValueError:
                print("Por favor, ingrese un número válido")
        
        elif opcion == "3":
            usuario.carrito_actual.mostrar_carrito()
        
        elif opcion == "4":
            if not usuario.carrito_actual.items:
                print("El carrito está vacío")
                continue
            
            usuario.carrito_actual.mostrar_carrito()
            try:
                idx = int(input("Seleccione el número del producto a eliminar: ")) - 1
                if 0 <= idx < len(usuario.carrito_actual.items):
                    producto_nombre = usuario.carrito_actual.items[idx].producto.nombre
                    cantidad = input("Cantidad a eliminar (dejar vacío para eliminar todo): ")
                    if cantidad.strip() == "":
                        usuario.eliminar_del_carrito(producto_nombre)
                        print("Producto eliminado del carrito")
                    else:
                        usuario.eliminar_del_carrito(producto_nombre, int(cantidad))
                        print("Cantidad reducida")
                else:
                    print("Número de producto inválido")
            except ValueError:
                print("Por favor, ingrese un número válido")
        
        elif opcion == "5":
            if usuario.realizar_compra():
                print("¡Compra realizada con éxito!")
            else:
                print("No se pudo realizar la compra")
        
        elif opcion == "6":
            usuario.mostrar_historial()
        
        elif opcion == "7":
            print("¡Gracias por usar nuestro sistema!")
            break
        
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()
