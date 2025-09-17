from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

#Task 6

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

url = "https://owasp.org/www-project-top-ten/"
driver.get(url)

top = driver.find_elements(By.XPATH, "//a[contains(@href, 'A0')]")

owasp = []
for element in top:
    vulnerable = {
        "title": element.text.strip(),
        "link": element.get_attribute("href")
    }
    owasp.append(vulnerable)

print(owasp)

with open('owasp_top_10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(owasp)