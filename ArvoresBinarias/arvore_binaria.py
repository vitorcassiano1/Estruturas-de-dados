class NodeArvore:
    """
    Classe Node para a árvore binária.
    Cada nó possui um valor e referências para os nós esquerdo e direito.
    """
    def _init_(self, valor: int):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def _repr_(self):
        return f"NodeArvore({self.valor})"

class ArvoreBinaria:
    """
    Implementação de uma Árvore Binária de Busca (BST).
    """
    def _init_(self):
        self.raiz = None

    def inserir(self, valor: int) -> None:
        """Insere um valor na árvore binária de busca."""
        self.raiz = self._inserir_rec(self.raiz, valor)

    def _inserir_rec(self, node: NodeArvore, valor: int) -> NodeArvore:
        if node is None:
            return NodeArvore(valor)
        if valor < node.valor:
            node.esquerda = self._inserir_rec(node.esquerda, valor)
        elif valor > node.valor:
            node.direita = self._inserir_rec(node.direita, valor)
        # Se o valor for igual, não insere duplicata
        return node

    def em_ordem(self) -> None:
        """Realiza uma travessia em ordem e imprime os valores."""
        self._em_ordem_rec(self.raiz)
        print()

    def _em_ordem_rec(self, node: NodeArvore) -> None:
        if node is not None:
            self._em_ordem_rec(node.esquerda)
            print(node.valor, end=" ")
            self._em_ordem_rec(node.direita)


if _name_ == "_main_":
    # Exemplo de uso:
    arvore = ArvoreBinaria()
    for valor in [50, 30, 70, 20, 40, 60, 80]:
        arvore.inserir(valor)
    print("Árvore em ordem:")
    arvore.em_ordem()  # Saída esperada: 20 30 40 50 60 70 80
