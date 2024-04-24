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

def read_pdf(filename):
    text = ''
    with open(filename, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def import_pdf(tree):
    filename = input("Enter the name of the PDF file to import: ")
    if filename:
        text = read_pdf(filename)
        for word in text.split():
            tree.agregar(word)
        print("PDF imported successfully.")

def search_word(tree):
    word = input("Enter a word to search: ")
    result = tree.busqueda(word)
    if result:
        print(f"'{word}' found in the PDF.")
    else:
        print(f"'{word}' not found in the PDF.")

if __name__ == "__main__":
    tree = Tree("")  # Árbol vacío para iniciar
    while True:
        print("\nMenu:")
        print("1. Import PDF")
        print("2. Search Word")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            import_pdf(tree)
        elif choice == "2":
            search_word(tree)
        elif choice == "3":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

