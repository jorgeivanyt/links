from datetime import datetime


class Cliente:
    # Este contador es de la clase: lo comparten todos los clientes
    cantidad_clientes = 0

    def __init__(self, nombre, apellidos, fecha_nacimiento):
        # Convertimos el texto "YYYY/MM/DD" a una fecha real
        fecha = datetime.strptime(fecha_nacimiento, "%Y/%m/%d")

        # Calculamos la edad en años (asumiendo 365 dias por año)
        hoy = datetime.now()
        dias_vividos = (hoy - fecha).days
        edad = dias_vividos // 365

        # Si es menor de 18, no se puede registrar
        if edad < 18:
            raise ValueError("El cliente debe ser mayor de 18 años")

        # Solo sumamos al contador si el cliente es valido
        Cliente.cantidad_clientes += 1

        self.nombre = nombre
        self.apellidos = apellidos
        self.fecha_nacimiento = fecha
        self.id = str(Cliente.cantidad_clientes).zfill(6)
        self.saldo = 0

    def saludo(self):
        print("Bienvenido al banco")
        print("Cliente:", self.nombre, self.apellidos)
        print("Saldo en cuenta:", self.saldo, "€")

    def deposito(self, cantidad):
        self.saldo = self.saldo + cantidad
        print("Deposito realizado. Saldo actual:", self.saldo, "€")

    def retirada(self, cantidad):
        if self.saldo > cantidad:
            self.saldo = self.saldo - cantidad
            print("Retirada realizada. Saldo actual:", self.saldo, "€")
        else:
            print("No hay saldo suficiente, la operacion no se puede realizar")


def transferencia(emisor, receptor, cantidad):
    if emisor.saldo > cantidad:
        emisor.saldo = emisor.saldo - cantidad
        receptor.saldo = receptor.saldo + cantidad
        print("Transferencia de", cantidad, "€ de", emisor.nombre, "a", receptor.nombre)
    else:
        print("El emisor no tiene saldo suficiente para transferir")


def main():
    # Dos clientes mayores de 18 años
    cliente_uno = Cliente("Ana", "Lopez Perez", "1995/04/10")
    cliente_dos = Cliente("Carlos", "Gomez Ruiz", "1988/11/23")

    # Un cliente menor de 18 años: debe dar error
    try:
        cliente_tres = Cliente("Luis", "Diaz Mora", "2015/06/15")
    except ValueError as error:
        print("Error al crear cliente:", error)

    print()
    cliente_uno.saludo()
    cliente_dos.saludo()

    print()
    # Deposito y retirada en una cuenta
    cliente_uno.deposito(500)
    cliente_uno.retirada(100)

    print()
    # Retirada en una cuenta sin saldo
    cliente_dos.retirada(50)

    print()
    # Transferencia entre dos clientes
    transferencia(cliente_uno, cliente_dos, 200)

    print()
    # Mostrar saldos finales
    print("Saldo de", cliente_uno.nombre, ":", cliente_uno.saldo, "€")
    print("Saldo de", cliente_dos.nombre, ":", cliente_dos.saldo, "€")


main()
