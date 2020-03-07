class FirstPage:
    def __init__(self,driver):
        self.driver = driver
    def input_10086(self):
        self.driver.find_element_by_id('key').send_keys('10086')
    def click_keyword(self):
        self.driver.find_element_by_class_name('button').click()