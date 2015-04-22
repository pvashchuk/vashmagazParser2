from selenium import webdriver
import csv

driver = webdriver.Firefox()
driver.implicitly_wait(5)
base_url = "http://vashmagazin.ua"
###########
driver.get(base_url + "/")
driver.find_element_by_link_text(u"Квартири").click()   #тут має бути цикл по рубриках
###########
Rubryka = driver.find_element_by_css_selector("span.foot_section_name").text
subRubryka = driver.find_element_by_css_selector("span.foot_rub_name").text
currentPage = driver.find_element_by_css_selector("div.page.current > a").text
nextPage = int(currentPage) + 1
lastPage = driver.find_element_by_xpath("//form[@id='price']/table[3]/tbody/tr[4]/td/div/div[6]/a").text
file = open("outFile.csv", "wb", newline="", dialect="excel"))
for x in range(int(currentPage), int(lastPage)+1):
    driver.get(base_url + "/nerukhomist/kvartyry//?item_price1=&item_price2=&page=" + str(x))
    currentPage = driver.find_element_by_css_selector("div.page.current > a").text
    phoneNum = driver.find_elements_by_class_name("ner-auto-tel")
    for i in phoneNum:
        csvWriter = csv.writer(file)
        csvWriter.writerow( [str((Rubryka) + '>' + (subRubryka) + ' | стор: ' + (currentPage)),
                                i.text] )
file.close()
driver.quit()
