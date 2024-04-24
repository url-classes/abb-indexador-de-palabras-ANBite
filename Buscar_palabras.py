from Arbol_buscador_pdf import Tree
import PyPDF2

archivos = ['pruebas/prueba.pdf', 'pruebas/prueba2.pdf']
palabras = []

for i in archivos:
    with open(i, 'rb') as file:
        abrir = PyPDF2.PdfReader(file)
        numero_paginas = len(abrir.pages)

        for j in range(numero_paginas):
            pagina = abrir.pages[j]

            texto = pagina.extract_text() #texto a colocar en el arbol

            palabras.append(texto.lower())
            arbol = Tree(palabras[0])


n = 0
d = 1
while n != numero_paginas+1:
    print(f"Documento No.{d}:")
    print(palabras[n])
    n += 1
    d += 1


while True:

    menu = input("*****Menú Principal*****\
    \nA. Colocar los datos al árbol\nB. Buscar un dato\n Elija su opción: ").lower()
    while menu == "a":

        break

    while menu == "b":
        i = 1
        while palabras is not None:
            arbol.agregar(input(palabras[i]))
            print(f"{palabras[i]} fue agregado")
            i += 1
        print("* -* -* -* Datos agregados correctamente *- *- *- *")

        break
    while menu == "c":
        numero_arbol = input("Ingrese el dato que desea buscar: ")
        a = arbol.busqueda(numero_arbol)
        if a is None:
            print(f"{numero_arbol} no existe")
        else:
            print(f"{numero_arbol} se encuentra en el árbol")

        break

    Continuar = input("\033[1;38;2;203;231;0m¿Desea continuar con el programa?\033[0;m\n"+"\033[1;38;2;162;233;29mS\033[0;m" + "/" + "\033[1;38;2;215;0;0mN \033[0;m").lower()
    if Continuar == "n":
            print("\033[1;38;2;231;0;95mPrograma Finalizado\033[0;m\n")
            break

