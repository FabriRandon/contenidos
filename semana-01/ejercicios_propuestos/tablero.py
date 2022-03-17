tablero = [['-', '-', '-'], ['-', 'o', '-'], ['-', '-', '-']]
pos = (1, 1)

def bajar(tablero, pos):
    tablero[pos[1]][pos[0]] = '-'
    pos = (pos[0], min(pos[1] + 1, 2))
    tablero[pos[1]][pos[0]] = 'o'
    return tablero, pos

def subir(tablero, pos):
    tablero[pos[1]][pos[0]] = '-'
    pos = (pos[0], max(pos[1] - 1, 0))
    tablero[pos[1]][pos[0]] = 'o'
    return tablero, pos
    
def derecha(tablero, pos):
    tablero[pos[1]][pos[0]] = '-'
    pos = (min(pos[0] + 1, 2), pos[1])
    tablero[pos[1]][pos[0]] = 'o'
    return tablero, pos

def izquierda(tablero, pos):
    tablero[pos[1]][pos[0]] = '-'
    pos = (max(pos[0] - 1, 0), pos[1])
    tablero[pos[1]][pos[0]] = 'o'
    return tablero, pos

dic = {"w":subir, "s":bajar, "a":izquierda, "d":derecha}

# Puedes rellenar aquí

while True:
    for fila in tablero:
        print("".join(fila))
    accion = input("Ingresa acción: ").strip()
    if accion in "asdw":
        tablero, pos = dic[accion](tablero, pos)

    elif accion == "q":
        print("¡Adios!")
        break
    else:
        print("Inválido")