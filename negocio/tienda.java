public class tienda {

    public static abstract class Producto {
        private String codigo;
        private String nombre;
        private double precio;

        public Producto(String codigo, String nombre, double precio) {
            this.codigo = codigo;
            this.nombre = nombre;
            this.precio = precio;
        }

        public String getCodigo() {
            return codigo;
        }

        public String getNombre() {
            return nombre;
        }

        public double getPrecio() {
            return precio;
        }

        @Override
        public String toString() {
            return "Producto = [" + nombre + " Precio: $" + precio + " Codigo " + codigo + "]";
        }
    }

    public static class ProductoAlimenticio extends Producto {
        private String fechacaducidad;

        public ProductoAlimenticio(String codigo, String nombre, double precio, String fechacaducidad) {
            super(codigo, nombre, precio);
            this.fechacaducidad = fechacaducidad;
        }

        @Override
        public String toString() {
            return super.toString() + " Fecha de caducidad: " + fechacaducidad;
        }
    }

    public static class ProductoElectronico extends Producto {
        private int voltaje;

        public ProductoElectronico(String codigo, String nombre, double precio, int voltaje) {
            super(codigo, nombre, precio);
            this.voltaje = voltaje;
        }

        @Override
        public String toString() {
            return super.toString() + " Voltaje: " + voltaje;
        }
    }

//La clase es como un molde (Tiempo de compilación): Es la abstracción o plantilla que define la estructura (atributos) 
//  y el comportamiento (métodos) comunes. No reserva memoria para datos concretos en tiempo de ejecución.

//El Objeto es como una instancia (Tiempo de ejecución): Es la concreción real del molde, generada en la memoria dinámica (Heap) 
// mediante el operador new. La variable creada en el código (almacenada en la pila o Stack) 
// contiene únicamente la dirección de memoria o referencia hacia el objeto en el Heap.

}





