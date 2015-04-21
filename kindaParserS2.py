# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import csv
import unittest, time, re

class KindaParserS2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(5)
        self.base_url = "http://vashmagazin.ua"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kinda_parser_s2(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"Квартири").click()   #тут би пасувало додати якусь змінну в яку можна б було вставляти назви\ідентифікатори рубрик
        Rubryka = driver.find_element_by_css_selector("span.foot_section_name").text
        subRubryka = driver.find_element_by_css_selector("span.foot_rub_name").text
        phoneNumber = driver.find_element_by_css_selector("span.ner-auto-tel > nobr").text
        currentPage = driver.find_element_by_css_selector("div.page.current > a").text
        nextPage = int(currentPage) + 1
        lastPage = driver.find_element_by_xpath("//form[@id='price']/table[3]/tbody/tr[4]/td/div/div[6]/a").text
        # ERROR: Caught exception [ERROR: Unsupported command [getEval |  | ]]
        print((Rubryka) + ' ' + (subRubryka) + ' ' )
        print('next page: ' + str(nextPage))
        print('last page: ' + (lastPage))
        # ERROR: Caught exception [ERROR: Unsupported command [getEval |  | ]]
        # driver.get(self.base_url + nextPageSTR)
        file = open("outFile.csv", "w", newline="")
        for x in range(int(currentPage), int(lastPage)+1):
           driver.get(self.base_url + "/nerukhomist/kvartyry//?item_price1=&item_price2=&page=" + str(x))
           currentPage = driver.find_element_by_css_selector("div.page.current > a").text
           phoneNumber = driver.find_element_by_css_selector("span.ner-auto-tel > nobr").text
           print('current page: ' + (currentPage))
           print ('Phone Number:' + (phoneNumber))
           csvWriter = csv.writer( file )  #Defaults to the excel dialect
           csvWriter.writerow( [str((Rubryka) + '>' + (subRubryka) + ' | page: ' + (currentPage)), str(phoneNumber)] )
              
##    def is_element_present(self, how, what):
##        try: self.driver.find_element(by=how, value=what)
##        except NoSuchElementException, e: return False
##        return True
##    
##    def is_alert_present(self):
##        try: self.driver.switch_to_alert()
##        except NoAlertPresentException, e: return False
##        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
    file.close()
