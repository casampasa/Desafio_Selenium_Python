import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
import time


class TestSuite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://mutant.com.br")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_enviar_mensagem(self):
        WebDriverWait(self.driver, 5)

        # Preenchimento de todos os campos de cadastro para enviar a mensagem
        self.driver.find_element(By.NAME, 'your-name').send_keys('Caio')
        self.driver.find_element(By.NAME, 'your-email').send_keys('casampasa@hotmail.com')
        self.driver.find_element(By.NAME, 'telefone').send_keys('85999851717')
        self.driver.find_element(By.NAME, 'empresa').send_keys('Test Company')

        self.driver.find_element(By.CLASS_NAME, "Zoly_cargo_lista").click()
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Gerente')]").click()

        self.driver.find_element(By.CLASS_NAME, "Home_e_Faceads_Assunto_comercial_rh_outros").click()
        self.driver.find_element(By.XPATH, "//li[contains(text(), 'Quero fazer parte do time Mutant')]").click()

        self.driver.find_element(By.CLASS_NAME, "Home_e_Faceads_Assunto_de_interesse").click()
        self.driver.find_element(By.XPATH,
                                 "//li[contains(text(), 'Quero desenvolver canais de atendimento (ex: WhatsApp e Chatbot)')]").click()

        self.driver.find_element(By.NAME, 'Home_e_Faceads_Mensagem').send_keys('Teste Automação Caio')

        time.sleep(2)

        # Clique no botão Enviar Mensagem
        self.driver.find_element(By.CSS_SELECTOR, ".has-spinner.wpcf7-submit").click()

        # Time Sleep alto inserido devido ao tempo de processamento do site após clicar no botão Enviar Mensagem
        time.sleep(70)

        # Capturar o texto presente no HTML
        elemento = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".wpcf7-response-output"))).text

        time.sleep(3)
        # Atribuir o texto a variável mensagem_atual e inserir o texto esperado na variavel mensagem_esperada
        mensagem_atual = elemento
        mensagem_esperada = "Agradecemos a sua mensagem."

        print("Mensagem atual:", mensagem_atual)
        print("Mensagem esperada:", mensagem_esperada)

        # realizar a validacao, verificando se a mensagem_esperada é igual a mensagem_atual
        assert mensagem_esperada == mensagem_atual, "A mensagem atual é diferente da mensagem esperada"

    def test_validar_acesso_site(self):
        elemento = self.driver.find_element(By.CSS_SELECTOR, ".button.text-center").text

        mensagem_atual = elemento
        mensagem_esperada = "Fale com a gente"

        print("Mensagem atual:", mensagem_atual)
        print("Mensagem esperada:", mensagem_esperada)

        assert mensagem_esperada == mensagem_atual, "A mensagem atual é diferente da mensagem esperada"



    def test_validar_clique_cases(self):
        menu_cases = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Cases')))
        menu_cases.click()

        link_banco_pan = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, 'Banco Pan')))
        link_banco_pan.click()

        elemento = wait.until(EC.presence_of_element_located((By.XPATH, "col-sm-6 roxo")))
        mensagem_atual = elemento.text

        mensagem_esperada = "BANCO PAN"

        print("Mensagem atual:", mensagem_atual)
        print("Mensagem esperada:", mensagem_esperada)

        assert mensagem_esperada == mensagem_atual, "A mensagem atual é diferente da mensagem esperada"

if __name__ == "__main__":
    unittest.main()
