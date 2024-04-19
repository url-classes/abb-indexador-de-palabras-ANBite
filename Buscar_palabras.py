from Arbol_buscador_pdf import Tree
import PyPDF2

archivos = ['prueba.pdf', 'prueba2.pdf']
palabras = []

for i in archivos:
    with open(i, 'rb') as file:
        abrir = PyPDF2.PdfReader(file)

        numero_paginas = len(abrir.pages)

        for j in range(numero_paginas):
            pagina = abrir.pages[j]

            texto = pagina.extract_text() #texto a colocar en el arbol
            palabras.append(texto.lower())

while True:
    menu = input("*****Menú Principal*****\nA. Ver todo el contenido de los archivos"
                 "\nB. Buscar un dato\n Elija su opción: ").lower()
    while menu == "a":
        n = 0
        d = 1
        while n != numero_paginas+1:
            print(f"Documento No.{d}:")
            print(palabras[n])
            n += 1
            d += 1
        break
    while menu == "b":
        numero_arbol = int(input("Ingrese el Número del árbol al que quiere buscar un dato: "))



        break

    Continuar = input("\033[1;38;2;203;231;0m¿Desea continuar con el programa?\033[0;m\n"+"\033[1;38;2;162;233;29mS\033[0;m" + "/" + "\033[1;38;2;215;0;0mN \033[0;m").lower()
    if Continuar == "n":
            print("\033[1;38;2;231;0;95mPrograma Finalizado\033[0;m\n")
            break

