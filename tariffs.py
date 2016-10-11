from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

driver = webdriver.Firefox()
driver.get(url)
country_name = driver.find_element_by_id("countryName")

for country in countries:
    country_name.clear()
    country_name.send_keys(country)
    country_name.send_keys(Keys.TAB)
    driver.find_element_by_id("paymonthly").click()
    landline = driver.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')
    print(u'{}\t{}'.format(country, landline.text))

driver.close()
