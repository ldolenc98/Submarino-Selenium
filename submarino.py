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

	print(str(i) + "-" + categoria[i].text)

	i = i + 1

