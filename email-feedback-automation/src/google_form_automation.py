from selenium import webdriver
from selenium.webdriver.common.by import By
import json

def submit_to_form(data):
    with open('config/google_form_config.json') as f:
        config = json.load(f)

    driver = webdriver.Chrome()
    driver.get(config["form_url"])

    driver.find_element(By.CSS_SELECTOR, config["fields"]["customer_name"]).send_keys(data["CustomerName"])
    driver.find_element(By.CSS_SELECTOR, config["fields"]["order_id"]).send_keys(data["OrderID"])
    driver.find_element(By.CSS_SELECTOR, config["fields"]["feedback_category"]).send_keys(data["Category"])
    driver.find_element(By.CSS_SELECTOR, config["fields"]["sentiment_score"]).send_keys(data["SentimentScore"])

    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    driver.quit()
