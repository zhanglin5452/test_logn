from selenium import webdriver
import unittest
from time import sleep
from DiffModule.page.first import FirstPage
from DiffModule.page.sendkeys import SendPage
class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.jd.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.firstpage = FirstPage(self.driver)
        self.sndleys = SendPage(self.driver)

    def tearDown(self):
        sleep(10)
        self.driver.quit()
    def test_case(self):
        # self.driver.find_element_by_id('key').send_keys('10086')
        self.firstpage.input_10086()
        # self.driver.find_element_by_class_name('button').click()
        self.firstpage.click_keyword()
        try:
            # self.driver.find_element_by_xpath('//*[text()='"10086"']')
            self.sndleys.getElemn()
            assert True
        except Exception:
            assert False
if __name__ == '__main__':
    unittest.main()