class ListaOrdenada:
    """
    Implementação de uma lista ordenada (em ordem crescente).
    Assume que os itens são comparáveis (por exemplo, números).
    """
    class Node:
        def _init_(self, item: any):
            self.item = item
            self.next = None

        def _repr_(self):
            return f"Node({self.item})"

    def _init_(self):
        self.head = None

    def insere_ordenado(self, item: any) -> None:
        """Insere um item na lista mantendo a ordem crescente."""
        novo = ListaOrdenada.Node(item)
        # Se a lista estiver vazia ou o item for menor que o primeiro
        if self.head is None or item < self.head.item:
            novo.next = self.head
            self.head = novo
        else:
            atual = self.head
            while atual.next is not None and atual.next.item < item:
                atual = atual.next
            novo.next = atual.next
            atual.next = novo

    def imprime_lista(self) -> None:
        """Imprime os itens da lista ordenada."""
        atual = self.head
        elementos = []
        while atual:
            elementos.append(str(atual.item))
            atual = atual.next
        print(" -> ".join(elementos) + " -> None")


if _name_ == "_main_":
    # Exemplo de uso:
    lista_ord = ListaOrdenada()
    for valor in [50, 20, 40, 10, 30]:
        lista_ord.insere_ordenado(valor)
    lista_ord.imprime_lista()  # Saída esperada: 10 -> 20 -> 30 -> 40 -> 50 -> None
