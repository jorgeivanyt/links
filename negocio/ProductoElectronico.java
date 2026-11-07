public class ProductoElectronico extends Producto {
    private int voltaje;

    public ProductoElectronico(String codigo, String nombre, double precio, int voltaje) {
        super(codigo, nombre, precio);
        this.voltaje = voltaje;
    }

    public int getVoltaje() {
        return voltaje;
    }

    @Override
    public String toString() {
        return super.toString() + " | Tipo: Electrónico | Voltaje: " + voltaje + "V";
    }
}