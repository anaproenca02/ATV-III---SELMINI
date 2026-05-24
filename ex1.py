import random


class Musica:

    def __init__(self, id, titulo, artista, genero, duracao):

        self.id = id
        self.titulo = titulo
        self.artista = artista
        self.genero = genero
        self.duracao = duracao
        self.reproducoes = 0


class No:

    def __init__(self, musica):

        self.musica = musica
        self.esq = None
        self.dir = None


class BST:

    def __init__(self):

        self.raiz = None
        self.ids = []


    def gerarId(self):

        while True:

            numero = random.randint(1000, 9999)

            if numero not in self.ids:

                self.ids.append(numero)

                return numero


    def inserir(self, raiz, musica):

        if raiz is None:
            return No(musica)

        if musica.id < raiz.musica.id:

            raiz.esq = self.inserir(raiz.esq, musica)

        else:

            raiz.dir = self.inserir(raiz.dir, musica)

        return raiz


    def cadastrarMusica(self):

        titulo = input("Titulo: ")
        artista = input("Artista: ")
        genero = input("Genero: ")
        duracao = int(input("Duracao em segundos: "))

        id = self.gerarId()

        musica = Musica(id, titulo, artista, genero, duracao)

        self.raiz = self.inserir(self.raiz, musica)

        print("Musica cadastrada.")
        print("ID:", id)


    def buscar(self, raiz, id):

        if raiz is None or raiz.musica.id == id:
            return raiz

        if id < raiz.musica.id:

            return self.buscar(raiz.esq, id)

        return self.buscar(raiz.dir, id)


    def buscarMusica(self):

        id = int(input("Digite o ID: "))

        no = self.buscar(self.raiz, id)

        if no:

            m = no.musica

            print("\nMusica encontrada")
            print("ID:", m.id)
            print("Titulo:", m.titulo)
            print("Artista:", m.artista)
            print("Genero:", m.genero)
            print("Duracao:", m.duracao)
            print("Reproducoes:", m.reproducoes)

        else:

            print("Musica nao encontrada.")


    def ouvirMusica(self):

        id = int(input("Digite o ID da musica: "))

        no = self.buscar(self.raiz, id)

        if no:

            no.musica.reproducoes += 1

            print("Musica reproduzida.")

        else:

            print("Musica nao encontrada.")


    def menorNo(self, no):

        atual = no

        while atual.esq:

            atual = atual.esq

        return atual


    def remover(self, raiz, id):

        if raiz is None:
            return raiz

        if id < raiz.musica.id:

            raiz.esq = self.remover(raiz.esq, id)

        elif id > raiz.musica.id:

            raiz.dir = self.remover(raiz.dir, id)

        else:

            if raiz.esq is None:
                return raiz.dir

            elif raiz.dir is None:
                return raiz.esq

            temp = self.menorNo(raiz.dir)

            raiz.musica = temp.musica

            raiz.dir = self.remover(raiz.dir, temp.musica.id)

        return raiz


    def removerMusica(self):

        id = int(input("Digite o ID para remover: "))

        self.raiz = self.remover(self.raiz, id)

        print("Musica removida.")


    def pegarMusicas(self, raiz, lista):

        if raiz:

            lista.append(raiz.musica)

            self.pegarMusicas(raiz.esq, lista)

            self.pegarMusicas(raiz.dir, lista)


    def top5(self):

        lista = []

        self.pegarMusicas(self.raiz, lista)

        for i in range(len(lista)):

            for j in range(i + 1, len(lista)):

                if lista[j].reproducoes > lista[i].reproducoes:

                    aux = lista[i]
                    lista[i] = lista[j]
                    lista[j] = aux

        print("\nTOP 5")

        limite = 5

        if len(lista) < 5:
            limite = len(lista)

        for i in range(limite):

            print(lista[i].titulo,
                  "-",
                  lista[i].reproducoes,
                  "reproducoes")


    def relatorioGenero(self, raiz, genero):

        if raiz:

            self.relatorioGenero(raiz.esq, genero)

            if raiz.musica.genero.lower() == genero.lower():

                print(raiz.musica.titulo,
                      "-",
                      raiz.musica.artista)

            self.relatorioGenero(raiz.dir, genero)


    def menu(self):

        while True:

            print("\n1 - Cadastrar musica")
            print("2 - Buscar musica")
            print("3 - Ouvir musica")
            print("4 - Remover musica")
            print("5 - Top 5")
            print("6 - Relatorio por genero")
            print("0 - Sair")

            op = int(input("Escolha: "))

            if op == 1:

                self.cadastrarMusica()

            elif op == 2:

                self.buscarMusica()

            elif op == 3:

                self.ouvirMusica()

            elif op == 4:

                self.removerMusica()

            elif op == 5:

                self.top5()

            elif op == 6:

                genero = input("Digite o genero: ")

                self.relatorioGenero(self.raiz, genero)

            elif op == 0:

                break

            else:

                print("Opcao invalida.")


arvore = BST()

arvore.menu()