import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup


WEBSITE = "https://www.powerlanguage.co.uk/wordle/"


class Game():
    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.get(WEBSITE)
        time.sleep(2)
        self.background = self.browser.find_element(By.TAG_NAME, "html")
        self.background.click()
        self.turn = 0

    def play_turn(self, word):
        """Types word, returns the result"""
        self.background.send_keys(word)
        self.background.send_keys(Keys.ENTER)
        time.sleep(1)

        host = self.browser.find_element(By.TAG_NAME, "game-app")
        game = self.browser.execute_script("return arguments[0].shadowRoot.getElementById('game')", host)
        shadow_board = game.find_element(By.ID, "board")
        rows = self.browser.execute_script("return arguments[0].getElementsByTagName('game-row')", shadow_board)
        row = self.browser.execute_script("return arguments[0].shadowRoot.querySelector('.row').innerHTML", rows[self.turn])
        self.turn += 1

        bs = BeautifulSoup(row, 'html.parser')
        results = {}
        for word in bs.findAll('game-tile'):
            letter = word.get('letter')
            evaluation = word.get('evaluation')
            results[letter] = evaluation

        return results

    def end_game():
        pass
