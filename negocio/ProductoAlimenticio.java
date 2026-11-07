public class ProductoAlimenticio extends Producto {
    private String fechaCaducidad;

    public ProductoAlimenticio(String codigo, String nombre, double precio, String fechaCaducidad) {
        super(codigo, nombre, precio);
        this.fechaCaducidad = fechaCaducidad;
    }

    public String getFechaCaducidad() {
        return fechaCaducidad;
    }

    @Override
    public String toString() {
        return super.toString() + " | Tipo: Alimento | Caducidad: " + fechaCaducidad;
    }
}