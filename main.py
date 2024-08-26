from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Configurações do ChromeDriver
chrome_service = Service('./chromedriver/chromedriver.exe')  # Substitua pelo caminho do seu chromedriver
chrome_options = Options()
chrome_options.add_argument("--headless")

# Iniciar o WebDriver
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

try:
    # Acessar o site
    driver.get('https://www.omelete.com.br/')

    # Aguardar a página carregar
    time.sleep(3)

    # Encontra o icone de pesquisa e clica nele 
    search_icon = driver.find_element(By.CSS_SELECTOR, 'i[class="icon icon-search"]')
    search_icon.click()
    time.sleep(3)

    # Interagir com o campo de entrada
    input_box = driver.find_element(By.CSS_SELECTOR,'input[placeholder="Faça a sua busca"]')
    input_box.send_keys('Deadpool')
    input_box.send_keys(Keys.RETURN)

    time.sleep(5)
    # Extrair as notícias relacionadas
    news_items = driver.find_elements(By.CSS_SELECTOR, 'article')  

    results = []
    for item in news_items:
        try:
            title = item.find_element(By.CSS_SELECTOR, 'h2').text  # Adquire os Titulos
            date = item.find_element(By.CSS_SELECTOR, 'div[class="mark__time"]').text  #Pega o horario da publicacao 
            results.append(f'Título: {title}\nData: {date}\n') #junta os dois
        except Exception as e:
            print(f'Erro ao extrair dados de uma notícia: {e}')

    # Armazenar os dados em um arquivo txt
    with open('resultados.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(results))

finally:
    # Fechar o WebDriver
    driver.quit()