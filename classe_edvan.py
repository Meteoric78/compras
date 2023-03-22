
class Compra:
    def __init__(self, carrinho, produto, preco, qty, Adicionar_Compra = False, Finalizar_Compra = False, Remover_Compra = False, Listar_Compra = False):
        self.carrinho = carrinho
        self.produto = produto
        self.preco = preco
        self.qty = qty
        self.Adicionar_Compra = Adicionar_Compra
        self.Finalizar_Compra = Finalizar_Compra
        self.Remover_Compra = Remover_Compra
        self.Listar_Compra = Listar_Compra
    
    #def produto(self, preco, qty):
    #    produto = [preco, qty]
    #    return

    def Adicionar_Compra(self, produto, preco, qty):
        carrinho.append(produto)
        return

    def Finalizar_Compra(self, produto, preco, qty):

        return

    def Remover_Compra(self, produto, preco, qty):

        return

    def Listar_Compra(self, carrinho):
        print(f'{carrinho}')

        return

        
carrinho = []
c1 = Compra.Adicionar_Compra('hasagi', 666, 2)
Listar_Compra(carrinho)