import os, subprocess
from document import document

def automatizer(num_doc = 1, file = "doc.json"):
    for i in range(num_doc):
        f = open(file, "w")
        numDatos = int(input("Número de campos en el documento: "))
        writing = document(numDatos)
        f.write(writing)
        f.close()
        db = str(input("\nNombre de la base de datos: "))
        coll = str(input("\nNombre de la colección: "))
        file = str(input("\nDonde se encuentra el fichero JSON (ponga la ruta absoluta): "))
        mongimp = str(input("\nDonde se encuentra mongoimport.exe (ponga la ruta absoluta): "))       
        #subprocess.run(["cd", "mongimp"])
        #subprocess.run(["mongoimport", "--db=", db, "--collection=", coll, "file=", file])
        #os.remove(file)