from bs4 import BeautifulSoup
import requests

class Livros:
	def __init__(self):
		self.top_url = 'https://www.amazon.com.br/gp/bestsellers/books?ie=UTF8&ref_=sd_allcat_books_best'
		self.getDados(self.top_url)
	
	def getDados(self,url):
		requisicao = requests.get(url,timeout=10)
		conteudo = BeautifulSoup(requisicao.content, "html.parser")
		DadosPrincipais = conteudo.find_all('ol',class_='a-ordered-list')[0].text
		
		conteudoTextual = []
		conteudoTextual.append(DadosPrincipais)

		texto = conteudoTextual[0].split('\n')
		texto = [x for x in texto if x != '']
		texto = [x for x in texto if x != '        ']
				
		i = 0
		print("===== Ranking de livros mais vendidos amazon =====\n")
		for y in range(1,31,5):#o (numero de livros *5) +1, melhor nao passar de 5
			i +=1
			texto[y]=texto[y].split("            ")
			print(i,"º lugar:", texto[y][1])
			print("Autor(a):", texto[y+1])
			print("Avaliacao media:", texto[y+2], "de um total de", texto[y+3], "avaliacoes")
			texto[y+4] = texto[y+4].split("R$")
			texto[y+4] = texto[y+4][1].split("#")
			print("preco: R$", texto[y+4][0])
			print ("\n==========\n")


livros = Livros()