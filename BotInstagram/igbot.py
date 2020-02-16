from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random
import os

dir_path = os.getcwd()

class InstagramBot:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.driver = webdriver.Chrome(dir_path+'/chromedriver')

	def login(self):
		driver = self.driver
		driver.get("https://www.instagram.com")
		time.sleep(3)
		botao_login = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
		botao_login.click()
		time.sleep(3)
		campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
		campo_usuario.click()
		campo_usuario.clear()
		campo_usuario.send_keys(self.username)
		campo_senha = driver.find_element_by_xpath("//input[@name='password']")
		campo_senha.click()
		campo_senha.clear()
		campo_senha.send_keys(self.password)
		campo_senha.send_keys(Keys.RETURN)
		time.sleep(3)
		self.comente_nas_fotos('corrida')

	@staticmethod
	def digite_como_uma_pessoa(frase, onde_digitar):
		for letra in frase:
			onde_digitar.send_keys(letra)
			time.sleep(random.randint(1,5)/30)

	def comente_nas_fotos(self, hashtag):
		driver = self.driver
		driver.get("https://www.instagram.com/explore/tags/{}/".format(hashtag))
		time.sleep(3)

		for i in range(1,3):
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			time.sleep(3)

		hrefs = driver.find_elements_by_tag_name('a')
		del hrefs[0:10]
		pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
		[href for href in pic_hrefs if hashtag in href]
		print(hashtag + 'foto' + str(len(pic_hrefs)))

		for pic_href in pic_hrefs:
			driver.get(pic_href)
			driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
			try:
				comentarios = ['Muito bom. Parabéns!', 'Continue com esse foco!', 'Que legal!', 'Que foto massa!', 'Essa foto ficou maravilhosa!']
				driver.find_element_by_class_name('Ypffh').click()
				campo_comentario = driver.find_element_by_class_name('Ypffh')
				time.sleep(random.randint(2,5))
				self.digite_como_uma_pessoa(random.choice(comentarios), campo_comentario)
				time.sleep(random.randint(10,15))
				driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
				time.sleep(5)
			except Exception as e:
				print(e)
				time.sleep(5)


BabyBot = InstagramBot('jp.656', 'p99616397')
BabyBot.login()