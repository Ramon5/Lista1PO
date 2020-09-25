from exercicios import (
    HelloWorld,
    MatrixNumbers,
    MatrixReader,
    MaxMinAverage,
    VectorStorage,
)


def menu():
    while True:
        print(
            "\nDigite o número do exercício ou 0 para sair:\n\n1 - Hello World\n2 - Preenchendo e exibindo vetor com 10 posições\n3 - Gerando matriz 10x10 \n4 - Min, Máx e Média\n5 - Ler arquivo e gerar matrizes\n\n"
        )
        try:
            choice = int(input())
            if choice == 0:
                break

            if choice == 1:
                HelloWorld()
            elif choice == 2:
                VectorStorage().execute()
            elif choice == 3:
                MatrixNumbers().execute()
            elif choice == 4:
                MaxMinAverage().execute()
            elif choice == 5:
                MatrixReader().execute()
        except ValueError:
            print("Você precisa informar um número inteiro!!")


if __name__ == "__main__":
    menu()
