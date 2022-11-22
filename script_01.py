"""
Entrada e saída de arquivos txt
I/O de arquivos (Input/Output)

"""

import os

if __name__ == "__main__":

    # Para abrir arquivos pelo Python, utilizar-se-á a função built-in open()
    # Hei de passar como argumentos o arquivo que deve ser aberto e o modo de abertura
    # Se o modo de abertura não for informado, o Python abrirá automaticamente o arquivo
    # como somente-leitura
    # A função open() retorna o objeto que representará esse arquivo.

    # os.path.join() -> concatena nomes de diretórios e nomes de arquivos,
    # garantindo assim que o caminho até o arquivo esteja correto.
    # arquivo = open("log.txt") - abertura comum, sem o os.path.join()
    # os.getcwd() retorna o caminho completo até o diretório
    # onde o script está sendo executado.
    arquivo = open(os.path.join(os.getcwd(), "log.txt"))

    # Podemos ler arquivos texto no Python de 4 maneiras diferentes:
    # Usando o método read(n) -> "n" significa quantos caracteres serão lidos.
    # Se não for passado, lê o arquivo inteiro.
    # read() retorna uma string, com o conteúdo lido.

    print(arquivo.read())

    # Método readline(n)
    # Lê uma linha inteira do arquivo até a quantidade de caracteres informado

    print(arquivo.readline())

    # A linha acima não imprime nada, pois o cursor do arquivo está no final, pois,
    # antes foi chamado o método read(). Podemos verificar a posição atual do cursor
    # utilizando o método tell().

    print(arquivo.tell())

    # Se quiser ler o arquivo novamente, é necessário rebobinar o cursor até o início
    # do arquivo ou, até a posição 0. Utilizar-se-á o método seek() para isso.

    arquivo.seek(0)

    print(arquivo.readline(10))
    print(arquivo.readline())

    # readlines() -> Lê as linhas do arquivo e retorna como itens de uma lista
    print(arquivo.readlines())

    arquivo.seek(0)

    # Sempre que abrimos um arquivo, devemos fechá-lo
    arquivo.close()