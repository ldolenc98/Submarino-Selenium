from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException
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

sleep(5)

escolha = int(input("Digite aqui a categoria escolhida: "))

sleep(5)

botao1 = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li"+str([escolha]))

botao1.click()

sleep(5)

print("\n")

print("***LIVROS DA CATEGORIA " + (categoria[escolha-1].text).upper() + "***\n")

sleep(10)

quantidade= browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div[2]/div/div/div/aside/div/div[1]/span")

print("Há " + quantidade.text + " nessa categoria\n")

livros = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/section/div/div/h2")

precos = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/section/div/div/div/span")

i = 0

for livro in livros:	

	print(str(livro.text) + "-" + str(precos[i].text))

	i = i + 1
"""
i = 0

print("\n")
print("***SUBCATEGORIAS***\n")

subcategorias = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li/a/span")

while i < len(subcategorias):

	print(str(i+1) + "-" + subcategorias[i].text)

	i = i + 1

print("\n0-Pŕoxima página\n")

escolha2 = int(input("Digite a sua escolha aqui: "))

while escolha2 == 0:
	
	botao2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[1]/div/div[2]/div[4]/div/div/div/div[2]/div/ul/li[10]/a")

	botao2.click()

	sleep(3)

	escolha2 = int(input("Digite a sua escolha aqui: "))
else:

	botao2 = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[2]/div/aside/div[1]/div[2]/div/div/div/span/div/div/section[1]/div/ul/li"+str([escolha2])+"/a/span")

botao2.click()"""



