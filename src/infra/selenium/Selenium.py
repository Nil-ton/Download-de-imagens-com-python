import string
from selenium import webdriver

class Selenium:
    def __init__(self) -> None:
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--user-data-dir=C:\\Users\\olive\\AppData\\Local\\Google\\Chrome\\Application\\User Data")
        self.driver = webdriver.Chrome(executable_path= './chromedriver.exe', chrome_options = self.options)
            
        

