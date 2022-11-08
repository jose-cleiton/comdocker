from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
opttions = webdriver.ChromeOptions()
opttions.add_argument('--ignore-certificate-erros')
opttions.add_argument('--ignore-certificate-errors')
opttions.add_argument('--ignore-ssl-errors')
opttions.add_argument('--start-maximized')

# importação do webdriver, que é o que possibilita a implementação para todos


servico = Service(ChromeDriverManager().install())
# requisições para essa instância criada utilizando o método `get`
navegdor = webdriver.Chrome(service=servico)