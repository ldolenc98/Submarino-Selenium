from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox()

browser.get('https://www.submarino.com.br/categoria/livros?chave=prf_hm_tt_0_1_livros')

print("***SUBMARINO***\n")
print("Qual categoria de livros você deseja acessar?\n")

categoria = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li/a/span")

i = 0

while i < len(categoria):

	print(str(i+1) + "-" + categoria[i].text)

	i = i + 1

print("\n")

escolha1 = int(input("Digite aqui a categoria escolhida: "))

botao1 = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li"+str([escolha1]))

botao1.click()

print("\n")

print("***LIVROS DA CATEGORIA " + (categoria[escolha1-1].text).upper() + "***\n")

sleep(10)

quantidade= browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div[2]/div/div/div/aside/div/div[1]/span")

print("Há " + quantidade.text + " nessa categoria\n")

livros = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/section/div/div/h2")

precos = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/section/div/div/div/span")

for livro in livros and preco in precos:
	
	print(livro.text + preco.text)

