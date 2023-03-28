import functions
player1 = str(input("Digite o seu nome: "))

n = functions.validacao_quantidade()
torres = functions.gerador_torres(n)
quant_jogadas = functions.game(torres, n)

print(f'Você venceu com: {quant_jogadas} jogadas.')
