'''
1 - Abrir site https://ge.globo.com/cartola/index/feed/pagina-95.ghtml e fazer login 
2 - Acessar competições 
3 - Entrar na liga
4 - Pegar o Nome do time, Nomde do cartoleiro e a pontuação do time na rodada
5 - Salvar em uma Planilha de forma decrescente (do maior pontuador ao menor)
6 - Entrar no Whatsapp
7 - Enviar a planilha para o grupo
'''
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# 1 - Abrir o site https://ge.globo.com/cartola/index/feed/pagina-95.ghtml e fazerr login
driver = webdriver.Chrome()
driver.get('https://ge.globo.com/cartola/index/feed/pagina-95.ghtml')
sleep(20)
button_login = driver.find_element(By.XPATH, "//a[@class='subheader-cartola']")
sleep(1)
button_login.click()
