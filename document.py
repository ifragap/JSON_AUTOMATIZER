import os
from tipos import booleano, number, string, array

def document(numDatos = 1, file = "doc.json", ovw = True):
    print("Vamos a representar un documento de ", numDatos, " parámetros.")
    if(ovw != True):
        f = open(file, "a")
    else:
        f = open(file, "w")
    f.write("{")
    f.close()
    for i in range(numDatos):
        print("\nPara el parámetro nº" + str(i+1) + ":")
        tipo = str(input("\n¿Qué tipo de dato quiere representar?\nElija entre Array (A), Boolean (B), Number (N), Object (O) o String (S).\n"))
        
        match tipo[0].upper():
            case "A":
                t = str(input("\n¿Tipo de dato dentro de array?\nElija entre Array (A), Boolean (B), Number (N), Object (O) o String (S).\n"))
                array(file, t[0].upper())
            case "B":
                booleano(file)          
            case "N":
                number(file)
            case "O":
                nom = str(input("\nNombre del parámetro: "))
                par = "\"" + nom + "\"" + ":"
                f = open(file, "a")
                f.write(par)
                f.close 
                print("\nProcedemos a la creación del objeto...")
                num = int(input("\nNúmero de parámetros que va a tener este objeto: "))
                document(num, file, False)
                print("\nHemos terminado de crear de objeto.")
            case "S":
                string(file)
        
        if(i != numDatos - 1):
            f = open(file, "a")
            f.write(",")
            f.close()

    f = open(file, "a")
    f.write("}")
    f.close()
    #os.remove(file)
    
document(2)