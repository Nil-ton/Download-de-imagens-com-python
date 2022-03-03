from infra.selenium.Selenium import Selenium
from selenium.webdriver.common.by import By
from domain.Pinterest import Pinterest
import os
import wget


class ScrapingImagePinterest:
    def __init__(self, selenium: Selenium) -> None:
        self.selenium = selenium
        self.driver = self.selenium.driver
    
    def login(self, pinterest: Pinterest):
        elementOpenConteinerLogin = self.driver.find_elements(
            By.CSS_SELECTOR,
            '#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div > main > div:nth-child(2) > div.Jea._he.b8T.gjz.zI7.iyn.Hsu > div.Jea.l7T.zI7.iyn.Hsu > div:nth-child(2) > button > div'
        )


        if len(elementOpenConteinerLogin) != 0:
            elementOpenConteinerLogin[0].click()

            elementOpenWithAnotheAccount = self.driver.find_elements(
                By.CSS_SELECTOR,
                '#__PWS_ROOT__ > div.zI7.iyn.Hsu > div > div > main > div:nth-child(2) > div.Jea.MIw.TpD.mQ8.sLG.zI7.iyn.Hsu > div.Jea.MIw.QLY.Rym.jzS.mQ8.ojN.p6V.prG.sLG.zI7.iyn.Hsu > div > div > div > div > div > div > div:nth-child(8) > div > div'
            )

            print(elementOpenWithAnotheAccount)

            if len(elementOpenWithAnotheAccount) != 0:
                elementOpenWithAnotheAccount[0].click()

            elementUsername = self.driver.find_element(
                By.XPATH,
                '//*[@id="email"]')
            elementUsername.send_keys(pinterest.username)

            elementPassword = self.driver.find_element(
                By.XPATH,
                '//*[@id="password"]')
            elementPassword.send_keys(pinterest.password)

            elementSubmit = self.driver.find_element(
                By.XPATH,
                '//*[@id="__PWS_ROOT__"]/div[1]/div/div/main/div[1]/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/form/div[5]/button/div')

            elementSubmit.submit()
            self.driver.implicitly_wait(1)

    def execute(self, username: str, password: str, urlOfListImage: str):
        pinterest = Pinterest(username, password)
        

        self.driver.get("https://br.pinterest.com")

        self.login(pinterest)

        self.driver.get(urlOfListImage)

        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')

        images = self.driver.find_elements(By.TAG_NAME, "img")

        imagesHref = [image.get_attribute('src') for image in images]

        path = os.getcwd()
        path = os.path.join(path,'tmp')

        os.mkdir(path)   

        counter = 0

        for imageHref in imagesHref:
            saveAs = os.path.join(path, f'image{counter}.jpg')
            wget.download(imageHref, saveAs)
            counter += 1
