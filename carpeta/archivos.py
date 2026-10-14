# 1.1 Sancho vs Dulcinea
with open("kijo.txt", encoding="utf-8") as archivo:
    personajes = ("Quijote", "Sancho", "Dulcinea")
    texto = archivo.read()
    for personaje in personajes:
        print(f"'{personaje}' aparece {texto.count(personaje)} veces.")

# 1.2 Reescribiendo el Quijote (Sin y con list comprehension)
with open("kijo.txt", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
nuevo = []
print(len(lineas))
print(len(nuevo))
for linea in lineas:
    nuevo.append(linea.replace("Quijote", "monolito"))

with open("monolito.txt", "w", encoding="utf-8") as a:
    a.writelines(nuevo)
    # imprime todo el texto monolito: print(nuevo)

gato_montes = [linea.replace("Quijote", "monolito") for linea in lineas]
print(len(gato_montes))
print("".join(gato_montes).count("monolito"))

# 1.3 Conteo de Palabras
variante = []
conteo = {}
for pala in texto.split():
    if pala in conteo:
        conteo[pala] += 1
    else:
        conteo[pala] = 1
print(len(conteo))
print(conteo["Dulcinea"] + conteo["Dulcinea,"])
# imprime todo el conteo de las palabras de todo el texto de kijo.txt print(conteo)

frecuentes = {p: n for p, n in conteo.items() if n > 100}
print(frecuentes)

# punto 2
import json

usuarios = {}
ARCHIVO = 'usuarios.json'

# 2.1 Registrar usuario
while True:
    nombre = input("¿que nombre de usuario te pondras? ")
    if nombre == "SALIR":
        break
    else:
        contraseña = input("cree su contraseña ")
        if contraseña == "":
            print("no fue posible registrar tu contraseña")
        usuarios[nombre] = contraseña

with open(ARCHIVO, "w", encoding="utf-8") as archivo:
    json.dump(usuarios, archivo)

# 2.2 Visualización de Usuarios Registrados
with open(ARCHIVO, "r", encoding="utf-8") as archivo:
    usuarios = json.load(archivo)
    for h in usuarios:
        print(h)

usuar = [u for u in usuarios]
print(usuar)

# 2.3 Inicio de Sesión
for intento in range(3):
    intente = input("cual es tu nombre de usuario? ")
    clave = input("¿cual es tu contraseña? ")
    if usuarios.get(intente) == clave:
        print("hola", intente)
        break
    else:
        print("intentalo de nuevo, te quedan", 2 - intento, "intentos")


# 2.4 Utilización de archivos binarios
import pickle

ARCHIVO_BIN = 'usuarios.bin'

# Guardar el diccionario de usuarios en formato binario ("wb")
with open(ARCHIVO_BIN, "wb") as archivo:
    pickle.dump(usuarios, archivo)

# Leer desde el archivo binario ("rb") y mostrar usuarios
with open(ARCHIVO_BIN, "rb") as archivo:
    usuarios_bin = pickle.load(archivo)
    for h in usuarios_bin:
        print(h)

usuar_bin = [u for u in usuarios_bin]
print(usuar_bin)

# Inicio de sesión verificando contra el archivo binario
for intento in range(3):
    intente = input("cual es tu nombre de usuario? ")
    clave = input("¿cual es tu contraseña? ")
    if usuarios_bin.get(intente) == clave:
        print("hola", intente)
        break
    else:
        print("intentalo de nuevo, te quedan", 2 - intento, "intentos")

# punto 3
import csv

# Primero creamos el archivo ventas.csv para que no dé FileNotFoundError
datos_tienda = [
    ["id_venta", "producto", "cantidad", "precio_unitario", "total"],
    ["1", "Camiseta", "3", "15.99", "47.97"],
    ["2", "Pantalón", "2", "29.99", "59.98"],
    ["3", "Zapatillas", "1", "49.99", "49.99"]
]

with open("ventas.csv", "w", encoding="utf-8", newline="") as a:
    escritor = csv.writer(a)
    escritor.writerows(datos_tienda)

# 3.1 Total Ventas
suma_total = 0
with open("ventas.csv", encoding="utf-8") as archivo:
    lector_csv = csv.reader(archivo)
    cabecera = next(lector_csv)  # Salta la primera fila de encabezados
    filas = list(lector_csv)     # Guardamos las filas para reusarlas abajo
    for fila in filas:
        suma_total += float(fila[4])

print("Total de ventas:", suma_total)

# 3.2 Ventas de Camisetas
camisetas = [fila for fila in filas if fila[1] == "Camiseta"]

with open("camisetas.csv", "w", encoding="utf-8", newline="") as a:
    escritor = csv.writer(a)
    escritor.writerow(cabecera)
    escritor.writerows(camisetas)

# 3.3 Producto más caro
mas_caro = ("", 0.0)
for fila in filas:
    precio = float(fila[3])
    if precio > mas_caro[1]:
        mas_caro = (fila[1], precio)

print("Producto mas caro:", mas_caro)