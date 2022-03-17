class TorreDeHanoi:
    
    def __init__(self):
        self.pilar_1 = [6, 5, 4, 3, 2, 1]
        self.pilar_2 = []
        self.pilar_3 = []
        self.pilares = self.pilar_1, self.pilar_2, self.pilar_3
        
    def mover_disco(self, pilar_origen, pilar_destino):
        pilar_origen -= 1
        pilar_destino -= 1
        # Recuerda que debes sacar el elemento que está más arriba en el pilar de origen
        # y colocarlo en lo más alto del pilar de destino
        # Sacar el disco
        
        origen = self.pilares[pilar_origen].pop() #Sacamos el disco del origen

    #Si no hay pilares en el destino, el movimiento es valido
        if(len(self.pilares[pilar_destino]) == 0):
            destino = self.pilares[pilar_destino].append(origen) #Ponemos el disco en el destino
        #Si existe un pilar, se debe revisar si el valor del top es mayor que el pilar de origen
        elif(self.pilares[pilar_destino][-1] > origen):
            destino = self.pilares[pilar_destino].append(origen)
    #Si no se cumple ninguna de las condiciones, el movimiento no es valido
        else:
            print("El movimiento no es valido")
            self.pilares[pilar_origen].append(origen)
    
    def __str__(self):
        output = ""
        # Range termina con -1 para recorrer al revés
        for i in range(5, -1, -1):
            fila = " "  # Armamos una fila a la vez, desde arriba
            # Pilar 1
            if len(self.pilar_1) > i:
                fila += str(self.pilar_1[i]) + " "
            else:
                fila += "x "
            # Pilar 2
            if len(self.pilar_2) > i:
                fila += str(self.pilar_2[i]) + " "
            else:
                fila += "x "
            # Pilar 3
            if len(self.pilar_3) > i:
                fila += str(self.pilar_3[i]) + " "
            else:
                fila += "x "
            output += fila + "\n"
        output += "=" * 7 + "\n"
        return output

torre_de_hanoi = TorreDeHanoi()
print(torre_de_hanoi)


print("Bienvenido a la torre de hanoi, puede rendirse ingresando \'-1\'")
print()
a = 0
b = 0
while a != -1 or b != -1:
    a = int(input("Ingrese la columna de origen: 1, 2 o 3: "))
    b = int(input("Ingrese la columna de llegada: 1, 2 o 3: "))
    if(a in [1, 2, 3] and b in [1, 2, 3] and a != b):
        torre_de_hanoi.mover_disco(a, b) # Del pilar 1 al pilar 2
    else:
        print("Comando no valido!!! Mira bien po")
    print(torre_de_hanoi)