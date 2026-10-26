
camiones = {
    201: ["Renault",2020, "3541BW4"],
    202: ["Mercedes",2018, "9834HJ1"],
    203: ["Volvo",2005, "6712CK9"],
    204: ["BMW",2023, "1289LM2"],
}
diccionary = {
   "B": 0,
   "C": 1,
   "D": 2,
   "F": 3,
   "G": 4,
   "H": 5,
   "J": 6,
   "K": 7,
   "L": 8,
   "M": 9,
   "N": 10,
   "P": 11,
   "R": 12,
   "S": 13,
   "T": 14,
   "V": 15,
   "W": 16,
   "X": 17,
   "Y": 18,
   "Z": 19,
   
}
def GetNumber(placa):
    numero = ""
    for i in placa:
        if i.isdigit():
            numero += i
        else:
            break
    return numero

def GerLetter(numero):
    calculo = int(numero) % 20
    for letra in diccionary:
        if diccionary[letra] == calculo:
            return numero + letra
def main():
    for i in camiones:
        placa = camiones[i][2]
        numero = GetNumber(placa)
        correccion_placa = GerLetter(numero)
        camiones[i][2] = correccion_placa
    print(camiones)

main()