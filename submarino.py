from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

i = 0

arquivo = open('livros.csv', 'w')

browser = webdriver.Firefox()

browser.get('https://www.submarino.com.br/categoria/livros?chave=prf_hm_tt_0_1_livros')

categorias_teste = WebDriverWait(browser,300).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li/a/span")))

categorias = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li/a/span")

sleep(10)

while i < len(categorias):

	sleep(10)

	categoria = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li" + str([i+1]) + "/a/span")

	sleep(2)

	categoria.click()

	j = 21

	sleep(40)
	
	subcategorias_teste = WebDriverWait(browser,300).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[2]/div/aside/div[1]/div[2]/div/div/div/span/div/div/section[1]/div/ul/li/a/span")))

	subcategorias = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li/a/span")

	sleep(15)
	
	try:
		ver_todos = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[2]/div/aside/div[1]/div[2]/div/div/div/span/div/div/section[1]/div/button")

		ver_todos.click()

		sleep(5)

	except:

		""

	subcategoria_plus = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/section/div/ul/li/a/span")

	sleep(1)

	try:

		ver_todos.click()

	except:

		""

	a = len(subcategorias) + len(subcategoria_plus)

	print(a)

	while j < a:

		sleep(3)

		z = 1
	
		if j > 19:

			ver_todos = browser.find_element_by_xpath("/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[2]/div/aside/div[1]/div[2]/div/div/div/span/div/div/section[1]/div/button")

			ver_todos.click()

			sleep(5)

			subcategoria_plus = browser.find_elements_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/section/div/ul/li/a/span")

			subcategoria_plus[z].click()

			z = z + 1		

		else:

			subcategorias_teste = WebDriverWait(browser,300).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[3]/div/div[2]/div[2]/div/aside/div[1]/div[2]/div/div/div/span/div/div/section[1]/div/ul/li/a/span")))

			sleep(3)

			subcategoria = browser.find_element_by_xpath("/html/body/div/div/div/div/div/div/div/div/div/aside/div/div/div/div/div/span/div/div/section/div/ul/li"+str([j+1])+"/a/span")

			subcategoria.click()

		sleep(60)

		livros = WebDriverWait(browser,60).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/section/div/div/h2")))


		precos = WebDriverWait(browser,60).until(EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/div/a/section/div/div/div")))

		a = precos[2]

		precos.append(a)

		l = 2

		for livro in livros:


			if precos[l].text == "" :
				
				arquivo.write(str(str(livro.text) + "| Produto fora de estoque\n"))

				print(str(livro.text) + "| Produto fora de estoque")

				l = l + 1

				sleep(1)

				
			elif precos[l+1].text == "Inclui oferta":

				arquivo.write(str(str(livro.text) + "|" + str(precos[l].text + "\n")))	

				print(str(livro.text) + "|" + str(precos[l].text))

				l = l + 4

				sleep(1)

				
			else:

				arquivo.write(str(str(livro.text) + "|" + str(precos[l].text + "\n")))	

				print(str(livro.text) + "|" + str(precos[l].text))

				try:
				
					if precos[l+3].text == "" and precos[l+4].text == "":

						l = l + 1

					else:

						l = l + 3

				except:

					""

				sleep(1)


		sleep(5)
		
		j = j + 1

		retorno = WebDriverWait(browser,60).until(EC.element_to_be_clickable((By.CLASS_NAME, "breadcrumb-backlink")))

		sleep(2)

		retorno.click()



	retorno2 = browser.find_element_by_name("Livros")

	retorno2.click()

	i = i + 1
			



