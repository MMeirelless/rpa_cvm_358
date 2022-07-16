from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import datetime

empresas = [
    {
        "nome":"Banco do Brasil",
        "cnpj":"00.000.000/0001-91"
    },
    {
        "nome":"Fleury",
        "cnpj":"60.840.055/0001-31"
    }
]

for empresa in empresas:
    
    driver = webdriver.Chrome("chromedriver.exe")
    action = webdriver.ActionChains(driver)
    driver.get("https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAb.aspx?TipoConsult=c")

    # Search Company
    search_bar = driver.find_element(By.ID, "txtCNPJNome")
    search_bar.click()
    search_bar.send_keys(empresa["cnpj"])

    continue_btn = driver.find_element(By.ID, "btnContinuar")
    continue_btn.click()

    # Clicking on company
    company_btn = driver.find_element(By.LINK_TEXT, empresa["cnpj"])
    company_btn.click()

    time.sleep(3)

    # Filtering
    filters = driver.find_element(By.ID, "textoDivPesquisa")
    filters.click()

    time.sleep(3)

    query_timepicker = driver.find_element(By.ID, "rdPeriodo")
    query_timepicker.click()

    query_timepicker_ini = driver.find_element(By.ID, "txtDataIni")
    query_timepicker_ini.click()
    query_timepicker_ini.send_keys(f'01/{datetime.today().strftime("%m/%Y")}')

    query_timepicker_fim = driver.find_element(By.ID, "txtDataFim")
    query_timepicker_fim.click()
    query_timepicker_fim.send_keys(datetime.today().strftime("%d/%m/%Y"))

    time.sleep(3)

    table_query = driver.find_element(By.ID, "btnConsulta")
    table_query.click()

    time.sleep(3)

    table_query = driver.find_element(By.ID, "buscaTabela")
    table_query.click()
    table_query.send_keys("Valores Mobiliários Negociados e Detidos")

    # Downloading PDF
    file_download_button = driver.find_element(By.CLASS_NAME, "fi-download")
    file_download_button.click()
    
    time.sleep(3)

    driver.close()

    # Renaming File
    import glob
    import os.path

    folder_path = r'c:/Users/matia/Downloads'
    file_type = r'\*pdf'
    files = glob.glob(folder_path + file_type)
    max_file = max(files, key=os.path.getctime)

    os.rename(max_file, max_file.replace(max_file.replace("c:/Users/matia/Downloads\\", ""), f"CVM358 - {empresa['nome']}.pdf"))




