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
        self.background = self.browser.find_element(By.TAG_NAME, "html")
        self.background.click()

    def play_turn(self, word):
        """Types word, returns the result"""
        self.background.send_keys(word)
        self.background.send_keys(Keys.ENTER)
        time.sleep(3)

        host = self.browser.find_element(By.TAG_NAME, "game-app")
        game = self.browser.execute_script("return arguments[0].shadowRoot.getElementById('game')", host)
        shadow_board = game.find_element(By.ID, "board")
        rows = self.browser.execute_script("return arguments[0].getElementsByTagName('game-row')", shadow_board)
        row = self.browser.execute_script("return arguments[0].shadowRoot.querySelector('.row').innerHTML", rows[self.turn])
        self.turn += 1

        bs = BeautifulSoup(row, 'html.parser')
        results = [tile_data.get('evaluation') for tile_data in bs.findAll('game-tile')]
        turn = Turn(word, results)

        if turn.pattern.readable_pattern() == "22222":
            self.running = False
            """time.sleep(3)
            game_modal = game.find_element(By.TAG_NAME, "game-modal")
            shadow_stats = self.browser.execute_script("return arguments[0].shadowRoot.getElementsByCssSelector('div')", game_modal)
            #game_stats = self.browser.execute_script("return arguments[0].shadowRoot.getElementByClassName('share-button')", shadow_stats)
            print(shadow_stats)
            #print(game_stats)"""
        
        return turn


class Turn:
    def __init__(self, guess, results):
        self.guess = guess
        self.pattern = Pattern(results, guess, turn_to_pattern=True)