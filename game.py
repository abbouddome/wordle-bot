import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from patterns import Pattern


WEBSITE = "https://www.nytimes.com/games/wordle/index.html"


class Game():
    def __init__(self):
        self.running = True
        self.turn = 0
        self.browser = webdriver.Chrome()
        self.browser.get(WEBSITE)
        time.sleep(2)
        self.delete_popups()
        self.background = self.browser.find_element(By.TAG_NAME, "html")

    def delete_popups(self):
        "Gets rid of the cookies and rules popups"
        cookies = self.browser.find_element(By.ID, "pz-gdpr-btn-closex")
        cookies.click()
        rules = self.browser.find_element(By.CLASS_NAME, "game-icon")
        rules.click()

    def play_turn(self, word):
        """Types word, returns the result"""
        self.background.send_keys(word)
        self.background.send_keys(Keys.ENTER)
        self.turn += 1
        time.sleep(3)

        row = self.browser.find_element(By.XPATH, f"""//*[@id="wordle-app-game"]/div[1]/div/div[{self.turn}]""")
        tiles = row.find_elements(By.TAG_NAME, "div")
        results = [tile.get_attribute("data-state") for tile in tiles if tile.get_attribute("data-state")]
        print(results)
        turn = Turn(word, results)

        if turn.pattern.readable_pattern() == "22222":
            self.running = False
    
        return turn

class Turn:
    def __init__(self, guess, results):
        self.guess = guess
        self.pattern = Pattern(results, guess, turn_to_pattern=True)