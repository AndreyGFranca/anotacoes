#coding=utf-8

import math

class Celula(object):
	"""
	Representacao de uma Celula.
	Uma celula eh um retangulo, aqui armazenaremos as extremidades,
	ou seja os vertices de retangulo, em uma tupla
	extremidades (x1, x2, y1, y2).
	A celula tambem sabe os pontos que estao contidos dentro dela,
	os mesmos serao armazenados em uma lista pontos.
	A celula tambem sabe quais são suas celulas vizinhas. Cada
	celula aqui contem duas vizinhas, sua vizinha do lado direito,
	e sua vizinha de cima.
	"""
	def __init__(self, extremidades, c_vizinhas):
		super(Celula, self).__init__()
		self.extremidades = extremidades # Tupla com as coordenadas
										 # dos vertices do retangulo.

		self.pontos[]	  				 # Lista com os indices dos
										 # pontos que estao contidos.

		self.c_vizinhas	= c_vizinhas 	 # Lista com o indice das
										 # respectivas vizinhas.

	def insere_pontos(p):
		self.pontos.append(p)



class Ponto(object):
	"""
	Representacao de um ponto, os quais serao calculados os vizinhos.
	Cada ponto possui uma coordenada representada por uma tupla (x, y)
	"""
	def __init__(self, coord):
		super(Ponto, self).__init__()
		self.coord = coord 				 # Coordenadas do ponto.

	

def criar_grade(dist, N_sqrt):
	"""
	Cria uma grade, com Nc celulas. Retorna uma lista com todas
	as celulas.
	"""
	l_aux = [i*dist for i in range(N_sqrt)]

	Lc = []
	c_vizinhas = []
	for x in range(l_aux):
		for y in range(l_aux):
			# (x1, x2, y1, y2)
			extremidades = (x, x+dist, y, y+dist)

			# primeira celula
			if x == 0 and y == 0:
				#vizinho de cima
				c_vizinhas.append( [0, dist, dist*(N_sqrt-1), dist*(N_sqrt) ])
				#vizinho da direita
				c_vizinhas.append( [x+dist, x+2*dist, y, y+dist ] )

			# ultima celula da primeira linha
			else if x == 0 and y == N_sqrt-1:
				# vizinho da direita
				c_vizinhas.append( [0, dist, 0, dist] )
				#vizinho de cima
				c_vizinhas.append( [] )

			# ultima celula primeira primeira coluna, ultima linha
			else if x == N_sqrt-1 and y == 0:
				c_vizinhas.append( [] )


			vizinha = [ (), () ]
			c = Celula(extremidades)


def main():
	"""
	Funcao principal que chama todas as outras funcoes.
	"""
	L = []
	N = 8**2
	N_sqrt = int(math.sqrt(N) + 0.5)
	delxy = 1.0/ (2.0 * N_sqrt)
	two_delxy = 2.0 * delxy
	for i in range(0, N_sqrt):
		for j in range(0, N_sqrt):
			L.append([delxy + i * two_delxy, delxy + j * two_delxy])

	# Distancia de uma extremidade da celula ate a outra, nas
	# coordenadas x e y.
	dist = 2* ( (delxy + 1 * two_delxy) - (delxy + 0 * two_delxy) )

	print "Hello World"


if __name__ == '__main__':
	main()