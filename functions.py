def validacao_quantidade():
    n = 0
    while True:
        n = input("Quantidade de discos (3 - 6): ")
        if not n.isdigit():
            print("Escolha somente números!")
            continue
        n = int(n)
        if not 3 <= n <= 6:
            print("Quantidade inválida!")
            continue
        break
    return n


def gerador_torres(n):
    torre1 = []
    torre2 = []
    torre3 = []
    for i in range(1, n + 1):
        torre1.append(i)
        torre2.append(0)
        torre3.append(0)
    torres = [torre1, torre2, torre3]
    return torres


def game(torres, n):
    win_array = torres[0].copy()
    venceu = False
    num_jogadas = 0
    jogada_invalida = 0
    while not venceu:
        i = n - 1
        y = 0
        aux = n - 1

        imprimir(torres, n)

        if jogada_invalida == 1:
            print("\nErro: Jogada inválida!!")
        base_origem = int(
            input("Digite de onde voce deseja retirar algum disco: "))
        base_destino = int(
            input("Digite onde voce deseja colocar esse disco: "))

        jogada_invalida = 0

        if torres[base_destino - 1][0] != 0:
            jogada_invalida = 1
            continue

        if torres[base_destino - 1][aux] != 0:
            while torres[base_destino - 1][aux] != 0:
                aux -= 1
            aux += 1

        if torres[base_destino - 1][i] != 0:
            while torres[base_destino - 1][i] != 0:
                i -= 1

        while torres[base_origem - 1][y] == 0:
            y += 1
            if y == n-1:
                break

        if torres[base_origem - 1][y] > torres[base_destino - 1][aux] != 0 or torres[base_origem - 1][y] == 0:
            jogada_invalida = 1
            continue

        x = torres[base_origem - 1].pop(y)
        torres[base_destino - 1][i] = x
        if len(torres[base_origem - 1]) < n:
            torres[base_origem - 1].insert(0, 0)
        if len(torres[base_destino - 1]) > n:
            del(torres[base_destino - 1][0])

        num_jogadas += 1

        if win_array in torres and num_jogadas > 5:
            venceu = True
            imprimir(torres, n)

    return num_jogadas


def imprimir(torres, n):
    for k in range(0, 3):
        print(f'({k + 1})')
        for j in range(0, n):
            if torres[k][j] == 0:
                print("   |".center(36))
                continue
            else:
                linha = "OOOOOO" * torres[k][j]
                print(linha.center(40))
