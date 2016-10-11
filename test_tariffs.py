import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestTariffs(unittest.TestCase):
    url = "http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk"
    countries = ["Canada", "Germany", "Iceland", "Pakistan", "Singapore", "South Africa"]

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_tariffs(self):
        driver = self.driver
        driver.get(self.url)
        assert "O2 | International | International Caller Bolt On" == driver.title
        country_name = driver.find_element_by_id("countryName")

        for country in self.countries:
            country_name.clear()
            country_name.send_keys(country)
            country_name.send_keys(Keys.TAB)

            country_code = driver.find_element_by_id("countryCode")
            assert "Country Code" in country_code.text

            driver.find_element_by_id("paymonthly").click()

            landline = driver.find_element_by_xpath('//*[@id="standardRatesTable"]/tbody/tr[1]/td[2]')
            # assert pound sign
            assert u"\u00A3" == landline.text[0]

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
