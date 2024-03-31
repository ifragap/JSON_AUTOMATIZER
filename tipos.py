# Función para escribir un parámetro String
def string():
    nom = str(input("\nNombre del parámetro: "))
    val = str(input("\nSu valor: "))
    
    par = "\"" + nom + "\"" + ": " + "\"" + val + "\""

    return par


# Función para escribir un parámetro Number
def number():
    nom = str(input("\nNombre del parámetro: "))
    val = str(input("\nSu valor: "))
    
    par = "\"" + nom + "\"" + ": " + val

    return par


# Función para escribir un parámetro Boolean
def booleano():
    nom = str(input("\nNombre del parámetro: "))
    val = str(input("\nSu valor, True (T) o False (F): "))
    if(val[0].upper() == "T"):
        val = "true"
    elif(val[0].upper() == "F"):
        val = "false"
    
    par = "\"" + nom + "\"" + ": " + val

    return par


# Función para escribir un parámetro Array
def array(tipo):
    nom = str(input("\nNombre del parámetro: "))
    par = "\"" + nom + "\"" + ": ["

    val = str(input("\n¿Quiere añadir algún valor dentro del array? (S/N)\n"))
    if(val[0].upper() == "S"):
        more = True
        while(more):
            val = str(input("\nSu valor: "))
            match tipo:
                case "A":
                    t = str(input("\n¿Tipo de dato dentro de array?\nElija entre Array (A), Boolean (B), Number (N), Object (O) o String (S).\n"))
                    array(t[0].upper())
                case "B":
                    if(val[0].upper() == "T"):
                        val = "true"
                    elif(val[0].upper() == "F"):
                        val = "false"
                case "O":
                    return
                case "S":
                    val = "\"" + val + "\""
            
            comp = str(input("\n¿Quiere añadir algún valor más? (S/N)\n"))
            if(comp[0].upper() == "S"):
                par = par + val + ","
            elif(comp[0].upper() == "N"):
                par = par + val
                more = False
    
    par = par + "]"
    return par