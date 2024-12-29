
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

start_url = "https://manblunder.com/articlesview/soundarya-lahari-verse-1"  
driver.get(start_url)
driver.implicitly_wait(10)

def scrape_page():
    try:
        content = driver.find_element(By.CSS_SELECTOR, "div.post-content").text
        print("Scraped Content:")
        print(content)
        print("-" * 50)
        with open("/Users/yuktha/Documents/Soundarya_Lahari/soundarya_lahari.txt", "a") as file:
            file.write(content + "\n" + "-" * 50 + "\n")
    except Exception as e:
        print("Error scraping content:", e)

def go_to_next_article():
    try:
        next_button = driver.find_element(By.XPATH, "//a[contains(@class, 'btn-pagination') and contains(@onclick, 'frm_submit1')]")
        next_button.click()
        time.sleep(2)  
    except Exception as e:
        print("Error navigating to next article:", e)
        return False  
    return True

while True:
    scrape_page()
    if not go_to_next_article():
        print("No more articles to scrape.")
        break

driver.quit()
