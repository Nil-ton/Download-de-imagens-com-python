from infra.selenium.Selenium import Selenium
from application.useCase.scrapingImage.scrapingImagePinterest import ScrapingImagePinterest

username = input('username: ')
password = input('password: ')
urlOfListImage = input('url: ')

selenium = Selenium()
scraping = ScrapingImagePinterest(selenium)

scraping.execute(username, password, urlOfListImage)