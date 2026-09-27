
from universidades import universidades

if __name__ == '__main__':

    aluno = universidades(
        "hallisson",
        123,
        "19/12/2003",
        bolsa=True,
        desconto=50
    )

    print(aluno.exibir())


