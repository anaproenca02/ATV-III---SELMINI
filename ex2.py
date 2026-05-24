class Especie:

    def __init__(self, codigo, continente,
                 nome, qtd, cientifico):

        self.codigoRaridade = codigo
        self.continenteOrigem = continente
        self.nomeComum = nome
        self.qtdAmostras = qtd
        self.nomeCientifico = cientifico


class No:

    def __init__(self, especie):

        self.especie = especie
        self.esq = None
        self.dir = None
        self.altura = 1


class AVL:

    def __init__(self):

        self.raiz = None


    def altura(self, no):

        if no is None:
            return 0

        return no.altura


    def balanceamento(self, no):

        if no is None:
            return 0

        return self.altura(no.esq) - self.altura(no.dir)


    def rotacaoDireita(self, y):

        x = y.esq

        t2 = x.dir

        x.dir = y

        y.esq = t2

        y.altura = 1 + max(self.altura(y.esq),
                           self.altura(y.dir))

        x.altura = 1 + max(self.altura(x.esq),
                           self.altura(x.dir))

        return x


    def rotacaoEsquerda(self, x):

        y = x.dir

        t2 = y.esq

        y.esq = x

        x.dir = t2

        x.altura = 1 + max(self.altura(x.esq),
                           self.altura(x.dir))

        y.altura = 1 + max(self.altura(y.esq),
                           self.altura(y.dir))

        return y


    def inserir(self, raiz, especie):

        if raiz is None:
            return No(especie)

        if especie.codigoRaridade < raiz.especie.codigoRaridade:

            raiz.esq = self.inserir(raiz.esq, especie)

        else:

            raiz.dir = self.inserir(raiz.dir, especie)

        raiz.altura = 1 + max(self.altura(raiz.esq),
                              self.altura(raiz.dir))

        balance = self.balanceamento(raiz)

        if balance > 1 and especie.codigoRaridade < raiz.esq.especie.codigoRaridade:

            return self.rotacaoDireita(raiz)

        if balance < -1 and especie.codigoRaridade > raiz.dir.especie.codigoRaridade:

            return self.rotacaoEsquerda(raiz)

        if balance > 1 and especie.codigoRaridade > raiz.esq.especie.codigoRaridade:

            raiz.esq = self.rotacaoEsquerda(raiz.esq)

            return self.rotacaoDireita(raiz)

        if balance < -1 and especie.codigoRaridade < raiz.dir.especie.codigoRaridade:

            raiz.dir = self.rotacaoDireita(raiz.dir)

            return self.rotacaoEsquerda(raiz)

        return raiz


    def menorNo(self, no):

        atual = no

        while atual.esq:

            atual = atual.esq

        return atual


    def remover(self, raiz, codigo):

        if raiz is None:
            return raiz

        if codigo < raiz.especie.codigoRaridade:

            raiz.esq = self.remover(raiz.esq, codigo)

        elif codigo > raiz.especie.codigoRaridade:

            raiz.dir = self.remover(raiz.dir, codigo)

        else:

            if raiz.esq is None:
                return raiz.dir

            elif raiz.dir is None:
                return raiz.esq

            temp = self.menorNo(raiz.dir)

            raiz.especie = temp.especie

            raiz.dir = self.remover(
                raiz.dir,
                temp.especie.codigoRaridade
            )

        if raiz is None:
            return raiz

        raiz.altura = 1 + max(self.altura(raiz.esq),
                              self.altura(raiz.dir))

        balance = self.balanceamento(raiz)

        if balance > 1 and self.balanceamento(raiz.esq) >= 0:

            return self.rotacaoDireita(raiz)

        if balance > 1 and self.balanceamento(raiz.esq) < 0:

            raiz.esq = self.rotacaoEsquerda(raiz.esq)

            return self.rotacaoDireita(raiz)

        if balance < -1 and self.balanceamento(raiz.dir) <= 0:

            return self.rotacaoEsquerda(raiz)

        if balance < -1 and self.balanceamento(raiz.dir) > 0:

            raiz.dir = self.rotacaoDireita(raiz.dir)

            return self.rotacaoEsquerda(raiz)

        return raiz


    def buscar(self, raiz, codigo):

        if raiz is None or raiz.especie.codigoRaridade == codigo:
            return raiz

        if codigo < raiz.especie.codigoRaridade:

            return self.buscar(raiz.esq, codigo)

        return self.buscar(raiz.dir, codigo)


    def cadastrar(self):

        codigo = int(input("Codigo: "))
        continente = input("Continente: ")
        nome = input("Nome comum: ")
        qtd = int(input("Quantidade de amostras: "))
        cientifico = input("Nome cientifico: ")

        especie = Especie(codigo,
                          continente,
                          nome,
                          qtd,
                          cientifico)

        self.raiz = self.inserir(self.raiz, especie)

        print("Especie cadastrada.")


    def alerta(self):

        codigo = int(input("Codigo atual: "))

        no = self.buscar(self.raiz, codigo)

        if no:

            novo = int(input("Novo codigo: "))

            especie = no.especie

            self.raiz = self.remover(self.raiz, codigo)

            especie.codigoRaridade = novo

            self.raiz = self.inserir(self.raiz, especie)

            print("Codigo atualizado.")

        else:

            print("Especie nao encontrada.")


    def especieRara(self):

        if self.raiz is None:

            print("Arvore vazia.")

            return

        atual = self.raiz

        while atual.dir:

            atual = atual.dir

        e = atual.especie

        print("\nEspecie mais rara")
        print("Codigo:", e.codigoRaridade)
        print("Nome:", e.nomeComum)

        self.raiz = self.remover(
            self.raiz,
            e.codigoRaridade
        )


    def relatorio(self, raiz):

        if raiz:

            self.relatorio(raiz.dir)

            e = raiz.especie

            print("\nCodigo:", e.codigoRaridade)
            print("Nome:", e.nomeComum)
            print("Continente:", e.continenteOrigem)

            self.relatorio(raiz.esq)


    def menu(self):

        while True:

            print("\n1 - Cadastrar especie")
            print("2 - Alerta de extincao")
            print("3 - Resgatar especie rara")
            print("4 - Buscar especie")
            print("5 - Relatorio")
            print("0 - Sair")

            op = int(input("Escolha: "))

            if op == 1:

                self.cadastrar()

            elif op == 2:

                self.alerta()

            elif op == 3:

                self.especieRara()

            elif op == 4:

                codigo = int(input("Digite o codigo: "))

                no = self.buscar(self.raiz, codigo)

                if no:

                    print("Especie encontrada:")
                    print(no.especie.nomeComum)

                else:

                    print("Nao encontrada.")

            elif op == 5:

                self.relatorio(self.raiz)

            elif op == 0:

                break

            else:

                print("Opcao invalida.")


arvore = AVL()

arvore.menu()