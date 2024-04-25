import PyPDF2

class Nodo:
    def __init__(self, data):
        self.data = data  # Dato
        self.left = None  # Izquierda
        self.right = None  # Derecha

class Tree:
    def __init__(self, data):
        self.raiz = Nodo(data)

    def agregar_recursivo(self, nodo, data):  # Recibe el nodo y el dato a agregar
        if data < nodo.data:  # Si el valor es menor que el dato que tiene el nodo
            if nodo.left is None:  # Si el nodo está disponible a su izquierda
                nodo.left = Nodo(data)  # Se coloca un nuevo nodo a la izquierda
            else:
                self.agregar_recursivo(nodo.left, data)  # Se agrega a la izquierda del nodo (Recursivo)
        else:
            if nodo.right is None:
                nodo.right = Nodo(data)
            else:
                self.agregar_recursivo(nodo.right, data)  # Se agrega a la derecha del nodo (Recursivo)

    def buscar_recursivo(self, nodo, buscar):  # Recibe a partir de un nodo, que dato buscamos
        if nodo is None:  # Si el nodo está vacío
            return None
        if nodo.data == buscar:  # Si el nodo (Raíz) es igual a la búsqueda deseada
            return nodo  # Retorna el nodo (Raíz)
        if buscar < nodo.data:  # Si la búsqueda es menor que el dato (Raíz)
            return self.buscar_recursivo(nodo.left, buscar)  # Se busca en el lado izquierdo
        else:
            return self.buscar_recursivo(nodo.right, buscar)  # Se busca en la derecha

    def agregar(self, data):
        self.agregar_recursivo(self.raiz, data)

    def busqueda(self, buscar):
        return self.buscar_recursivo(self.raiz, buscar)

def leer_pdf(archivo):
    texto = ''
    with open(archivo, 'rb') as file:
        lector = PyPDF2.PdfReader(file)
        num_pag = len(lector.pages)
        for i in range(num_pag):
            pagina = lector.pages[i]
            texto += pagina.extract_text()
    return texto

def importar_pdf(arbol):
    try:
        nombre_del_archivo = input("Ingrese el nombre del archivo PDF (Ejemplo: pruebas/prueba.pdf): ")
        if nombre_del_archivo:
            texto = leer_pdf(nombre_del_archivo)
            for j in texto.split():
                arbol.agregar(j)
            print("* -* -* -* Archivo importado correctamente *- *- *- *")
    except FileNotFoundError:
        print("\033[1;38;2;215;0;0mNo existe un archivo con ese nombre, asegurese que se encuentra en la carpeta llamada 'pruebas'\033[0;m")

def buscar_dato(arbol):
    dato = input("Ingrese el dato a buscar: ")
    resultado = arbol.busqueda(dato)
    if resultado:
        print(f"El '{dato}' fue encontrado en el PDF.")
    else:
        print(f"'{dato}' no está en el PDF.")


arbolito = Tree("")  # Árbol vacío para iniciar

while True:

    menu = input("*****Menú Principal*****\
    \nA. Importar PDF\nB. Buscar un dato\n Elija su opción: ").lower()
    while menu == "a":
        importar_pdf(arbolito)
        break

    while menu == "b":
        buscar_dato(arbolito)
        break

    Continuar = input("\033[1;38;2;203;231;0m¿Desea continuar con el programa?\033[0;m\n"+"\033[1;38;2;162;233;29mS\033[0;m" + "/" + "\033[1;38;2;215;0;0mN \033[0;m").lower()
    if Continuar == "n":
            print("\033[1;38;2;231;0;95mPrograma Finalizado\033[0;m\n")
            break


