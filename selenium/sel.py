from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")
"""
driver.get("http://www.yahoo.co.jp/")
searchBox = driver.find_element_by_css_selector("#srchtxt")
searchBox.send_keys("Amazon")
kensakuBotan = driver.find_element_by_css_selector("#srchbtn")
kensakuBotan.click()
driver.close()
"""

driver.get("https://www.amazon.co.jp/?tag=hydjpabky-22&hvadid=263039465963&hvdev=c&ref=pd_sl_7iohgj9py6_e")
searchBox = driver.find_element_by_css_selector("#srchtxt")
searchBox.send_keys("Amazon")
kensakuBotan = driver.find_element_by_css_selector("#srchbtn")
kensakuBotan.click()
driver.close()
