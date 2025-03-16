class Node:
    """
    Classe Node para listas encadeadas.
    Cada nó contém um valor (item) e uma referência para o próximo nó.
    """
    def _init_(self, item: any):
        self.item = item
        self.next = None

    def _repr_(self):
        return f"Node({self.item})"
