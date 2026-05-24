import random


class Ativo:

    def __init__(self, codigo, ticker,
                 empresa, setor,
                 cotacao, qtd, tipo):

        self.codigoAtivo = codigo
        self.ticker = ticker
        self.nomeEmpresa = empresa
        self.setor = setor
        self.cotacaoAtual = cotacao
        self.qtdCotas = qtd
        self.tipoAtivo = tipo


class No:

    def __init__(self, ativo):

        self.ativo = ativo
        self.esq = None
        self.dir = None


class BST:

    def __init__(self):

        self.raiz = None
        self.codigos = []


    def gerarCodigo(self):

        while True:

            codigo = random.randint(1000, 9999)

            if codigo not in self.codigos:

                self.codigos.append(codigo)

                return codigo


    def inserir(self, raiz, ativo):

        if raiz is None:
            return No(ativo)

        if ativo.codigoAtivo < raiz.ativo.codigoAtivo:

            raiz.esq = self.inserir(raiz.esq, ativo)

        else:

            raiz.dir = self.inserir(raiz.dir, ativo)

        return raiz


    def cadastrar(self):

        ticker = input("Ticker: ")
        empresa = input("Empresa: ")
        setor = input("Setor: ")
        cotacao = float(input("Cotacao: "))
        qtd = int(input("Quantidade: "))
        tipo = input("Tipo do ativo: ")

        codigo = self.gerarCodigo()

        ativo = Ativo(codigo,
                      ticker,
                      empresa,
                      setor,
                      cotacao,
                      qtd,
                      tipo)

        self.raiz = self.inserir(self.raiz, ativo)

        print("Ativo cadastrado.")
        print("Codigo:", codigo)


    def buscar(self, raiz, codigo):

        if raiz is None or raiz.ativo.codigoAtivo == codigo:
            return raiz

        if codigo < raiz.ativo.codigoAtivo:

            return self.buscar(raiz.esq, codigo)

        return self.buscar(raiz.dir, codigo)


    def buscarAtivo(self):

        codigo = int(input("Digite o codigo: "))

        no = self.buscar(self.raiz, codigo)

        if no:

            a = no.ativo

            valor = a.cotacaoAtual * a.qtdCotas

            print("\nAtivo encontrado")
            print("Ticker:", a.ticker)
            print("Empresa:", a.nomeEmpresa)
            print("Setor:", a.setor)
            print("Cotacao:", a.cotacaoAtual)
            print("Quantidade:", a.qtdCotas)
            print("Tipo:", a.tipoAtivo)
            print("Valor total:", round(valor, 2))

        else:

            print("Ativo nao encontrado.")


    def atualizarCotacao(self):

        codigo = int(input("Digite o codigo: "))

        no = self.buscar(self.raiz, codigo)

        if no:

            nova = float(input("Nova cotacao: "))

            no.ativo.cotacaoAtual = nova

            print("Cotacao atualizada.")

        else:

            print("Ativo nao encontrado.")


    def menorNo(self, no):

        atual = no

        while atual.esq:

            atual = atual.esq

        return atual


    def remover(self, raiz, codigo):

        if raiz is None:
            return raiz

        if codigo < raiz.ativo.codigoAtivo:

            raiz.esq = self.remover(raiz.esq, codigo)

        elif codigo > raiz.ativo.codigoAtivo:

            raiz.dir = self.remover(raiz.dir, codigo)

        else:

            if raiz.esq is None:
                return raiz.dir

            elif raiz.dir is None:
                return raiz.esq

            temp = self.menorNo(raiz.dir)

            raiz.ativo = temp.ativo

            raiz.dir = self.remover(
                raiz.dir,
                temp.ativo.codigoAtivo
            )

        return raiz


    def retirar(self):

        codigo = int(input("Digite o codigo: "))

        self.raiz = self.remover(self.raiz, codigo)

        print("Ativo removido.")


    def valorPatrimonial(self, no):

        if no is None:
            return 0

        valorNo = no.ativo.cotacaoAtual * no.ativo.qtdCotas

        return (
            valorNo +
            self.valorPatrimonial(no.esq) +
            self.valorPatrimonial(no.dir)
        )


    def contar(self, no):

        if no is None:
            return 0

        return (
            1 +
            self.contar(no.esq) +
            self.contar(no.dir)
        )


    def patrimonio(self):

        codigo = int(input("Digite o codigo: "))

        no = self.buscar(self.raiz, codigo)

        if no:

            valorProprio = (
                no.ativo.cotacaoAtual *
                no.ativo.qtdCotas
            )

            valorSub = self.valorPatrimonial(no)

            total = self.valorPatrimonial(self.raiz)

            qtd = self.contar(no)

            percentual = (valorSub / total) * 100

            print("\nAtivo consultado")
            print("Ticker:", no.ativo.ticker)
            print("Codigo:", no.ativo.codigoAtivo)

            print("Valor proprio:",
                  round(valorProprio, 2))

            print("Ativos na subarvore:",
                  qtd)

            print("Valor da subarvore:",
                  round(valorSub, 2))

            print("Participacao:",
                  round(percentual, 2), "%")

        else:

            print("Ativo nao encontrado.")


    def menu(self):

        while True:

            print("\n1 - Cadastrar ativo")
            print("2 - Buscar ativo")
            print("3 - Atualizar cotacao")
            print("4 - Retirar ativo")
            print("5 - Patrimonio")
            print("0 - Sair")

            op = int(input("Escolha: "))

            if op == 1:

                self.cadastrar()

            elif op == 2:

                self.buscarAtivo()

            elif op == 3:

                self.atualizarCotacao()

            elif op == 4:

                self.retirar()

            elif op == 5:

                self.patrimonio()

            elif op == 0:

                break

            else:

                print("Opcao invalida.")


arvore = BST()

arvore.menu()