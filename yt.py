from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import random

# Setup Chrome options
options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")  # To avoid noise

# Path to ChromeDriver
driver = webdriver.Chrome(options=options)

# Your playlist URL
url = "https://music.youtube.com/playlist?list=OLAK5uy_lpbVFKWAojZ3lYzpqxCTrIbvxZ0VWaU6g"

while True:
    driver.get(url)
    print("Playing YouTube Music...")
    
    # Random delay (simulate human behavior)
    time.sleep(random.randint(180, 240))  # 3–4 minutes
