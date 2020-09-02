
def usuario_escolhe_jogada(n, m):
	"""
	Pede pro usuário inserir quantas peças quer tirar e analisa se é um valor menor ou igual ao máximo estipulado e maior que 0.
	Caso não seja, diz que a jogada é inválida e repete a pergunta. Caso seja, retorna o valor retirado. 
	"""
	numero_valido = False

	while not numero_valido:

		tirou = int(input('''Quantas peças você vai tirar? 
			'''))

		if tirou <= m and tirou>0: 
		
			numero_valido = True
			return tirou

		else: print('''Oops! Jogada inválida! Tente de novo.
			''')


def computador_escolhe_jogada(n, m): 
	"""
	Devolve um número, que a máquina vai retirar na partida, que obedeça a estratégia para vencer:
	Sempre deixar na mesa múltiplos de m+1.
	"""
	tirou = 0    
	obedece_estrategia = False
	nao_se_aplica = False 

	while not obedece_estrategia or not nao_se_aplica:

		tirou = tirou + 1  #garante que tira > 0
		n = n - 1

		if (n%(m+1)) == 0 and tirou <= m:
			obedece_estrategia = True
			return tirou

		if n == 0:  # a estratégia vencedora não se aplica
			nao_se_aplica = True
			return 1



def partida():
	"""
	Pergunta ao usuário quantas peças vão ter no tabuleiro e qual o limite de peças a retirar por jogada. 
	Se o número de peças no tabuleiro for múltiplo de m+1, pede pro usuário começar. Se não, diz que a máquina começará 
	(estratégia para vencer o jogo). A função redireciona a partida entre máquina e usuário até que o valor de peças na mesa
	seja 0, e anuncia o vencedor (quem tirou a última peça).
	"""
	n = float(input('''Quantas peças? '''))         
	m = float(input('''Limite de peças por jogada? 
		'''))

	if n%(m+1) == 0: 
		print('''Você começa!
			''')
		x = 1
	else: 
		print('''Computador começa!
			''')
		x = 2

	tirou = 0

	while n != 0: 
		
		if x == 2:
			tirou = computador_escolhe_jogada(n, m)
			n = n - tirou
			print("O computador tirou", tirou, '''peças.
				''')
			print("Agora restam ", n, '''peças no tabuleiro.
				''')
			x = 1

		else:
			tirou = usuario_escolhe_jogada(n, m)
			n = n - tirou
			print("Você tirou", tirou, "peças.")
			print("Agora restam ", n, "peças no tabuleiro.")
			x = 2

	if x == 2:
		print('''Fim do jogo! Você ganhou!
			''')
		return 2
	else:
		print('''Fim do jogo! O computador ganhou!
			''')
		return 1 


def campeonato():  
	"""
	Chama a função partida 3 vezes, anunciando o número da partida e o placar final.
	"""
	vez = 1 #
	usuario = 0 
	computador = 0

	while vez<= 3:
		print("	**** Rodada ", vez, '''****
			''')
		vez = vez + 1

		x = partida()

		if x == 2:
			usuario = usuario + 1
		else: 
			computador = computador + 1

	print('''**** Final do campeonato! ****

	Placar: Você''', usuario, "X", computador, "Computador" )


def main():
	"""
	Mensagem inicial do jogo. Pede pro usuário escolher entre partida isolada ou campeonato, chamando as funções.
	"""
	tipo_de_jogo = int(input(''' Bem-vindo ao jogo do NIM! Escolha:
	1 - para jogar uma partida isolada
	2 - para jogar um  campeonato 

	'''))

	if tipo_de_jogo == 1:
		print('''Voce escolheu uma partida isolada!
			''')
		partida()  ##tem como resumir?
	else:
		print('''Voce escolheu um campeonato!
			''')
		campeonato()


main( ) #chama automaticamente no terminal





