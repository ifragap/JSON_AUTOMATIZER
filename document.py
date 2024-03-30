import os
from tipos import booleano, number, string, array

def document(numDatos = 1):
    for i in range(numDatos):
        par = "{"
        print("\nPara el parámetro nº" + str(i+1) + ":")
        tipo = str(input("\n¿Qué tipo de dato quiere representar?\nElija entre Array (A), Boolean (B), Number (N), Object (O) o String (S).\n"))
        
        match tipo[0].upper():
            case "A":
                t = str(input("\n¿Tipo de dato dentro de array?\nElija entre Array (A), Boolean (B), Number (N), Object (O) o String (S).\n"))
                array(t[0].upper())
            case "B":
                booleano()          
            case "N":
                number()
            case "O":
                nom = str(input("\nNombre del parámetro: "))
                par = "\"" + nom + "\"" + ":"
                print("\nProcedemos a la creación del objeto...")
                num = int(input("\nNúmero de parámetros que va a tener este objeto: "))
                document(num)
                print("\nHemos terminado de crear de objeto.")
            case "S":
                string()
        
        if(i != numDatos - 1):
            par = par + ","
        
        par = par + "}"
    return par
    
print(document(2))