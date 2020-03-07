class SendPage:
    def __init__(self,driver):
        self.driver = driver
    def getElemn(self):
        self.driver.find_element_by_xpath('//*[text()='"10086"']')