from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

options = Options()
options.add_argument("--incognito")
options.add_argument("--mute-audio")

driver = webdriver.Chrome(options=options)

url = "https://open.spotify.com/track/5EbwDW4cgCWcbTt5HRN6sV"

while True:
    driver.get(url)
    print("Playing Spotify track...")
    time.sleep(random.randint(180, 240))  # adjust based on track length
