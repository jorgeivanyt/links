import java.util.HashMap;

public class Inventario {
    private HashMap<String, Producto> productos;

    public Inventario() {
        this.productos = new HashMap<>();
    }

    public void agregarProducto(Producto producto) {
        productos.put(producto.getCodigo(), producto);
    }

    public Producto buscarProducto(String codigo) throws ProductoNoEncontradoException {
        Producto encontrado = productos.get(codigo);
        if (encontrado == null) {
            throw new ProductoNoEncontradoException("El producto con código " + codigo + " no fue encontrado.");
        }
        return encontrado;
    }

    public void mostrarInventario() {
        System.out.println("=== Listado de Inventario: Tienda El Éxito ===");
        for (Producto p : productos.values()) {
            System.out.println(p.toString());
        }
    }
}