from cmath import log
from typing import List 
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from RPA.Libs.LocalStorage import LocalStorage
from RPA.Libs.SendEmail import *
from RPA.Libs.LocalStorage import *
import pandas as pd
import json
from RPA.Config import *
from RPA.Libs.SendEmail import smtp
from RPA.Libs.Logs import LogCsv
from RPA.Libs.Logs import deco_log

@deco_log(LOG,"OPENING CADMUS WEBSITE")
def OPEN_CADMUS()->webdriver:
    driver = webdriver.Chrome(CHROME_DRIVER)
    driver.get("https://cadmus.com.br/vagas-tecnologia/")

    #WAITING  FOR THE PAGE LOAD ELEMENTS
    wdw = WebDriverWait(driver, 30)
    locator = (By.CSS_SELECTOR, '#pfolio')
    wdw.until(presence_of_element_located(locator))  
    #WHEN PAGE IS LOEADED RETURN  DRIVER
    return driver

@deco_log(LOG,"GET ALL OPORTUNITIES")
def GET_OPORTUNITIES(driver:webdriver)->List:

    storage = LocalStorage(driver) #LOCAL STORAGE 
    STORAGE_DETAILS = json.loads(storage.get("vagas")) # GET ALL OPORTUNITIES STORED ON LOCALSTORAGE
    driver.quit()

    # GET ONLY NECESSARY FIELDS FROM EACH OPORTUNITY
    DATA = [
        {
            "Oportunity": box['name'],
            "Locale": box['cidade_Regi_o__c'],
            "Detail": box['descricao_da_vaga__c'].replace("<br>", "\n")
        }

        for box in STORAGE_DETAILS
    ]
    return DATA

@deco_log(LOG,"EXPORT TO EXCEL FILE")
def EXPORT_TO_EXCEL_FILE(DATA:List):
    DF = pd.DataFrame(DATA)
    DF.to_excel(OUTPUT_FILE,index=False)
    return OUTPUT_FILE

@deco_log(LOG,"SENDING EMAIL")
def SEND_EMAIL(file):
    smtp_o = smtp(FROM,SERVER,PORT, USER, PWD)

    Body = "<h2>Relatório de vagas disponíveis Cadmus</h2><p>Segue Excel com  vagas disponíveis do portal da CadMus para análise<p>"
    
    smtp_o.sendmail(TO, Body, SUBJECT, "html","", [file])


@deco_log(LOG,"MAIN FUNCTION")
def MAIN():
    #============================== VARIABLES
    driver:         webdriver
    OPORTUNITIES:   List

    #============================== START PROCESS
    driver          = OPEN_CADMUS()
    OPORTUNITIES    = GET_OPORTUNITIES(driver)
    FILE            = EXPORT_TO_EXCEL_FILE(OPORTUNITIES)
    MAIL            = SEND_EMAIL(FILE)

MAIN()

