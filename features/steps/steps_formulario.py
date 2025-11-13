# ============================================================
# 🧩 Importação das bibliotecas necessárias
# ============================================================

from behave import given, when, then  
# Importa as anotações (decorators) do framework Behave, que são usadas para
# definir etapas do comportamento BDD:
# @given → representa o "Dado que"
# @when  → representa o "Quando"
# @then  → representa o "Então"
# Elas conectam o texto escrito no arquivo .feature com o código que o executa.

from selenium.webdriver import Edge  
# Importa o driver do navegador Microsoft Edge, usado pelo Selenium para controlar o navegador.

from selenium.webdriver.edge.options import Options  
# Importa a classe Options, que permite configurar parâmetros do navegador (como tela cheia, logs, etc).

from selenium.webdriver.common.by import By  
# Classe que define os diferentes tipos de seletores (estratégias para localizar elementos na página),
# como: By.ID, By.NAME, By.XPATH, By.CSS_SELECTOR, etc.

from selenium.webdriver.common.keys import Keys  
# Permite simular o uso de teclas do teclado, como ENTER, TAB, SETA, etc.

from selenium.webdriver.support.ui import Select
#Permite selecionar input's

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time  
# Biblioteca padrão do Python usada aqui para adicionar pausas (delays) entre as ações.
# Isso garante que a página tenha tempo de carregar antes do próximo comando.

# ============================================================
# 🧠 Definição dos passos do teste BDD (Gherkin)
# ============================================================


# ----------------------------------------
# 1️⃣ Etapa "DADO QUE..."
# ----------------------------------------
@given("que o Mercado Livre está aberto")
def step_open_browser(context):
    pass
    # Cria um objeto de configuração do navegador
    options = Options()

    # Inicia o navegador maximizado (em tela cheia)
    options.add_argument("--start-maximized")

    # Desativa a detecção de automação (impede que sites saibam que o navegador é controlado por Selenium)
    options.add_argument("--disable-blink-features=AutomationControlled")

    # Remove mensagens de log desnecessárias no terminal (de "DevTools" e "EdgeAuth")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    # Inicializa o navegador Edge com as opções definidas acima
    context.driver = Edge(options=options)

    # Abre o site inicial: Google
    context.driver.get("https://www.mercadolivre.com.br/")

    # Aguarda 3 segundos para garantir que a página carregue
    time.sleep(10) 


# ----------------------------------------
# 2️⃣ Etapa "QUANDO..."
# ----------------------------------------
@when('desejo um notebook barato')
def step_complete_form(context):
    # aguarda até 15 segundos
    wait = WebDriverWait(context.driver, 10)

    # Localiza o campo de pesquisa
    campo = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="cb1-edit"]')))
    campo.send_keys("notebook samsung")
    campo.send_keys(Keys.ENTER)
    time.sleep(3)
    # Aguarda o carregamento dos resultados
    
    # Clica no botão de ordenação para achar o menor preço
    filtro = context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Mais relevantes"]')
    filtro.click()
    time.sleep(3)
    #aguarda 3 segundos

    # Aguarda a lista abrir e o item "Menor preço" aparecer
    menor_preco = context.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/section/div[2]/div/div/div/div[2]/div/div/div/div/div/ul/li[2]')
    menor_preco.click()
    time.sleep(5)
   

    print("✅ Filtro 'Menor preço' selecionado com sucesso!")
    time.sleep(5)


# ----------------------------------------
# 3️⃣ Etapa "ENTÃO..."
# ----------------------------------------
@then("devo obter o melhor custo x beneficio")
def step_send_form(context):

    #QUEM NASCEU PRA WEBDRIVERWAIT NUNCA VAI SER TIMESLEEP #TIMESLEEPFOREVER!!!!!
    barato = context.driver.find_element(By.CSS_SELECTOR,".andes-card.poly-card.poly-card--grid-card.poly-card--xlarge.poly-card--CORE.andes-card--flat.andes-card--padding-0.andes-card--animated")
    barato.click()
    time.sleep(5)  # Espera a página do produto abrir   

    context.driver.save_screenshot("Evidencias.png")
    
    print("✅ Screenshot salva com sucesso!")
    # Aguarda o carregamento da tela de resultados   
   
    print("✅ Formulário enviado com sucesso!")
    context.driver.quit()
    #apenas mostra um print final para dizer que o codigo rodou!