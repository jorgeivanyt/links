public class TiendaApp {
    public static void main(String[] args) {
        Inventario inventario = new Inventario();

        // 1. Crear al menos 3 productos (combinando alimentos y electrónicos)
        Producto p1 = new ProductoAlimenticio("A001", "Leche Entera 1L", 4500.0, "2026-12-15");
        Producto p2 = new ProductoAlimenticio("A002", "Arroz Premium 1Kg", 5200.0, "2027-06-30");
        Producto p3 = new ProductoElectronico("E001", "Licuadora 5 Velocidades", 145000.0, 110);

        // Agregarlos al inventario
        inventario.agregarProducto(p1);
        inventario.agregarProducto(p2);
        inventario.agregarProducto(p3);

        // 2. Mostrar todo el inventario
        inventario.mostrarInventario();
        System.out.println();

        // 3. Buscar un producto que SÍ existe
        System.out.println("--- Búsqueda de producto existente ---");
        try {
            Producto encontrado = inventario.buscarProducto("A001");
            System.out.println("Producto localizado: " + encontrado);
        } catch (ProductoNoEncontradoException e) {
            System.out.println("Error: " + e.getMessage());
        }

        System.out.println();

        // 4. Buscar un producto que NO existe
        System.out.println("--- Búsqueda de producto inexistente ---");
        try {
            Producto noExiste = inventario.buscarProducto("X999");
            System.out.println("Producto localizado: " + noExiste);
        } catch (ProductoNoEncontradoException e) {
            System.out.println("Aviso al usuario: " + e.getMessage());
        }
    }
}